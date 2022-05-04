import array as arr
_name = "Hi"
# print(_name)    #decrypted form
# string="Hi"
# print(string)  #right variable declarations
str = "Hii"  # wrong because keyword
# print(str)

list1 = [1, 2, 3, [20, 30, [400]]]  # nested list
#print(list1[3][2][0])

'''
def find_leap_years(yr):
    leap_years=[]
    for i in range(yr, yr+4):
        if yr%400==0:
            l_year=yr
                    
        elif yr%100==0:
            pass
        elif yr%4==0:
            
        yr+=1
    return leap_years
leap_years=find_leap_years(2001)
print(leap_years)
'''
# Lonely integer

'''
def lonely_integer(lst):
    for i in lst:
        if i<0:
            lst[i]=-i
    c=set(lst)
    print(c)
lonely_integer([1,-1,2,-2,3])
'''
# lst=set(lst)


def lonely_integer(lst):
    lst1 = []
    for i in lst:
        if -i not in lst:
            lst1.append(i)


#lonely_integer([-3, 1, 2, 3, -1, -4, -2])
#lonely_integer([9, -105, -9, -9, -9, -9, 105])

'''
Create a function that takes a string as an argument and returns a coded version of the string
Ex:
hacker_speaks("javascript is cool")
a with 4
e with 3
i with 1
o with 0
s with 5
'''


def hacker_speak(str1):
    str1 = str1.replace('a' or 'A', '4')
    str1 = str1.replace('e' or 'E', '3')
    str1 = str1.replace('i' or 'I', '1').replace(
        'o' or 'O', '0').replace('s' or 'S', '5')
    print(str1)


#hacker_speak('javascript is cool')

# ***day 2***
# list
'''
list1 = [1, 2, 3]
list1.append((4, 5))
print(list1)

list1.extend((1, 3))
list1.extend((1, 3))
print(list1)

list1.insert(3, 'oppo')
print(list1)

# tuples
tuple1 = (1, 2, 3, 4, 5)
print(type(tuple1))

# dictonary {}
dict1 = {"brand": "Google", "year": 1976}
print(dict1)

# sets
set1 = {1, 2, 3, 4}
set1.remove(4)
print(set1)
set2 = {9, 8, 1, 2}
print(set1.union(set2))

# arrays

# arr1=array(1,2,3) its not an inbuilt function
car = ['ford', 'volvo', 'BMW']
car.append("honda")
print(car)
car.pop(2)
print(car)
car.remove("honda")
print(car)
'''

'''
a = arr.array('i', [1, 2, 3, 4, 5])
while True:
    print('1.print array')
    print('2.add elements')
    print('3.delete elements')
    print('4.exit')
    choice = int(input)
def vehicle(x):
    pass

#Stacks
class stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self,data):
        self.items.append(data)
        print('current stack:', self.items)
    def pop(self):
        return self.items.pop()
s=stack()
while True:
    print('1.push')
    print('2.pop')
    print('3.quit')
    do=int(input("enter your choice: "))
    if do==1:
        val=input("enter the value: ")
        s.push(val)
    elif do==2:
        if s.is_empty():
            print("stack is empty")
'''
#Day 3
import queue
stack=queue.LifoQueue()
stack.put(10)
stack.put(20)
stack.put(30)
print(stack.get())

class stack:
    def __init__(self):
        self.items=[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items==[]
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items
def rev_str(stack,input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])
    reverse_str=""
    while not stack.is_empty():
        reverse_str+=stack.pop()
    return reverse_str
stack=stack()
input_str="hello miss"
print(rev_str(stack,input_str))

#Linked List
class Node:
    def __init__(self, data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("node is not present there")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def delete_begin(self):
        if self.head is None:
            print("LL is empty")
        else:
            self.head=self.head.ref
    def delete_end(self):
        '''if self.head is None:
            print("LL is empty")
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=None'''
        ptr = self.head
        if(ptr!= None):
            next = ptr.ref
        while( next!= None and next.ref != None):
            ptr = ptr.ref
            next= next.ref
            if(next == None):
                self.head = None
            else:
                ptr.ref = None
        else:
            print("you have no node")
LL1=LinkedList()
LL1.add_begin(10)
LL1.add_end(100)
LL1.add_after(20,10)
LL1.print_LL()
LL1.delete_begin()
print("Deleting from start: ")
LL1.print_LL()
LL1.delete_end()
print("deleting from end: ")
LL1.print_LL()

#lists
def merge_list(list1, list2):
    merged_data=""
    res=[]
    j=len(list2)-1
    for i in list1:
        if list2[j]==None:
            list2[j]=''
        if  i==None:
            i=''
        merged_data=i+list2[j]
        j=j-1
        res.append(merged_data)
        a=' '.join(res)
    return a

#Provide different values for the variables and test your program
list2=['ue', 'is', 'y', 'he']
list1=['T', 'sk', None, 'bl']
merged_data=merge_list(list1,list2)
print(merged_data)

#lex_auth_0127426166978887681375

def merge_list(list1, list2):
    merged_data=""
    new_list2 = (list2[::-1])
    for i in range(0,len(list1)):
        data_1 = ""
        data_2 = ""
        if list1[i]:
            data_1 = (list1[i])
        if new_list2[i]:
            data_2 = (new_list2[i]) 
        merged_data += data_1 + data_2 + " "
    # print(merged_data.rstrip())
    return merged_data.rstrip()

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)

