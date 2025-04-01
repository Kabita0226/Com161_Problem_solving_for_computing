#dictionary
Student = {"Aliza":"21","Amit":"22","Ujan":"26","Ajay":"21","amy":"20"}
print(Student)
Student["Kabita"] = "19"
print(Student)
Student_set={"Aliza","Amit","Ujan","Ajay","Kabita"}
print(Student_set)
print('Aliza'in (Student))

if "Aliza" in (Student):
    print(Student["Amit"])
Student.update({"Ajay":"22"})
Student.pop("amy")
Student.popitem()
print(Student)
del Student['Ujan']

