import { createClient, print } from 'redis';
import { promisify } from 'util';
/**
 * Using the client to store a hash value
 * The key of the hash should be HolbertonSchools
 * Use redis.print for each hset
 */
const client = createClient();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) => console.error(`Redis client not connected to the server: ${err.message}`));

client.hset('HolbertonSchools', 'Portland', '50', print);
client.hset('HolbertonSchools', 'Seattle', '80', print);
client.hset('HolbertonSchools', 'New York', '20', print);
client.hset('HolbertonSchools', 'Bogota', '20', print);
client.hset('HolbertonSchools', 'Cali', '40', print);
client.hset('HolbertonSchools', 'Paris', '2', print);

const hgetallAsync = promisify(client.hgetall).bind(client);
const hashGet = async () => {
  console.log(await hgetallAsync('HolbertonSchools'));
};

hashGet();
