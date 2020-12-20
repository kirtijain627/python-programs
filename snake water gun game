import random
list1 = ['snake', 'water', 'gun']
i = 0
count = 0
uc = 0
while(i<10):
    i = i+1
    user = input("enter snake water or gun: ")
    print("your choice is ",user)
    comp = random.choice(list1)
    print("computer choice is ",comp)
    if(comp == "snake" and user == "water"):
        print("comp wins")
        count = count+1
    elif(comp == "snake" and user == "gun"):
        print("you win")
        uc = uc+1
    elif(comp == user):
        print("tie")
    elif(comp == "water" and user == "snake"):
        print("you win")
        uc = uc +1
    elif(comp == "water" and user == "gun"):
        print("comp wins")
        count = count+1
    elif(comp==user):
        print("tie")
    elif(comp == "gun" and user == "water"):
        print("you win")
        uc = uc+1
    elif(comp == "gun" and user == "snake"):
        print("comp wins")
        count = count+1
    else:
        print("tie")
print("computer wins ", str(count) + "times")
print("you win ", str(uc) + "times")


