'''

This is script used to caliculate internal marks
written by
Aditya Kadali
can be used without my permission

'''
class_test_marks = [] #marks of class tests
mid_marks = [] #mid marks


class_test_1 = float(input('Enter class test 1 marks '))
class_test_2 = float(input('Enter class test 2 marks '))
class_test_3 = float(input('Enter class test 3 marks '))
class_test_4 = float(input('Enter class test 4 marks '))

mid_test_1 = float(input('Enter mid 1 marks '))
mid_test_2 = float(input('Enter mid 2 marks '))

''' Taking classtest marks into list
and Mid marks in to list'''
class_test_marks.append(class_test_1)
class_test_marks.append(class_test_2)
class_test_marks.append(class_test_3)
class_test_marks.append(class_test_4)

mid_marks.append(mid_test_1)
mid_marks.append(mid_test_2)


new_class_test_marks = sorted(class_test_marks) # sort of class test marks
updated_class_test_marks = new_class_test_marks[1:] #taking highest 3 marks

new_mid_marks = sorted(mid_marks)   #sort mid marks





def total():
    class_test = ((updated_class_test_marks[0] + updated_class_test_marks[1] + updated_class_test_marks[2])/3) * 2
    mids = ((new_mid_marks[0] * 0.25 ) + (new_mid_marks[1] * 0.75)) / 2
    total = class_test + mids
    print(' hey dude you got ' + str(total) +' marks')
total()
