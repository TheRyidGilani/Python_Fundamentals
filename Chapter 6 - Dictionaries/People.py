People = {
    'Friend_1': {
        'First Name': 'Samem',
        'Last Name': 'Zamani',
        'Age': '23',
        'Location': 'Swansi'
    },
    'Friend_2': {
        'First Name': 'Nihal',
        'Last Name': 'Kehal',
        'Age': '23',
        'Location': 'Humberwood'
    },
    'Friend_3': {
        'First Name': 'Yousuf',
        'Last Name': 'Nadir',
        'Age': '21',
        'Location': 'Plano'
    }
}

for friend,friend_info in People.items():
    fullname = friend_info['First Name'] + " " + friend_info['Last Name']
    location = friend_info['Location']
    age = friend_info['Age']

    print("\n" + friend + "'s name is: " + fullname + "\nFrom: " + location)
    print("They are: " + friend_info['Age'] + " years old")