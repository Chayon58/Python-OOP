class Cat:
    def __init__(self,color,action):
        self.color= color
        self.action = action
    def view(self,num,clr):
        num=num+ 6
        clr1 = clr
        clr1[0]="Green"
        print("Method inside : ",num)
        print("Method inside :",clr)

#=======================================================

colors = ["Black","Red","Yellow","White"]
c1= Cat("white","Jumping")
x= 55
c1.view(x,colors)
print("Method outside",x)
print("Method outside",colors)

