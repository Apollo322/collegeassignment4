class Student:
    def __init__(self, name, sex, phone):
        self.name = name
        self.phone = phone
        self.sex = sex
    def __str__(self):
        return '姓名：%s 性别：%s 手机号：%s' % (self.name, self.sex, self.phone)
class StudentManager:
    def __init__(self):
        self.students = []
    def add(self, student):
        self.students.append(student)
        print('添加成功')
    def remove(self, name):
        for i in self.students:
            if i.name == name:
                self.students.remove(i)
                print('删除成功')
                return
            print("未找到该学生")
    def change(self, name,sex, phone):
        for i in self.students:
            if i.name == name:
                i.sex = sex
                i.phone = phone
                print('修改成功')
                return
        print('修改失败')
    def seek(self, name):
        for i in self.students:
            if i.name == name:
                print(i)
                return
            print('未找到该学生')
test = StudentManager()
test.add(student=Student('tjw', '男', '12345678901'))
test.change('tjw', '女', '12345678902')
test.seek('tjw')
test.remove('tjw')