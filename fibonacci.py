'''
Sequência de Fibonacci
Autor:Felipe Pinto Marinho
Data:25/08/2023
'''

#Resolução utilzando Recursão
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


#Resolução utilizando Programação dinâmica
def fibonacci_dp(n):
    #Toma os dois primeiros números de fibonacci como sendo 0 e 1
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i-1] + f[i-2])

    return f[n]

#Testes
if __name__ == "__main__":
    n = 10
    print(n, 'th sequência de fibonacci:')
    print(fibonacci(n))
    print(fibonacci_dp(n))


from sys import maxsize

# Function to find the maximum contiguous subarray
# and print its starting and end index

def maxSubArraySum(a, size):

    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(0, size):

        max_ending_here += a[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1

    print("Maximum contiguous sum is %d" % (max_so_far))
    print("Starting Index %d" % (start))
    print("Ending Index %d" % (end))


# Driver program to test maxSubArraySum
a = [-2, -3, 4, -1, -2, 1, 5, -3]
maxSubArraySum(a, len(a))