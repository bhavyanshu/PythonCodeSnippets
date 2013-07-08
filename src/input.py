# Now let us look at examples on how to ask the end user for inputs.

print "How many cats were there?",
numberofcats = int(raw_input())
print numberofcats

# Now basically what we have here is that we take user input as a string and not as a proper integer value as
# it is supposed to be. So this is a major problem because you won't be able to apply any kind of math operation on string type value.
# Now in the next example i will show you how to accept a string from user and let python convert it to an integer type value.

print "How many kittens were there?",
numberofkittens = int(raw_input())
print numberofkittens

# What's the difference between input() and raw_input()?
# The input() function will try to convert things you enter as if they were Python code, but it has security problems so you should avoid it.

#There is an easier way to write the above input prompter in single line. Let's take a look"

numberofDogs= int(raw_input("Total number of Dogs?")) #Easy, isn't it?
print numberofDogs

print "*********************Let us now print the input data******************"
print "*Number of cats are %d, number of kittens are %d & number of dogs are %d"%(numberofcats,numberofkittens,numberofDogs)+"*"
print "**********************************************************************"