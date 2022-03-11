def sumodd(n):
 

    return (n * n)
 
# Function to find the
# sum of first N even numbers

def sumeven(n):
 

    return (n * (n + 1))
 
 
# Function to overall
# find the sum of series

def findSum(num):
 
 

    # Initial odd numbers

    sumo = 0
 

    # Initial even numbers

    sume = 0
 

    # First power of 2

    x = 1
 

    # Check for parity

    # for odd/even

    cur = 0
 

    # Counts the sum

    ans = 0

    while (num > 0):
 

        # Get the minimum

        # out of remaining num

        # or power of 2

        inc = min(x, num)
 

        # Decrease that much numbers

        # from num

        num -= inc
 

        # If the segment has odd numbers

        if (cur == 0):
 

            # Summate the odd numbers

            # By exclusion

            ans = ans + sumodd(sumo + inc) - sumodd(sumo)
 

            # Increase number of odd numbers

            sumo += inc

         

        # If the segment has even numbers

        else:
 

            # Summate the even numbers

            # By exclusion

            ans = ans + sumeven(sume + inc) - sumeven(sume)
 

            # Increase number of even numbers

            sume += inc

         
 

        # Next set of numbers

        x *= 2
 

        # Change parity for odd/even

        cur ^= 1

     

    return ans
 


n = 2

print(findSum(n))
 

 
