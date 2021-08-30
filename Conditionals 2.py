mark = int(input("Enter Your Mark: "))

# if mark >= 0 and mark < 50:
#     print('out of range')
if mark >= 51 and mark < 61:
    print('fail')
elif mark >= 61 and mark < 71:
    print("Acceptable")
elif mark >= 71 and mark < 81:
    print("Good")
elif mark >= 81 and mark < 91:
    print("Very Good")
elif mark >= 91 and mark <= 100:
    print("Excellent")
else:
    print("Fail")
