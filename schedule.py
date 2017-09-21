'''
David Myers

Command line class scheduling program


'''
#create class schedule
classSchedule = ["CITPT 106", "CITPT 117", "CITPT 213", "CITPT 227"]

print "Your Class Schedule:"
		
for item in classSchedule:
	print item


#function to add class
def addClass():
	global classSchedule
	new_class = raw_input("What class do you want to add:  ")
	new_class = new_class.upper()
	classSchedule.append(new_class)

#function to delete class
def delete_class():
	global classSchedule
	remove_class = raw_input("What class do you want to remove:  ")
	remove_class = remove_class.upper()
	
	if remove_class in classSchedule:
		classSchedule.remove(remove_class)
	else:
		print "bad input"



#main program
def main():
	while True:

		print "---------------------"
		print "What do you want to do:  Add, Delete, or View classes.  Type quit to quit.:  "
		user_choice = raw_input("")
		#format user choice
		user_choice = user_choice.strip()
		user_choice = user_choice.lower()
		
		if user_choice == "add":
			addClass()
			continue
			
		elif user_choice == "delete":
			delete_class()
			continue
			
		elif user_choice == "view":
			print "Your Class Schedule:"
			for item in classSchedule:
				print item
				continue
		
		elif user_choice == "quit":
			break
		
		else:
			print "bad input"
			continue
main()
		