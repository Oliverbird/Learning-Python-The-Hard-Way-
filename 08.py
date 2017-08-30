formatter='%s %s %s %s'
print (formatter % (1,1,1,1))
print (formatter %  ('one','one','one','one'))
print (formatter %  (False,True,False,True))
print (formatter %  (formatter,formatter,formatter,formatter,))
print (formatter %  (
    'Hey, how are you.',
    'Good, how about you.',
    "I'm good.",
    "Alright,talk to you soon."
                    )
       )
