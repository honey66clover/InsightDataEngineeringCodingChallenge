For the second problem, numpy package is used to store and manipulate array.
The second problem is to find out the running median of a stream of integers. 
Each integer is the numbers of words of a line.
Here I use counting sort which is good for a large amount of integers while the integer is not so big(<65536).
On the other hand, if the integers are big but the amount is relatively small, we can use a maxheap to store integers smaller than the current median,
and a minheap to store integers larger than the current median.