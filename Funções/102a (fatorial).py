def fatorial(n=0,show=False):
    total=n
    for i in range(n - 1, 0, -1):
        total *= i

    if show==False:
        return f"{total}"
    elif show==True:
        for c in range(n, 0, -1):
            print(c,end="")
            if c>1:
                print(f" x ",end="")
            else:
                print(" = ",end="")
        return f"{total}"

num=int(input("Indique um numero : "))
show=str(input("Quer ver as contas [s][n]:")).upper().strip()
if show=="S":
    print(fatorial(num, True))
else:
    print(fatorial(num,False))
