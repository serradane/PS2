import math
import statistics
import hashlib

a_file = open("tests/test_50bits_10000_A.txt", "r")
b_file = open("tests/test_50bits_10000_B.txt", "r")
c_file = open("tests/test_50bits_10000_C.txt", "r")

with open('introduction.txt', 'r') as file:
    data = file.read()

list_of_A = []
for line in a_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_A.append(line_list)

a_file.close()

list_of_B = []
for line in b_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_B.append(line_list)

b_file.close()

list_of_C = []
for line in c_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_C.append(line_list)

c_file.close()

def printPascal(n:int):
  
    # An auxiliary array to store 
    # generated pascal triangle values
    arr = [[0 for x in range(n)] 
              for y in range(n)] 
  
    # Iterate through every line
    # and print integer(s) in it
    for line in range (0, n):
  
        # Every line has number of 
        # integers equal to line number
        for i in range (0, line + 1):
  
            # First and last values 
            # in every row are 1
            if(i == 0 or i == line):
                arr[line][i] = 1
  
            # Other values are sum of values
            # just above and left of above 
            else:
                arr[line][i] = (arr[line - 1][i - 1] + 
                                arr[line - 1][i])
    return arr
                          

def simple_case(n, confinterval):
    a = (2**n)*confinterval
    array = printPascal(n+1)
    temp = a
    i = 1
    temp = temp - array[n][n//2]
    while temp>=1 and i<=(n-1)//2:
        temp = temp - array[n][n//2+i]
        temp = temp - array[n][n//2-i] 
        i = i+1
        # print("temp:", temp)
    return i-1


def complex_case(n, confinterval, times):
    difference = []
    for i in range(5,n+1):
        expected = (math.sqrt(i)/2)*times
        experimental = simple_case(i,confinterval)
        difference.append((expected-experimental)**2)
        print("n =",i, "experimental t:",experimental, "expected t:","{:.4}".format(expected), "difference:","{:.4}".format(abs(experimental-expected)))
    print("Standard deviation:", "{:.4}".format(statistics.stdev(difference)))

print("Confidence interval = 0.95")
complex_case(100, 0.95, 1.96)
print("-------------------")
print("Confidence interval = 0.99")
complex_case(100, 0.99, 2.58)

def check_random(key):
    length = len(key)
    # print(key)
    t = simple_case(length, 0.99)
    h = 0
    for i in key:
        i = int(i)
        if i == 1:
            h = h+1
    if h<=length//2+t and h>=(length//2)-t:
        return True
    else:
        return False


def is_random(data):
    data = data[1:]
    random = True
    i = 0
    horizontal = 0
    vertical = 0
    while i<=len(data)-1:
        # print("horizontal", i)
        random = check_random(data[i][0])
        if(random):
            horizontal += 1 
        i += 1
    horizontal_p = (horizontal/len(data))*100
    k = 0
    while k<=len(data[0][0])-1:
        # print("vertical", k)
        listofbits = [item[0][k] for item in data]
        for i in range(len(listofbits)//500):
            j = i*500
            # print(j, j+500)
            num = ''.join(listofbits[j:j+500])
            random = check_random(num)
            # print(random)
        if(random):
            vertical += 1
        k += 1
    vertical_p = (vertical/len(data[0][0]))*100
    print("horizontal percentage:",horizontal_p,"vertical percentage:", vertical_p)
    return horizontal_p >= 99 and vertical_p >= 95
# print("50 bits 10000, A:",is_random(list_of_A))
# print("50 bits 10000, B:",is_random(list_of_B))
# print("50 bits 10000, C:", is_random(list_of_C))


string = 'Serra Emrullahi seviyor'
string2 = 'Ben de snei cok seviyprum'
def hashfunc(d, word):
    if d==1:
        h = hashlib.blake2b(digest_size=20)
    if d==2:
        h = hashlib.md5()
    if d==3:
        h = hashlib.sha1()
    word = repr(word).encode()
    h.update(word)

    ini_string = h.hexdigest()
    res = "{0:08b}".format(int(ini_string, 16))

    # Print the resultant randomness
    return check_random(res)

def hash_randomness(str, d):
    count = 0
    str = str.split()
    for i in str:
        random = hashfunc(d, i)
        if(random):
            count += 1
    res = (count/len(str))*100
    return res

# print("Percentage of the randomness of the text using the blake2b hash fuction:",hash_randomness(data, 1))
# print("Percentage of the randomness of the text using the md5 hash fuction:", hash_randomness(data, 2))
# print("Percentage of the randomness of the text using the sha1 hash fuction:", hash_randomness(data, 3))