#!/usr/bin/env python 
'''
The line above is often called shebang line. This is important if you want to invoke python script directly. Also in unix/mac systems, this line plays an important role. Not in windows though.
If you have several versions of Python installed, /usr/bin/env will ensure the interpreter used is the first one on your environment's $PATH.
'''

'''
Sorting Algorithms applied in python
------------------------------------
In this i am going to show you sorting algorithms ported to python. If you have done them in c/c++/java then you must be aware of these basic sorting algos.
The first step is to create a menu with options like selection sort, bubble sort, insertion sort, merge sort etc.
The second step would be to take user input as an option and the control would pass to that particular chosen sort based on the input & call the appropriate sorting function.
Before calling we should request some array input from the user which he/she would like to sort and pass them as arguments to the sorting function during function call.
'''


'''
First Step: Since python does not have switch statement (Yeah! sucks, i know!). It was proposed and rejected in PEP 3103. I don't know why it didn't have it initially. Basicallly some people believe that having switch statement is just bad design and we should always try to replace switch cases. 
Why bad design? Because having switch statements lead to duplicacy of code. It is often known as "SwitchSmell". Typically, similar switch statements are scattered throughout a program. If you add or remove a clause in one switch, you often have to find and repair the others too. 
The replacement can usuallly be done using polymorphism concepts.

The following is a direct quote from RefactoringImprovingTheDesignOfExistingCode(http://c2.com/cgi/wiki?RefactoringImprovingTheDesignOfExistingCode), page 256.
Polymorphism gives you many advantages. The biggest gain occurs when the same set of conditions appears in many places in the program. If you want to add a new type, you have to find and update all of the conditionals. But with subclasses, you just create a new subclass and provide the appropriate methods. Clients of the class don't need to know about the subclasses, which reduces the dependencies in your system and makes it easier to update.

Anyway, in python either we can implement polymorphism or we can use associative arrays also known as dictionaries. These provide one-to-one matching of a key-value pair. In this particular example we will be using dictionaries instead of polymorphism. Then we will port this code to use the concept of polymorphism. That's it for the theory of python. Let's begin some coding.
'''

#function 1 is for bubble sort
def bubblesort(): 
	'''Basic idea behind bubble sort : easy to implement but cannot be used for large or medium sized datasets. Now we will apply it on a small array of integers
Theory: The bubble sort works by passing sequentially over a list, comparing each value to the one immediately after it. If the first value is greater than the second, their positions are switched. Over a number of passes, at most equal to the number of elements in the list, all of the values drift into their correct positions (large values "bubble" rapidly toward the end, pushing others down around them). Because each pass finds the maximum item and puts it at the end, the portion of the list to be sorted can be reduced at each pass. A boolean variable is used to track whether any changes have been made in the current pass; when a pass completes without changing anything, the algorithm exits. 
'''
	print "You selected bubble sort. \n"
	newarr=createarr() #Calling function createarr() to build an array & pass the value to a local array.
	print "Before sorting the array is ", newarr
	done = 0 #Here done is the boolean variable
	while (done!=1): #while for checking if finished or not
		done=1 #set boolean to 1 if finished
		for i in range(1,len(newarr)):  #loop through the array
			if(newarr[i-1]>newarr[i]): #check if previous is greater than the next item in array
				done = 0 #set done to 0 to keep going on.
				tmp = newarr[i-1] #Perform swap between them
				newarr[i-1]=newarr[i]
				newarr[i]=tmp
	print "After sorting the array is ", newarr #once done = 1, generate the final array.
####################################################################################	



#function 2 is for selection sort
def selectionsort():
	'''
	In this we first find the smallest element in the array and exchange it with the element in the first position. In simple terms we shift the smallest element to first positions, then find the second smallest element and exchange with the element on the second position and so on. 
	This is also inefficient for large arrays.
	Application: Its primary purpose is for when writing data is very expensive (slow) when compared to reading, eg writing to flash memory or EEPROM. No other sorting algorithm has less data movement. 
	'''
	print "You selected selection sort. \n"
	newarr=createarr()
	print "Before sorting the array is", newarr
	for i in range(0,len(newarr)-1): #looping through array
		m=i #setting position for min value
		for j in range(i+1,len(newarr)): #to move through loop leaving the min value
			if(newarr[j]<newarr[m]): #checking if next element is less than min value, #if it is min then
				m=j #switching position
		temp = newarr[i] #Now swapping
		newarr[i]=newarr[m]
		newarr[m]=temp
	print "After sorting the array is", newarr
	

####################################################################################



#function 3 is for merge sort
def mergesort():
	'''The basic idea is to split the collection into smaller groups by halving it until the groups only have one element or no elements (which are both entirely sorted groups). Then merge the groups back together so that their elements are in order. This is how the algorithm gets its "divide and conquer" description.'''
	print "You selected merge sort. \n"
	newarr=createarr()
	print "Before sorting the array is", newarr
	print "After sorting the array is", divide(newarr) #Calling divide() function and passing the array as argument

