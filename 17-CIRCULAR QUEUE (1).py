q=[]

n_=int(input("ENTER THE SIZE OF THE CIRCULAR QUEUE:"))

for i in range(n_):

    q.append(None)

front=-1

rear=-1




def push(q):
    global rear,front

    if full(q):
        n=int(input("ENTER THE NUMBER TO INSERT:"))

        if (front==-1 and rear==-1)  :
            front=front+1
            rear+=1

        elif rear==n_-1:
            rear=0

        else:
            rear+=1
        q[rear]=n 


    else:
         print("\n\nTHE QUEUE IS FULL")
       
    


def dele(q):
    global rear,front

    if empty(q):
        q[front]=None

        if front==rear:
            front,rear=-1,-1
            q=[]

        elif front==n_:
            front=0

        else:
            front=front+1   

    else:
         print("\n\nTHE QUEUE IS EMPTY")




def empty(q):

    if not(rear==-1 and front==-1):
        return 1

    else:
        return 0


def full(q):

    if not ((front==0 and rear==n_-1)):
        return 1

    else:
        return 0
    
    
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
    print(q)    

else:
    print("PARKING SLOT IS FULL...")                                                            
