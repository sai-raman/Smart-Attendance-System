import qrcode
import csv



students = []
with open('students.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        students.append((row[0]))

for student in students:
    img = qrcode.make(student)
    img.save('./images/'+student+'.jpg')
 