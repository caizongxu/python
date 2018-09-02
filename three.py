def menu():
	print("*"*30)
	print("1:增加学生")
	print("2:查找学生")
	print("3:更新学生")
	print("4:删除学生")
	print("5:退出")
	print("6:显示学生")
	print("*"*30)
def search_student(students):
	name=input("输入查找学生姓名:")
	for student in students:
		#if name in student.values()
		if name ==student['name']:
			print("学生存在")
			print("学生的信息是:姓名为:%s,年龄为:%s,电话为:%s"%(student['name'],student['age'],student['phone']))
			break
	else:
		print("学生不存在")
	print("*"*20)
def display():
	pass
def run():
	students=[]
	while True:
		menu()
		operator=input("请选择执行的操作: ")
		if operator=="1":
			add_student(students)
		elif operator=="2":
			search_student(students)
		elif operator=="3":
			change_student(students)
		elif operator=="4":
			delete_student(students)
		elif operator=="5":
			break
def add_student(students):
	name=input("输入学生姓名:")
	age=input("请输入学生的年龄:")
	phone=input("请输入学生的电话号码:")
	student={}
	student['name']=name
	student['age']=age
	student['phone']=phone
	students.append(student)
	print("*"*20)
	print("Name\tAge\tPhone")
	for s in students:
		print("%s\t%s\t%s"%(s["name"],s["age"],s["phone"]))
def delete_student(students):
	name=input("输入学生姓名:")
	for student in students:
		if name== student['name']:
			students.remove(student)
			print("删除学生成功")
			break
	else:
		print("学生不存在")
	print("*"*20)
	print("Name\tAge\tPhone")
	for s in students:
		print("%s\t%s\t%s"%(s["name"],s["age"],s["phone"]))
def change_student(students):
	name=input("输入学生姓名:")
	for student in students:
		if name==student['name']:
			name=input("请输入修改后的姓名:")
			student['name']=name
			print("学生修改成功！")
			break
	else:
		print("学生不存在")
	print("*"*20)
	print("Name\tAge\tPhone")
	for s in students:
		print("%s\t%s\t%s"%(s["name"],s["age"],s["phone"]))


if __name__=="__main__":
	run()


