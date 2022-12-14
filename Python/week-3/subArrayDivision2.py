#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    res = 0
    for i in range(len(s) - m + 1):
        if sum(s[i: i + m]) == d:
            res += 1

    return res

if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    print(f'Day: {d}')
    print(f'Month: {m}')
