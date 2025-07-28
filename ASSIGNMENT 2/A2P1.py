item=int(input("Enter the number of items:"))
if(item<10):
    print(f"Total Cost is {item*120}")
elif(item>=10 and item<=99):
    print(f"Total Cost is {item*100}")
elif(item>=100):
    print(f"Total Cost is {item*70}")
