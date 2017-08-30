from sys import argv
script, user_name=argv
prompt= '>>>>'

print ("Hello %s, This is a Python %s script." % (user_name,script))
print ('I am very smart so I am gonna ask you three questions\n')
print ('Did you write any programming languages before, %s?' % user_name)
languages=input(prompt)

print ('How do you like using Python so far, %s?' % user_name)
feeling=input(prompt)

print ('Do you use Windows, Mac, or Linux?')
computer= input(prompt)

print ('''
Based on your input,
You said %r about your programming experience
Then you said %r about the experience so far. thanks!
And you are using a %r computer. Awesome!
''' %(languages,feeling,computer))
