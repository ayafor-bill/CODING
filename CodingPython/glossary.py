dict = {}

dict['get'] = 'A function to get information from a speciied resouce.'
dict['modules'] = 'A stored file which contains functions that carry out a specific task.'
dict['def'] = 'A keyword used to create a function.'
dict['loop'] = 'A continuous process'
dict['list'] = 'An array of elements usually of a specific type'

define = input("Get, Modules, Def, Loop, and List - which one would you like to know about: ")
lower_def = define.lower()

if lower_def == 'get':
    print(dict['get'])
elif lower_def == 'modules':
    print(dict['modules'])
elif lower_def == 'def':
    print(dict['def'])
elif lower_def == 'loop':
    print(dict['loop'])
elif lower_def == 'list':
    print(dict['list'])
        