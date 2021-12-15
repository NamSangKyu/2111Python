"""
    http://gofile.me/4KZc6/WcpkR0zio
    학생정보.csv 파일을 받은 후
    해당을 읽어와서 출력  ---> wt
"""
student_list = []
with open('학생정보.csv','rt') as file:
    while True:
        line = file.readline()
        if not line:
            break
        line = line.replace('\n','')
        student = line.split(",")
        for i in range(len(student)):
            #student[i] =student[i].replace('"','')
            student[i] = student[i].strip('"')
        student_list.append(student)
print(student_list)
