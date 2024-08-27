import { createClient } from 'redis';
// Subscriber receives message on the channel and logs it to the console

const client = createClient();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) => console.error(`Redis client not connected to the server: ${err.message}`));

client.subscribe('holberton school channel');
client.on('message', (channel, message) => {
  console.log(`${message}`);
  if (message === 'KILL_SERVER') {
    client.unsubscribe('holberton school channel');
    client.quit();
  }
});
