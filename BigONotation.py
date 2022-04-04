"""
What is "better"?
1. Takes less time
2. Takes less space

Big O is used to formalize counting.
Allows us to express how the runtime of an algorithm grows with the input

Big O is only concerned with the worst case scenario (the upper bound)

* Ignore smaller terms
5N^2 + 3N + 1 = O(N^2)

Note : 
1. Arithmetic operations, assignments are constants
2. Direct array element access(by index) is a constant


Space complexity : 
1. When analyzing space complexity, we only care about the space our algorithm takes
2. We don't include the space taken up by the input

Space complexity of popular data structures

Hash tables : O(N)
Stacks : O(N)
Queues : O(N)
Strings : O(N)
Arrays : O(N) 

2D Arrays : O(NM)

Logarithms: 
1. A not so straight forward complexity like O(1), O(N)
2. Some algorithms have a complexity of O(log(N)) or O(NLog(N))

The No. of times you can divide a number by the log's base, before you get a value that's less than or equal to 1

Log(N) is better than N
NLog(N) is better than N^2
"""