while True:
    print("Welcome to Wscube Tech - E school: ")
    uc = int(input('''
                   1. Student’s Admission
                   2. Student’s Fee
                   3. Principal Access
                   4. Exit: ____
                   '''))
    if uc==1:
                       print("** Welcome to Student Admission **")
                       st_name=input("Student's name: ")
                       st_father_name=input("Student's father name: ")
                       st_mother_name=input("Student's mother name: ")
                       st_phone_no=input("Phone No.: ")
                       st_add=input("Address.: ")
                       st_card_no=int(input("Enter Card No: "))
                       st_class=int(input("Class: "))
                       print("Successfully Admission")
    elif uc==2:
                           print("** Student Fee **")
                           st_name1=input("Student's name: ")
                           st_card_no1=int(input("Enter Card No.: "))
                           if st_name==st_name1 and st_card_no==st_card_no1:
                               print(st_name)
                               print(st_card_no1)
                               f=int(input("Enter fee Amount: "))
                               print(f)
                               print("Successfully Fee Submitted")
                               
    elif uc==3:
                                   p=int(input("Enter principal access no.: "))
                                   print("** Principal Access **")
                                   p1=int(input("Enter principal access no.: "))
                                   st_card_no2=int(input("Enter Card No.: "))
                                   if p==p1 and st_card_no==st_card_no2:
                                       print(st_name)
                                       print(st_father_name)
                                       print(st_mother_name)
                                       print(st_phone_no)
                                       print(st_add)
                                       print(st_card_no)
                                       print(st_class)
    else:
                                 break
        