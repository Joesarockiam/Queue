q=[]

n_1=int(input("ENTER THE SIZE OF THE CIRCULAR QUEUE:"))

for i in range(n_1):

    q.append([0,0])

front=-1
print(q)
    

rear=-1




def push(q):
    global rear,front

    if full(q):  
        if (front==-1 and rear==-1)  :
            front=front+1
            rear+=1

        elif rear==n_1-1:
            rear=0
        else:
            rear+=1
        q[rear]=[int(input("ENTER THE CAR NUMBER:")),int(input("ENTER THE APPROXIMATE RETURN TIME:"))]    
    else:
         print("\n\nTHE PARKING LOT  IS FULL")


def dele(q):
    global rear,front

    if empty(q):
        piriot=0
        for i in range(len(q)):
            if q[i][1]>=q[piriot][1]:    
              piriot=i
              front=i
        q[front]=[0,0]

        if q[front]==[0,0]:
            front+=1
            

    else:
         print("\n\nTHE QUEUE IS EMPTY")





def empty(q):

    if not(rear==-1 and front==-1):
        return 1

    else:
        return 0






            
def full(q):

    if not ((front==0 and rear==n_1-1) or (front-1==rear)):
        return 1

    else:
        return 0
k=0
while True:

    n=int(input("\tSLOT OPTIONS\n1)INSERT\n2)DELETE\n3)EMPTY\n4)FULL\nENTER YOUR CHOICE:"))

    if n==1:
        push(q)
                  
    elif n==2:
        dele(q)

    elif n==3:

        if empty(q):
            print("EMPTY OF QUEUE: FALSE")

        else:
             print("EMPTY OF QUEUE: TRUE")

    elif n==4:

        if full(q):
            print("FULL OF QUEUE: FALSE")

        else:
             print("FULL OF QUEUE: TRUE")

    else:
        print("ENTER THE CORRCT OPTION..")
    print("F:",front,"R",rear)    
    print(q)
    k+=1
    
