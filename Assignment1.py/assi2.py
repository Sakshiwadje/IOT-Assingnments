a=int(input("Enter number :"))
b=int(a%10)
a=a/10
c=int(a%10)
a=a/10
d=int(a%10)
a=a/10
e=int(a%10)
a=a/10  

print(f"{e} {d} {c} {b}")
print(f"9361 = {e*1000} + {d*100} + {c*10} + {b}")

print(f"{b} {c} {d} {e}")