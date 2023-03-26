'''def factorial(number):
    if number==1:
        return 1
    else:
        return number*factorial(number-1)
    

#n=int(input("Enter a number :"))

#print(factorial(n))

def squared(num):
    return num**2

print(squared(2))

#def greetings_function(name,greetings):
#    print("Happy New Year!, I wish you {}".format(name,greetings))

#greetings_function("Newton","Long life")

def circle(r):
    return 2*r,3.14*r**2

print(circle(9))

def srch(li_st,elem):
    count=0
    lb=0
    ub=len(li_st)
    for i in range(lb,ub,1):    #for(i=0;i<n;i++)
        if (elem==li_st[i]):
            count+=1
            print("The element is found at",i)
            
    print("No. of times the element is present :",count)
    
l1=[4,5,6,9,4,8,3]

srch(l1,4)'''

#To show the words present in the string and to count the no. of occurences
string="You're a slave to history. Even after Calamity, you fight against the only order that can guarantee the safety of your people. You, solely, are responsible for this "
string1="Search endlessly, Fight til we are free. Fly past the edge of the sea. No bended knee, No mockery. Somehow we still CARRY ON."
words=[]
count_words=[]

count=0
lb=0
ub=0
for i in range(0,len(string)):
    if string[i] in (' ','.',',') :
        ub=i
        words.append(string[lb:ub])
        lb=i+1

for j in words:
    for k in range(0,len(words)):
        if j==words[k]:
            count+=1
    count_words.append(count)
    count=0

d=dict(zip(words,count_words))

print(d)