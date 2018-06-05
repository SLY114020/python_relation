
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'huang'

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print('Hello world')
	elif len(args) == 2:
		print('hell, %s' % (args[1]))
	else:
		print('Too many argument')
		
class Student(object):

	cname = 'Student'
	
	__slots__ = ('name', 'score', '__gender')
	
	def __init__(self, name, gender, score):
		self.name = name
		self.score = score
		self.__gender = gender
	
	def print_info(self):
		print("%s : %s", self.name, self.score)
		
	def get_gender(self):
		return self.__gender
	
	def set_gender(self, new_gender):
		if new_gender != 'male' or new_gender != 'female':
			self.__gender = new_gender
		else:
			raise ValueError('bad new_gender')
	
	@property
	def sscore(self):
		return self.score
		
	@sscore.setter
	def sscore(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self.score = value
		
bart = Student('Bart', 'male', 100)
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功1!')
		
bart.sscore = 10
print(bart.sscore)
print(Student.cname)





if __name__ == '__main__':
	test()
	
	


