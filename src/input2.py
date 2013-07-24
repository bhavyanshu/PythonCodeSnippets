# This exercise is basically for prompting user for input. We saw in previous exercise that how to take input 
# by a little lengthy method but now we will take a look at some other methods which are comparatively easier to use.

cats=raw_input("How many cats do you have?")
kittens=raw_input("How many kittens are there?")
dogs=raw_input("What about dogs?")

print"So, you have %rcats, %rkittens and %rdogs."%(cats,kittens,dogs)