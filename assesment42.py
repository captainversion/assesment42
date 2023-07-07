
number = list(map(int,input("enter the numbers:").split(",")))
print("original list is:",number)
def triple(x):
  return 3*x 
triple_num = map(triple, number)
print("the output list is:",list(triple_num))