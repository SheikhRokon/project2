class person:
    def info(self,name,add,email,phone):
        return name,add,email,phone

obj = person()  
print(obj.info('Rokon','Dhaka','rokon@gmail.com','0187952846'))    

class student(person):
    def sinfo(self,depat,roll):
        return depat,roll

s_obj = student()
print(s_obj.info('Rael','Barguna','rokon@gmail.com','0187952846'))
print(s_obj.sinfo('CMT',918888))

############### Techer ##############

class techer(student):
    def info(self):
        return 

T_obj = techer()
print(T_obj.info('Rael','Barguna','rokon@gmail.com','0187952846', 2000, 5544))

