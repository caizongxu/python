class Student():
	def __init__(self,name,age,phone):
		self.name=name
		self.age=age
		self.phone=phone
	def display(self):
		print("%s\t%d\t%s"%(self.name,self.age,self.phone))

class StudentManager():
	__students=[]
	@staticmethod
	def menu():
		print("====学生管理系统===")
		print("*"*30)
		print("1:增加学生")
		print("2:查找学生")
		print("3:更新学生")
		print("4:删除学生")
		print("5:退出")
		print("6:显示学生")
		print("*"*30)
	@classmethod
	def add_student(cls):
		name=input("请输入学生的姓名")
		age=int(input("请输入学生的年龄"))
		phone=input("请输入学生的电话")
		student=Student(name,age,phone)
		cls.__students.append(student)
	@classmethod
	def find_student(cls):
		name=input("输入查找学生姓名:")
		for student in cls.__students:
			#if name in student.values()
			if name ==student.name:
				print("学生存在")
				break
		else:
			print("学生不存在")
	@classmethod
	def update_student(cls):
		name=input("输入学生姓名:")
		for student in cls.__students: 
			if name==student.name:
				name=input("请输入修改后的姓名:")
				student.name=name
				print("学生修改成功！")
				break
		else:
			print("学生不存在")
	@classmethod
	def delete_student(cls):
		name=input("输入学生姓名:")
		for student in cls.__students:
			if name== student.name:
				cls.__students.remove(student)
				print("删除学生成功")
				break
		else:
			print("学生不存在")
	@classmethod
	def display_student(cls):
		print("*"*20)
		print("Name\tAge\tPhone")
		for student in cls.__students:
			student.display()
	@staticmethod
	def run():
		while True:
			StudentManager.menu()
			operator=input("请选择执行的操作: ")
			if operator=="1":
				StudentManager.add_student()
				StudentManager.display_student()
			elif operator=="2":
				StudentManager.find_student()
				StudentManager.display_student()
			elif operator=="3":
				StudentManager.update_student()
				StudentManager.display_student()
			elif operator=="4":
				StudentManager.delete_student()
				StudentManager.display_student()
			elif operator=="5":
				break			
			elif operator=="6":
				StudentManager.display_student()
if __name__=="__main__":
	studentmanager=StudentManager()
	studentmanager.run()
