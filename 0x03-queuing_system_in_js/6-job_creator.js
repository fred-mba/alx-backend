import { createQueue } from 'kue';
// Create a queue with Kue
const queue = createQueue();

const job = queue.create('push_notification_code', {
  phoneNumber: '1246-3578-1012',
  message: 'Phone number added successfully',
});

job
  .on('enqueue', () => {
    console.log(`Notification job created:, ${job.id}`);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed attempt', () => {
    console.log('Notification job failed');
  });
job.save();
