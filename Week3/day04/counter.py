
# Write a recursive function that takes one parameter: n and counts down from n.
def counter(n):
    if n == 0:
        return n
    else:
        #print(n)
        return counter(n-1), n


print(counter(5))