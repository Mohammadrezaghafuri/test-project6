n = int(input("number of student :"))

users = []

for e in range(n):
    student = input('name:')
    age =input('age:')
    users.append({'name':student , 'age': age})    

serch_name = input("name for serch:")

for e in users:
    el = len(users)-1
   
    if e['name'] == serch_name:
        print(e['age'])
        break
    elif e['name'] != serch_name:
          if e == el:
              print("there is no user with given name")
          else:
             continue
      

     
