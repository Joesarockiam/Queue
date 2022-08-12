cq=[]
front=0
rear=0
n=int(input("Enter the maximum size:"))
while rear!=n:
    c=int(input("1- Insertion\n2-Deletion\n3-View queue\n4-Length\n"))
    if c==1:
        if front==1 and rear==n:
            print("full")
        
        elif rear==front-1:
            print("full")
        if front<1:
            a=input("Enter the value:")
            cq.append(a)
            front+=1
            rear+=1
            print("front:",front,"rear:",rear)
        else:
            if rear==n and front!=1:
                a=input("Enter the value:")
                cq.append(a)
                rear=1
                print("front:",front,"rear:",rear)
            elif rear!=n:
                a=input("enter the value:")
                cq.append(a)
                rear+=1        
    elif c==2:
        if front==0:
            print("empty")
        else:
            if rear!=front:
                x=cq.pop(front-1)
                print(x)
                if front==n:
                    front=1
                    print("front:",front,"rear:",rear)
            elif rear==front:
                x=cq.pop(front-1)
                print(x)
                front=0
                rear=0
                print("front:",front,"rear:",rear)
                
                
        x=cq.pop(front-1)
        front+=1
        print("front:",front,"rear:",rear)
    elif c==3:
        print(cq)
    elif c==4:
        print("length:",len(cq))
    
        
