import { createClient, print } from 'redis';
import { promisify } from 'util';

/**
 * A copy of 2-redis_op_async.js:
 * function displaySchoolValue to use ES6 async / await
 */
const client = createClient();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) => console.error(`Redis client not connected to the server: ${err.message}`));

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
};

const getAsync = promisify(client.get).bind(client);

const displaySchoolValue = async (schoolName) => {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(err);
  }
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
