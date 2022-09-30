import math
import scipy.stats as st 
import itertools

a_file = open("tests/test_20bits_500_A.txt", "r")
list_of_A = []
for line in a_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_A.append(line_list)
a_file.close()
list_of_A = list_of_A[1:]

L = [1,1,1,0,1,1,1,0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,0,1,1,1,0,0,0,1]
def getRuns(l):
    runs = [sum(1 for _ in r) for _, r in itertools.groupby(l)]
    return runs

def waldwolf(R, n1, n2, n):
    seR = math.sqrt( ((2*n1*n2) * (2*n1*n2 - n)) / ((n**2)*(n-1)) )
    muR = ((2*n1*n2)/n) + 1
    z = (R - muR) / seR
    return z

def wwfunc(data):
    sump = 0
    for i in data:
        L = [*i[0]]
        print(L)
        L = [int(item) for item in L]
        listOfRuns = getRuns(L) 
        z = waldwolf(len(listOfRuns), sum(L), len(L)-sum(L), len(L))
        p_values_two = st.norm.sf(abs(z))*2 
        sump += p_values_two
    return sump/len(data)

print("Percentage:", wwfunc(list_of_A))