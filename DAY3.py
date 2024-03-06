#data conversion (type casting)
a=int(5.7)
print(a,type(a))

#TAKING USER INPUT

#1 STRING
a=input("enter your name:")
print("my name is",a)

#1.1

r=int(input("enter the radius of the circle:"))
area=3.14*r*r
print("Area of the circle with radius",r,"is",area)

#2 INTEGER
x=int(input("enter first no.:"))
y=int(input("enter second no.:"))
print(x+y)

#MORE ABOUT STRINGS
name="riya"
myfriend="nithya"
print(name,"and",myfriend,"are friends forever")

#multiline string

about='''hey, I'am riya
I am 20 year old,
I am studying data science from IITM
'''
#indexing

print(name[0])
print(name[1])
print(name[2])
print(name[3])