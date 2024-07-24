## Caching
### Learning Objectives
1. What a caching system is
- A mechanism that temporarily stores(caches) data in a cache so that it can be quickly accessed without needing to fetch it from the original source each time.
- The main goal is to reduce data access time, latency, and to lower the load on an underlying slower data source.

2. What FIFO means
- An eviction policy type that removes the oldest items first when the cache reaches its capacity. When the cache is not full, new items are added to the cache in the order they were added.
- When the cache reaches its capacity and new item needs to be added, the item that has been in the cache longest is evicted to make space.
3. What LIFO means
- "Last In, First Out." It is a cache eviction policy where the most recently added cached data is the first to be removed when the cache reaches its capacity. Useflu inn scenarios where the most recently added data is likely to be needed soon.
- **Disadvantage**: Not well-suited for most caching scenarios, as it often evicts data that is still relevant and keeps less useful data.
- **Use cases**: Stack-based Scenarios where the most recent entries are less likely to be needed soon.

4. What LRU means
- Least Recently Used(LRU) is the most popular and widely used cache replacement policies. The LRU policy assumes that items which have not been used recently are less likely to be used in the near future. These items are tracked with `time stamp` or order of access. When the cache reaches its capacity and new item needs to be added, the item that has been accessed the least recently is evicted.
- **Disadvantages**: Implementing LRU can be more complex and computationally expensive compared to FIFO or LIFO because it requires tracking the order of access for all items.
- It requires additional data structures like linked lists to maintain the order of access, which can increase memory overhead.
- **Use cases**: Web caching, Database caching, Operating Systems.

5. What MRU means
- Most Recently Used(MRU) is the opposite of the LRU policy. It is a cache replacement policy that operates on the principle that most recently accessed or added items are the first to be removed when the cache reaches its capacity. It assumes the most recently used items are less likely to needed again soon.

6. What LFU means
- Least Frequently Used(LFU) is a cache replacement policy that evicts item with the `lowest access count` first when the cache reaches its capacity. If multiple items have have the same count, a secondary policy(such as FIFO) may be used to decide which item to evict.
- **Disadvantages**: Implementing LFU can be more complex and computationally expensive compared to FIFO or LIFO because it requires tra    cking and updating the access count for each items.
- Requires additional data structures to maintain the access counts, which can increase memory overhead.
- **Use cases**: Web caching, Database caching, Operating Systems.

7. What the purpose of a caching system
- **Reduced Latency**: Faster data access by storing frequently accessed data in a high-speed cache.
- **Lower Load on Backend Systems**: Reduces the need to fetch data from slower storage layers or perform expensive computations repeatedly.
- **Improved Scalability**: Enables systems to handle higher loads by offloading frequent requests to the cache.
- **Enhanced User Experience**: Faster response times for end-users in applications such as web browsing, online services, and gaming.

8. What limits a caching system have
- **Capacity Limits**: Caches have finite storage capacity. Once full, they must evict data to make room for new entries, which may lead to the removal of useful data.
- **Consistency Issues**: Ensuring that cached data is consistent with the original data source can be challenging, especially in distributed systems.
- **Overhead**: Maintaining the cache involves additional computational and storage overhead, which can impact system performance.
- **Eviction Policy Efficiency**: The effectiveness of a caching system heavily depends on the chosen eviction policy. An inappropriate policy may lead to inefficient caching and frequent cache misses.
- **Security Risks**: Caching sensitive data can introduce security vulnerabilities if not managed properly, as unauthorized access to the cache can lead to data breaches.
- **Complexity in Implementation**: Implementing and managing an efficient caching system can add complexity to the overall system architecture.

### Resources
- [Cache replacement policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29)
- [Cache replacement policies - LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_%28LIFO%29)
- [Cache replacement policies - LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_%28LRU%29)
- [Cache replacement policies - MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_%28MRU%29)
- [Cache replacement policies - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-Frequently_Used_%28LFU%29)
