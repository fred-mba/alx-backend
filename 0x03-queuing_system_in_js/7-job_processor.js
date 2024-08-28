import { createQueue } from 'kue';
/**
 * Track progress and errors with Kue: Create the Job processor
 * Create an array that will contain the blacklisted phone numbers
 * Create a function sendNotification that takes 4 arguments:
 * `phoneNumber`, `message`, `job`, and `done`
 * Create a queue with Kue that will proceed job of the queue
 * push_notification_code_2 with two jobs at a time
 */
const blacklistedNumbers = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  }
};

const queue = createQueue();

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
  done();
});
