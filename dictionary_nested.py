student_data={
    'jay':{'details':{'roll':101,'marks':[92,89,90,95,78]}},
    'viru':{'details':{'roll':102,'marks':[61,81,91,98,79]}},
    'basanti':{'details':{'roll':103,'marks':[82,93,78,98,69]}},
    'kumar':{'details':{'roll':104,'marks':[81,95,76,98,80]}}

}
for std  in student_data:
    per=sum(student_data[std]['details']['marks'])/5
    print(f"{std} has got {per}%")
