# Hi this is the first exercise to learn python. It is completely based on printing exercise and playing around with variables.

print "Hi I am a Cat" # This line just prints out whatever we have mentioned in the inverted commas.

# As you can see that anything after a "#" is ignored by python and is considered as a comment.
# Now let us see another example

print "Hi I am a # Cat" # Now in this case it does not ignore the letters after the # since the # is a part of the string itself.

#It is very much similar to giving the above string to a variable and printing the value of the variable instead. Let's take a look at it.

var = "Hi I am a # Cat"

print "The string in var says",'"' + var + '"'  # Simple, isn't it? In this statement i have used string concatenation using + symbol.

print "******************* Numbers & Maths *******************" 

# Now let us take a look at the arithematic operators and operations that python provides us.
# We will use them in the following example

print "Let me count my kittens"
print "Kittens: = ", (24+50*100/150)-50 #Output is 7.
print"Is it greater?", 7>2
# Now let us look at the problem of floating point.
print "Floating kittens: = ", 5.0+7.2 # Now it works perfectly fine.

print "******************* Playing with Variables *******************"

cats = 5
kittens = 20
print "There are",cats,"cats"
print "There are",kittens,"kittens"
# Now let us combine it all
print "There are",cats,"cats &",kittens,"kittens." #Simple, right?
#We can also use the way mentioned below as we did in C :)
print "Or the other way,"
print "There are %d cats & %d kittens" %(cats,kittens) #look at the syntax very carefully.
print"If I add cats & kittens, I would get %d."%(cats+kittens) #Oh yes you can do arithematic operations within print statements. :)

#Some more string vars examples.
hilarious=False
joke_evaluation="Isn't that joke so funny?! %r" # Use the %r for debugging, since it displays the "raw" data of the variable
print joke_evaluation%hilarious #So simple.

print"Mary had a little lamb."
print"Its fleece was white as %s."%'snow'
print"And everywhere that Mary went."
print"."*10 # what'd that do? It would print "." character 10 times.

end1="C"
end2="h"
end3="e"
end4="e"
end5="s"
end6="e"
end7="B"
end8="u"
end9="r"
end10="g"
end11="e"
end12="r"

# watch that comma at the end. try removing it to see what happens
print end1+end2+end3+end4+end5+end6,
print end7+end8+end9+end10+end11+end12

days="Mon\tTue\tWed\tThu\tFri\tSat\tSun"
months="\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" #\n is the end line character. Similarly there is \t used to tab spacing.


print"Here are the days: ",days
print"Here are the months: ",months

print"""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
# Remember there are no spaces between three """. It is a very common mistake.
