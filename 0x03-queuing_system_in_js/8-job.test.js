// Test for job creation
import { expect } from 'chai';
import { createQueue } from 'kue';
import sinon from 'sinon';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
  let queue;
  const consoleSpy = sinon.spy(console, 'log');
  before(() => {
    queue = createQueue();
    queue.testMode.enter();
  });
  after(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });
  it('should throw an error an exit if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Job is not an array');
  });
  it('should create jobs inside a queue', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
    ];
    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);

    queue.process('push_notification_code_3', () => {
      expect(consoleSpy.calledWith(`Notification job created: ${queue.testMode.jobs[0].id}`)).to.be.true;
      consoleSpy.restore();
    });
  });
  it('should check on the progress event', (done) => {
    queue.testMode.jobs[0].addListener('progress', () => {
      expect(consoleSpy.calledWith('Notification job', queue.testMode.jobs[0].id, '25% complete')).to.be.true;
      done();
    });
    queue.testMode.jobs[0].emit('progress', 25);
  });
  it('should check if create event is complete', (done) => {
    queue.testMode.jobs[0].addListener('complete', () => {
      expect(consoleSpy.calledWith('Notification job', queue.testMode.jobs[0].id, 'complete')).to.be.true;
      done();
    });
    queue.testMode.jobs[0].emit('complete');
  });
});
