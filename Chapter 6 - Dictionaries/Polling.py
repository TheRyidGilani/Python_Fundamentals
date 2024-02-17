favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

people = ['jen', 'sarah', 'edward', 'phil', 'mike', 'alice', 'bob']

for names in people:
    if names in favorite_languages:
        print(names.title() + ", Thank you for taking the poll!")
    else:
        print(names.title() + ", Please take the poll!")