# Variables
n = input("Enter the first number of the range: ")
m = input("Enter the last number of the range: ")
    
def multiples():
    num_sum = 0
    for i in range(int(n),int(m)):
        if i % 3 == 0 or i % 5 ==0:
            print(i)
            num_sum += i
            
        else:
            continue    
    print("the sum of these numbers is: ", num_sum)


multiples()

