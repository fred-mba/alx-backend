/**
 * Write job create function
 * If jobs is not an array, it should throw an Error with a message
 */

const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Job is not an array');
  }
  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData)
      .save((err) => {
        if (!err) console.log(`Notification job created: ${job.id}`);
      });
    job
      .on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      })
      .on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      })
      .on('failed', (err) => {
        console.log(`Notification job ${job.id} failed: ${err.message}`);
      });
  });
};
export default createPushNotificationsJobs;
