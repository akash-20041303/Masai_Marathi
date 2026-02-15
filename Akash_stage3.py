name = input("Enter Student Name: ")
sub1 = int(input("Enter 1st Sub Marks: "))
sub2 = int(input("Enter 2nd Sub Marks: "))
sub3 = int(input("Enter 3rd Sub Marks: "))
total = sub1+sub2+sub3
per = total / 3
print("Total Marks is: ",total)

print("Average is: ",per)
if per >= 80:
    print("A Grade")
elif per >=60:
    print("B Grade")
elif per >= 50:
    print("C Grade")
elif per >= 35:
    print("Pass")
else:
    print("Failed")

