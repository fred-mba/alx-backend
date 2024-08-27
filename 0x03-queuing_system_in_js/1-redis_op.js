import { createClient, print } from 'redis';

/**
 * Adds two functions:
 * 1. setNewSchool:
 * It accepts two arguments schoolName, and value.
 * It should set in Redis the value for the key schoolName
 * It should display a confirmation message using redis.print
 * 2. displaySchoolValue:
 * It accepts one argument schoolName.
 * It should log to the console the value for the key passed as argument
 */
const client = createClient();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) => console.error(`Redis client not connected to the server: ${err.message}`));

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, value) => console.log(value));
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