def divide(arrToDivide):
	if (len(arrToDivide))<=1:
		return arrToDivide #check if there is just a single element in the array.
	
	middle = len(arrToDivide)/2 #Divide given array in two parts left and right
	left = arrToDivide[:middle] #Left partition of array. You should read more on lists in python and how do we access list elements
	right = arrToDivide[middle:] #Right partition of array

	left = divide(left) #Recursive call for further partitioning.
	right = divide(right)
	return merge(left,right) #Calling merge() function which generates the output for divide() function which is returned to margesort() as final sorted array

def merge(left,right):
	result = [] #Creating new array named result
	leftID=0 #Initializing left index variable
	rightID=0 #Initializing right index variable
	while leftID<len(left) and rightID<len(right): #change sequence to change sorting sequence
		if left[leftID]<=right[rightID]: #ex, if first of left <= first of right
			result.append(left[leftID]) #then append left to result
			leftID+=1
		else:	
			result.append(right[rightID]) #else append right to result
			rightID+=1
	if left:		#merge sorted halfs back to single array result
		result.extend(left[leftID:])
	if right:
		result.extend(right[rightID:])
	return result
####################################################################################

#function 4 is for quick sort
def quicksort():  
	'''
    1.Choose any element of the array to be the pivot.
    2.Divide all other elements (except the pivot) into two partitions.
        All elements less than the pivot must be in the first partition.
        All elements greater than the pivot must be in the second partition. 
    3.Use recursion to sort both partitions.
    4.Join the first sorted partition, the pivot, and the second sorted partition. '''
	print "You selected quick sort. \n"
	newarr=createarr()
	print "Before sorting the array is", newarr
	print "After sorting the array is", sort(newarr) #Output of sort() function

def sort(newarr): #This is where quick sort actually occurs
	less = [] #List of elements less than pivot value
	greater = [] #List of elements greater than pivot value
	pivotequal = [] #List of elements equal to pivot value
	if len(newarr)<=1:
		return newarr #if there is single element in list
	else:
		pivot = newarr[0] #Initializing pivot to first element (default)
		for i in newarr:
			if i<pivot:	#If element is less than pivot
				less.append(i) #then append to less list
			elif i>pivot: #If element is greater than pivot
				greater.append(i) #then append to greater list
			else:	#if equal to pivot
				pivotequal.append(i)#then append to pivotequal list
		less = sort(less) #Recursive call to sort both new partitions
		greater = sort(greater)
		return less+pivotequal+greater #Join left, middle & right to output

####################################################################################

#function 5 is for insertion sort
def insertionsort():  
	'''It involves moving one element at a time into the previous sorted part of the array. Its simplicity, low overhead, good locality of reference and efficiency make it a good choice in two cases (i) small n (where n is the total number of elements in the list), (ii) as the final finishing-off algorithm for O(n logn) algorithms such as mergesort and quicksort. '''
	print "You selected insertion sort. \n"
	newarr=createarr()
	print "Before sorting the array is", newarr
	print "After sorting the array is", insertion(newarr)

def insertion(iarr):
	for i in range(1,len(iarr)): #Looping through elements in list
		value = iarr[i] #initializing key element
		j=i-1 #index of element previous to key element
		while (j>=0) and (iarr[j]>value): #checking if j is greater than 0 and value of element previous to key element is greater
			iarr[j+1] = iarr[j] #Shifting ahead
			j=j-1 #Moving back
		iarr[j+1] = value #Changing value of key element to next element
	return iarr
####################################################################################

#Acts as default function for invalid user input.
def errorMessage():
    print "Incorrect input. Please enter a number between 1 and 5."

#Function used to build array from user input.
def createarr():
	arr = [] #Declaring an array
	elem = int(raw_input("How many elements you want?\t "))  #creating a size limit for array.
	for i in range(0, elem):
    		arr.append(int(raw_input("Enter number "+str(i+1)+":" ))) #Accepting array elements & appending to the array. This is not complicated. Look carefully. We are just concatenating & i+1 is because the array starts from 0. To make it more user friendly, we must start from 1.
	return arr #Printing the array values.


#Main function that is called as soon as the program executes. 
def main():
	print  '''Help Menu : 
			1. Bubble Sort, 
			2. Selection Sort, 
			3. Merge Sort, 
			4. Quick Sort,
			5. Insertion Sort'''
	num=raw_input("Which sorting algo would you like to run?");
	options = {'1' : bubblesort, 
           '2' : selectionsort,
           '3' : mergesort,
           '4' : quicksort,
           '5' : insertionsort,
	} #Declaring a dictionary
	options.get(num, errorMessage)()
	

if __name__ == '__main__':
	main() #Called as soon as the program runs.
