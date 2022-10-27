def teacher():
    print('working')
teacher()


#argoment

def teacher(id,name,designation,salary=25000):
    return id,name,designation,salary

# t1 = teacher(555,'rokon','rokon',50000) 
print(teacher(555,'rokon','rokon',50000)) 
print(teacher(556,'rokon','rokon',50000)) 
print(teacher(555,'rokon','rokon',50000))
print(teacher(558,'rokon','rokon',))  
