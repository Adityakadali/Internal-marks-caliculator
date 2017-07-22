from appJar import gui

app = gui('Internal marks caliculator')
app.setBg('#8b9dc3')
app.addLabel('lb1','Enter your marks')
app.addLabelNumericEntry('class test 1')
app.addLabelNumericEntry('class test 2')
app.addLabelNumericEntry('class test 3')
app.addLabelNumericEntry('class test 4')
app.addLabelNumericEntry('mid 1')
app.addLabelNumericEntry('mid 2')


def total(button):
	class_test_1 = app.getEntry('class test 1')
	class_test_2 = app.getEntry('class test 2')
	class_test_3 = app.getEntry('class test 3')
	class_test_4 = app.getEntry('class test 4')
	mid_marks_1 = app.getEntry('mid 1')
	mid_marks_2 = app.getEntry('mid 2')
	class_test_marks = [class_test_1, class_test_2, class_test_3, class_test_4] # list of class test marks
	mid_marks = [mid_marks_1, mid_marks_2] # list of mid marks
	new_class_test_marks = sorted(class_test_marks) # sort of class test marks
	updated_class_test_marks = new_class_test_marks[1:] #taking highest 3 marks
	new_mid_marks = sorted(mid_marks)   #sort mid marks
	#print(new_class_test_marks)
	#print(new_mid_marks)
	class_test = (((updated_class_test_marks[0] + updated_class_test_marks[1] + updated_class_test_marks[2])/3) * 2)
	mid = (new_mid_marks[0]*0.25 + new_mid_marks[1]*0.75)/2.0
	tot = class_test + mid
	app.addStatusbar()
	app.setStatusbar(tot)
	#mif = (((new_mid_marks[0] * 0.25 ) + (new_mid_marks[1] * 0.75)) / 2)
	#total = class_test + mif
	#print(' hey dude you got ' + str(total) +' marks')

app.addButton('caliculate',total)
app.setResizable(False)

app.go()