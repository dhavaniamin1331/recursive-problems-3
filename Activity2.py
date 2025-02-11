# Program to move n dsks in Tower of Hanoi 

def Hanoi(n , a, b, c):
    if n == 1:
        print("Move disk 1 from rod",a, "to rod",b)
        return
    # move n-1 disk rom a to b
    Hanoi(n-1, a, c, b)
    print("Move disk",n, "From rod",a,"to rod",b)
    Hanoi(n-1, c, b, a)

n = 4
Hanoi(n, 'A', 'C', 'B')