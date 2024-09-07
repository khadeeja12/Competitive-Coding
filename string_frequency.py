from collections import defaultdict
def push( s):
    if s.isalpha():
        stack1.append(s)
    elif i.isdigit():
        stack2.append(s)

    return stack2
   

#push onto stack
str=input("enter the string and its frquency:")
stack1=[]
stack2=[]
for i in str:
    if i.isalpha():
        push(i)
    elif i.isdigit():
        push(i)
print(stack1)
print(stack2)
d=zip(stack1,stack2)

#add duplicate values
result_dic=defaultdict(list)
for key,freq in d:
    result_dic[key].append(int(freq))
final_dic=dict(result_dic)
print(final_dic)

#add the values in dictionary
sum_d={key: sum(value) for key,value in final_dic.items()}
print(sum_d)






    



