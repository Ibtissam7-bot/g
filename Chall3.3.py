L = [7 , 23 , 5 , 23 , 7 , 19 , 23 , 12 , 29]
a= 23
count=0
for i in L:
    if i==a:
        count+=1
print(f"Le nombre {a} apparaît {count} fois.")