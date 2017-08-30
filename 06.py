x= ('There are %d types of people' %2)
good= 'good'
are_not= "aren't"
y=('Those who are %s and those who %s' %(good, are_not))
print(x)
print(y)

print(('I said: %r.') %x)
print("I also said: '%s'." %y)

funny = True
words_feedback = "Do you agree on that?! %r"

print (words_feedback % funny)

q = 'Look at me first...'
w = 'and then look at me '

print (q+w)
