def get_user_name():
    user = input('''
Congratulations on beginning your journey towards learning how to code!

You\'ll be happy you started this process. 

First off, what\'s your name? 
''')
    return user

def get_user_proficiency(username):
    isBeginner = input(f'''
Hey {username}! Would you say that you\'re a beginner to programming? [Type either "yes" or "no"]
''')
    if 'yes' in isBeginner.lower():
        isBeginner = True
    else:
        isBeginner = False
    return isBeginner

