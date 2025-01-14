def sayHello():
    print("hello")
sayHello()
"""
Scope explanation :
Types of Scopes: Global Scope and local scope
"""
sco = 10 # Global Variable can be used inside as well as outside the function as well
def sayHello():
    scoinside = 20 #local variable can't be used outside the function bcs of local scope
    print(sco) #using global variable sco


sayHello()
print(sco)
""" 
Tricky Question
"""
scop = 10
def sayHello():
    global scop #MAKING a local variable  which is inside the function only to global outside the function available  by using global keywoard 
    scop = 20
    sayHello()
    print(scop)
li = [1,2,3,"Hello"]
li2 = ["hello","name","is","sanket",99.4]
print(li)
print(li2)
#index
li2[4]
#change element
li[0]=22.4
print(li)
#slicing
#li[start:stop]
li[1:3]
print(li[1:3])
li.append(5)
print(li)
li.append("hi")
print(li)
li.insert(0,"sachdeva")
print(li)
li2.insert(3,"sam")
print(li2)
li2.extend((10,11,12,13))
print(li2)
li2.remove(10)
print(li2)
li2.pop()
print(li2)
li2.pop(1)
print(li2)
print(len(li2))
li2.reverse()
print(li2)
li2.sort()
print(li2)