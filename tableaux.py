global branchNum
global fatherNumArr
branchNum = 1
fatherNumArr = [0]
def pr_erase(x):
    counter = 0
    help=0
    if(len(x)==1 or len(x)==2):
        return x
    for i in range(len(x)):
        if x[i] == "(":
            counter+=1
            help+=1
        elif x[i] == ")":
            counter-=1
        if counter == 0 :
            if i == len(x) -1 and help!=0 :
                return (pr_erase(x[1:len(x)-1]))
            else :
                return x
def negation_find(x):
    x = pr_erase(x)
    if len(x) == 1:
        x = "~" + x
        return  x
    if len(x) == 2 :
        x = x[1:]
        return x
    counter = 0 
    for i in range (len(x)):
        if x[i] == "(":
            counter +=1
        elif x[i] == ")":
            counter -=1
        elif ( x[i] == "^" and counter == 0 ):
            return "(" + negation_find(x[:i]) + ")" + "V" + "(" + negation_find(x[i+1 : ]) + ")"
        elif ( x[i] == "V" and counter == 0 ):
            return "(" + negation_find(x[:i]) + ")" + "^" + "(" + negation_find(x[i+1 : ]) + ")"
        elif ( x[i] == ">" and counter == 0 ):
            return "(" + x[:i] + ")" + "^" + "(" + negation_find(x[i+1 :]) + ")"
def negation_match(x):
    numNeg=0
    check=False
    for i in range(len(x)):
        if x[i]=="~" :
            numNeg+=1
            for j in range(i+1,len(x)):
                if(x[j]=="~"):
                    numNeg+=1
                    check=True
                else:
                    if(numNeg%2 == 0):
                        x = x[:i] + x[j:]  
                        numNeg=0    
                        break              
                    elif(numNeg%2 != 0):
                        x = x[:i] + "~" + x[j:] 
                        numNeg=0
                        break
            if(check):
                break
    if(check):
        return negation_match(x)
    else:
        return x 
def do_negation(x):
    x = pr_erase(x)
    x=negation_match(x)
    checkEnd=False
    help=0
    for i in range(len(x)):
        if (x[i]=="~"):
            counter = 0
            for j in range(i+1,len(x)):
                if x[j]=="(":
                    counter+=1
                elif x[j]==")":
                    counter-=1
                if counter==0 :
                    x = x[:i]  +negation_find(x[i+1:j+1]) + x[j+1:]
                    if(len(x[i+1:j+1])>2):
                        help+=1
                    break 
    if(help>0):
        return do_negation(x) 
    return x 
def leaf_check(x):
    for i in range (len(x)):
        if x[i]=="^" or x[i]=="V" or x[i]== ">":
            return False
    return True
def or_string_help(x , father):
    global branchNum
    global fatherNumArr
    counter=0
    start_index=0
    end_index=len(x)
    beforV=""
    afterV=""
    for i in range(len(x)):
        if x[i] == "(":
            counter +=1
        elif x[i] == ")":
            counter -=1 
        elif x[i]=="V" and counter==0:
            for j in range(i+1 , -1 , -1):
                if x[j]==",":
                    start_index=j+1
                    break
            beforV = x[start_index:i]
            for k in range(i+1,len(x)):
                if x[k]==",":
                    end_index=k-1
                    break
            afterV=x[i+1:end_index+1]
            break
    beforV = x[:start_index] + beforV + x[end_index+1 :]
    afterV = x[:start_index] + afterV + x[end_index+1 :]
    print("vertex :" , end=" ")
    print(branchNum , end=" -> ")
    print(beforV , end="     ")
    print("(" , end="")
    print(father , end="")
    print(")")
    branchNum+=1
    successor(beforV , father)
    print("vertex :" , end=" ")
    print(branchNum , end=" -> ")
    print(afterV , end="     ")
    print("(" , end="")
    print(father , end="")
    print(")")
    branchNum+=1
    successor(afterV,father)
    fatherNumArr=fatherNumArr[:len(fatherNumArr)-1]
def ifmaker(x,i):
    counter2=0
    counter3=0
    startX=0
    endCheck=False
    endX=len(x)
    for j in range(i-1,-1,-1):
        if x[j]=="(":
            counter2+=1
        elif x[j]==")":
            counter2-=1
        if counter2==0 or x[j]==",":
            startX=j
            for k in range(i+1,len(x)):
                if endCheck :
                    break
                if x[k]=="(":
                    counter3+=1
                elif x[k]==")":
                    counter3-=1  
                if counter3==0 or x[k]==",":
                    endX=k
                    x = x[:j] +"(" +"("+negation_find(x[j:i])+")" + "V" + x[i+1:k+1] + ")" + x[k+1:]
                    endCheck=True
                    break
    return successor(x ,fatherNumArr[len(fatherNumArr)-1] )
def successor(x,father):
    global branchNum
    global fatherNumArr
    x = pr_erase(x)
    counter = 0
    strArr=[]
    andArr=[]
    check=True
    while((leaf_check(x)==False) and check):
        for i in range(len(x)):
            if x[i] == "(":
                counter +=1
            elif x[i] == ")":
                counter -=1
            elif (x[i]=="^" and counter==0):
                x = x[:i] + "," + x[i+1:]
                print("vertex :" , end=" ")
                print(branchNum , end=" -> ")
                print(x , end="     ")
                print("(" , end="")
                print(father , end="")
                print(")")
                branchNum+=1
                andArr.append(x)
            elif (x[i]=="V" and counter==0):
                fatherNumArr.append(branchNum-1)
                or_string_help(x , branchNum-1)
                branchNum+=1
                check=False
                break
            elif (x[i]==">" and counter==0):
                return ifmaker(x,i )
        strArr = x.split(",")
        for i in range(len(strArr)):
            strArr[i] = pr_erase(strArr[i])
        newX=""
        newX += strArr[0] 
        for i in range( 1, len(strArr) ):
            newX += "," +strArr[i]
        strArr=[]
        x=newX
print("Enter your string :")
x= str(input())
print("vertex : 0 ->" , end=" ")
print(x , end="     ")
print("(0)")
m = do_negation(x)
successor(m,0)