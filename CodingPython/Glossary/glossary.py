glossary = {
    'get': 'A function to get information from a specified resource.',
    'modules': 'A stored file which contains functions that carry out a specific task.',
    'def': 'A keyword used to create a function.',
    'loop': 'A continuous process.',
    'list': 'An array of elements usually of a specific type.'
}

print("Python glossary helper")
print("Available terms: Get, Modules, Def, Loop, List")
print("Type 'quit' or 'exit' to stop.")

while True:
    define = input("Which term would you like to know about? ")
    lower_def = define.strip().lower()

    if lower_def in ('quit', 'exit'):
        print("Goodbye!")
        break

    if lower_def in glossary:
        print(glossary[lower_def])
    else:
        print("Sorry, that term is not in this glossary. Please choose from Get, Modules, Def, Loop, or List.")

        