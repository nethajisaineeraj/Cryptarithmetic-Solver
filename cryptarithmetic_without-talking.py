def unique_elements(string,num_list):
    list1=[]
    list2=[]
    for i in range(len(string)):
        if(string[i] not in list1):
            list1.append(string[i])
            list2.append(num_list[i])
    return (list1,list2)

def step2(string,num):
    num_string=str(num)
    for i in range(len(string)):
        for j in range(len(string)):
            if(i!=j):
                try:
                    if(string[i]==string[j]):
                        if(num_string[i]==num_string[j]):
                            continue
                        else:
                            return False
                except:
                    return False
                else:
                    try:
                        if(num_string[i]!=num_string[j]):
                            continue
                        else:
                            return False
                    except:
                        return False
    return True

def step1(string1, string2, string3):
    m=len(string1)
    n=len(string2)
    str1_low_limit=10**(m-1) 
    str1_upr_limit=(10**m)-1
    str2_low_limit=10**(n-1)
    str2_upr_limit=(10**n)-1
    for i in range(str1_low_limit,str1_upr_limit+1):
        if(step2(string1,i)):
            for j in range(str2_low_limit,str2_upr_limit):
                if(step2(string2,j)):
                    if(step2(string1+string2,str(i)+str(j))):
                        if(step2(string3,i+j)):
                            if(step2(string1+string2+string3,str(i)+str(j)+str(i+j))):
                                return (i,j,i+j)
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
        else:
            continue
        


print("*****Welcome crypt Arithmetic Solver*****")
print("Enter the inputs ")
string1=input("enter first word :")
string2=input("enter second word :")
string3=input("enter third word :")

print("Wait for a while your output will be displayed shortly ......")

result=step1(string1,string2,string3)
list1,list2=unique_elements(string1+string2+string3,str(result[0])+str(result[1])+str(result[2]))
for i in range(len(list1)):
    print(list1[i]+" = "+list2[i])