#lex_auth_0127426336682147841449

def check_double(list1,list2):
    new_list=[]
    #write your logic here
    for ele_1 in list1:
        if ele_1*2 in list2:
            new_list.append(ele_1)
    
    return new_list

#Provide different values for the variables and test your program
list1=[11,8,23,7,25,15]
list2=[6,33,50,31,46,78,16,34]
print(check_double(list1, list2))

####################
'''
try:
    t=int(input())
    while t>0:
        n=int(input())
        if n>=21:
            print("YES")
        else:
            print("NO")
        t=t-1
except:
    pass
'''

def div_cookies(x):
    t=[]
    try:
        for i in range(x):
            t1=int(input())
            t.append(t1)
        for i in range(x):   
            if t[i]>=21:
                print("YES")
            else:
                print("NO")
    except:
        pass  
#div_cookies(3)

def transac(w,bal):
    #try:
    if w%5==0 and w+0.50<=bal:
        #x=bal-w-0.50
        print(bal-w-0.50)
    else:
        print("%.2f" %bal)
    #except: pass
'''w,bal=input().split()
print(w,bal)
transac(int(w),float(bal))
'''

##############
#stacks
'''
data=[]
print(dir(data))

#create stack
def create_stack():
    pass'''


import queue
q=queue.Queue(maxsize=5)
#print(dir(q))

##########
#Doubly Linked List
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("empty doubly linked list")
        else:
            temp=self.head
            print('\nElements in DLL:')
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
    def insert_beginning(self,data):
        n=Node(data)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
    def insert_end(self,data):
        n=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp
    def insert_position(self,pos,data):
        n=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n #actual insertion of the new node n
    def delete_begin(self):
        temp=self.head #storing first node in temp
        self.head=temp.next #head is pointing to next that is 2nd node
        temp.next=None #for removing all references from first node
        self.head.prev=None
    def delete_end(self):
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.prev.next=None #second last element next is removed
        temp.prev=None #last element is removed
    def delete_position(self,pos):
        temp=self.head.next
        before=self.head
        for i in range(1, pos-1): #traversing
            temp=temp.next
            before=before.next
        before.next=temp.next
        temp.next.prev=before
        temp.next=None  #deleting node at position by deleting links/null
        temp.prev=None
L=DLL()
#print('\n')
n1=Node(10)
L.head=n1
n2=Node(20)
n2.prev=n1
n1.next=n2
L.insert_beginning(30)
L.display()
L.insert_position(1,45)
L.display()
L.delete_begin()
L.display()
L.delete_end()
L.display()
L.insert_end(50)
L.insert_end(55)
L.insert_end(65)
L.insert_end(70)
L.insert_end(75)
L.display()
L.delete_end()
L.display()
L.delete_position(2)
L.display()

###############
#Graphs

'''def add_node(v):
    global node_count
    if v in nodes:
        print(v,"is already present")
    else:
        node_code=node_count+1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp=[]
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)
    def add_edge(v1,v2):
        if v1 not in nodes:
            print("it is not present in the graph")
        elif v2 not in nodes:
            print("it is not present in the graph")
        else:
            index1=nodes.index(v1)
            index2=nodes.index(v2)
            graph[index1][index2]=1
            graph[index2][index1]=1
    def print_graph():
        for i in range(node_count):
            for j in range(node_count):
                print(graph[i][j],end=" ")
            print()
    print_graph()'''
def add_newnode(v):
    if v in graphs:
        print(v, "is present already")
    else:
        graphs[v]=[]
graphs={}
add_newnode("a")
add_newnode("b")
print(graphs)
'''nodes=[]
graph=[]
node_count=0
print("\nbefore adding nodes")
print(nodes)
print(graph)
print("After adding nodes")
add_node(1)
add_node(2)
add_node(3)
add_node(4)
print(nodes)
print(graph)
'''

######Inheritance
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def __init__(self):
        super().__init__('bus', 100, 35)
        Vehicle.seating_capacity(self,50)

b1=Bus()
b1

'''
ex- 
menu=Menu([1,2,3])
menu.display()
'''
class Menu:
    def __init__(self, list1):
        self.list1=list1
        self.pos=0
        self.len_lst=len(list1)

    def to_the_right(self):
        self.pos=(self.pos+1)%self.len_lst

    def display(self):
        temp_lst=self.list1.copy()
        temp_lst[self.pos]=[temp_lst[self.pos]]
        return str(temp_lst)

menu=Menu([1,2,3])
print(menu.display())

menu.to_the_right()
print(menu.display())
menu.to_the_right()
print(menu.display())