current_users = ['Admin','Ryid','Sam','Azzy','Nihal']
current_users_lower = [user.lower() for user in current_users]
new_users = ['Hans','Ryid','Sam','Kim','Marshall','RYID']


for name in new_users:
    if name.lower() in current_users_lower:
        print("Sorry, the username " + name + " is already taken.")
    else:
        print("Username available.")
