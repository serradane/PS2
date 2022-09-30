
# Problem Set 2 Question 2
One of the key assumptions of hyper-log-log is that the input keys when
passed through the hash functions produce a random set of hash values. With this project we are able to 
test randomness of a given set.




## Usage

For part A: 

Call the function complex_case as following,
complex_case(n, confidence interval, expected (t/std)).

Note: expected (t/std) is 1.96 when confidence interval is .95 and 2.58 when it is .99.


For part B: 

Call the function is_random as following,
is_random(list_of_A).

Note: Here data is list of lines in the test cases.

For part C:

Call the function hash_randomness as following,
hash_randomness(data, d)

Note: Here data is a read text file. And if d is 1 the hash function is blake2b. If it is 2 the hash function is md5.
And if it is 3 the hash function is sha1.




## Authors

- [@serradane](https://www.github.com/serradane) 

  
