#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# name =input('please input your name:')
# print("hello,",name)
# print("\\")
# print('''line1
# line2
# line3''')

# n = 123
# f = 456.789
# s1 = 'hello,world'
# s2 = 'hello,\'adam\''
# s3 = r'Hello,"Bart"'
# s4 = r'''hello,
# Lisa!'''
# print(n,f,s1,s2,s3,s4)
# print('ABC'.encode('ascii'))
# print(b'ABC'.decode('ascii'))

# print("hello,%s" % 'world')


#算算小明成绩提升的绩点
# g1 = 72
# g2 = 87
# r = (g2 - g1)/g1 * 100
# print('小明成绩提升了%.2f%%' % r)



#List
# classmates = ["xiaoming","zhanghua","lihong"]
# print(classmates)
# print(len(classmates))
# classmates.insert(1,"wangming")
# print(classmates)
# classmates.pop()
# classmates.pop()
# print(classmates)

# print('''''')

# p = ["chinese","math"]
# L = ["jack","male",p,15]
# print(L)
# print(L[2][1])

# L.append("rose")
# print(L)






#Tuple

# classmates = ("rose","jack","martin","love")
# print(classmates)
# print(classmates[2])
# #classmates[0] = "nick"
# print(classmates)

# test = (1,classmates)
# print(test)


# L = [
    # ['Apple', 'Google', 'Microsoft'],
    # ['Java', 'Python', 'Ruby', 'PHP'],
    # ['Adam', 'Bart', 'Lisa']
# ]

# print(L[0][0])
# print(L[1][1])
# print(L[2][2])



#条件判断
# grade = input("your grade:")
# grade = int(grade)
# if grade >= 90:
	# print('A')
# elif grade >= 80:
	# print('B')
# elif grade >= 70:
	# print('C')
# else:
	# print('D')



#循环语句

# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
	# print(name)

# s = 0
# for n in range(101):
	# s = s + n
# print(s)

# L = ['Bart','Lisa','Adam']
# for name in L:
	# print('hello,%s!' % name)
	
	
# n = 10
# while n > 0:
	# print(n)
	# n = n - 1
	
	
	
	
#使用dict和set

d = {
	'Michael':99,
	'Bob':20,
	'Lucy':79
}

print('\'Michael\' = ' , d['Michael'])
print('\'Bob\' = ' , d['Bob'])
print('\'Lucy\' = ' , d['Lucy'])



s1 = set([1,2,3])
print(s1)
s2 = set([2,3,4,5])
print(s1 & s2)
print(s1 | s2)
















input()