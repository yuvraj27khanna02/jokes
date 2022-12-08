import pandas as pd
from datetime import datetime
from random import *
import random
joke_app_USERS_csv_reader = pd.read_csv("joke_app_USERS.csv")
USERS_user_username = joke_app_USERS_csv_reader['username'].values.tolist()
USERS_user_password = joke_app_USERS_csv_reader['password'].values.tolist()
USERS_user_name = joke_app_USERS_csv_reader['Name'].values.tolist()

joke_app_USERS_LOGIN_csv_reader = pd.read_csv("joke_app_USER_LOGIN.csv")
USERSLOGIN_TIMESTAMP = joke_app_USERS_LOGIN_csv_reader['TIMESTAMP'].values.tolist()
USERLOGIN_userlogin_id = joke_app_USERS_LOGIN_csv_reader['user login ID'].values.tolist()
USERSLOGIN_user_username = joke_app_USERS_LOGIN_csv_reader['username'].values.tolist()
USERSLOGIN_userlogin_count = joke_app_USERS_LOGIN_csv_reader['user login count'].values.tolist()

joke_app_JOKE_csv_reader = pd.read_csv("joke_app_JOKE.csv")
JOKE_TIMESTAMP = joke_app_JOKE_csv_reader['TIMESTAMP'].values.tolist()
JOKE_joke_id = joke_app_JOKE_csv_reader['joke ID'].values.tolist()
JOKE_joke_content = joke_app_JOKE_csv_reader['joke Content'].values.tolist()
JOKE_user_username_creator = joke_app_JOKE_csv_reader['Creator username'].values.tolist()

joke_app_REACTION_csv_reader = pd.read_csv("joke_app_REACTION.csv")
REACTION_TIMESTAMP = joke_app_REACTION_csv_reader['TIMESTAMP'].values.tolist()
REACTION_reaction_id = joke_app_REACTION_csv_reader['reaction ID'].values.tolist()
REACTION_user_username = joke_app_REACTION_csv_reader['reaction username'].values.tolist()
REACTION_joketags_tags = joke_app_REACTION_csv_reader['joke tags'].values.tolist()
REACTION_reaction_like = joke_app_REACTION_csv_reader['like'].values.tolist()
REACTION_reaction_dislike = joke_app_REACTION_csv_reader['dislike'].values.tolist()
REACTION_reaction_comment = joke_app_REACTION_csv_reader['comment'].values.tolist()
REACTION_reaction_rate = joke_app_REACTION_csv_reader['rate (0 to 10)'].values.tolist()

joke_app_USER_ACTIVITY_csv_reader = pd.read_csv("joke_app_USER_ACTIVITY.csv")
USERACTIVITY_TIMESTAMP = joke_app_USER_ACTIVITY_csv_reader['TIMESTAMP'].values.tolist()
USERACTIVITY_useractivity_id = joke_app_USER_ACTIVITY_csv_reader['useractivity ID'].values.tolist()
USERACTIVITY_useractivity_activity = joke_app_USER_ACTIVITY_csv_reader['useractivity activity'].values.tolist()
USERACTIVITY_user_username = joke_app_USER_ACTIVITY_csv_reader['user'].values.tolist()

joke_app_JOKE_TAGS_csv_reader = pd.read_csv("joke_app_JOKE_TAGS.csv")
JOKETAGS_TIMESTAMP = joke_app_JOKE_TAGS_csv_reader['TIMESTAMP'].values.tolist()
JOKETAGS_joke_id = joke_app_JOKE_TAGS_csv_reader['joke ID'].values.tolist()
JOKETAGS_joketags_tag = joke_app_JOKE_TAGS_csv_reader['joke tags'].values.tolist()
name_user = str
username_user = str
a = str
b = str
c = str
qwerty = []
q = '****************'

hw = True
h = True

hw_authentication = True
hw_login = True
hw_signup = True
hw_signup_password = True
hw_signup_name = True
hw_app = True
hw_main_menu = True
hw_joke = True
hw_add_joke = True
hw_view_joke = True
hw_reaction = True
hw_reaction_rate = True
hw_add_joke_JOKE_joke_id = True
hw_add_joke_JOKE_joke_content = True
hw_add_joke_JOKE_joke_content_confirmation = True
hw_add_joke_JOKE_user_username_creator = True
hw_add_joke_JOKETAGS_joketags_tags = True
hw_add_joke_JOKETAGS_joketags_tags_confiration = True
hw_add_joke_JOKETAGS_joketags_tags_again = True
def initialize_for_JOKES_app():
    USERS_user_username = []
    USERS_user_password = []
    USERS_user_name = []
    USERSLOGIN_TIMESTAMP = []
    USERLOGIN_userlogin_id = []
    USERSLOGIN_user_username = []
    USERSLOGIN_userlogin_count = []
    JOKE_TIMESTAMP = []
    JOKE_joke_id = []
    JOKE_joke_content = []
    JOKE_user_username_creator = []
    REACTION_TIMESTAMP = []
    REACTION_reaction_id = []
    REACTION_user_username = []
    REACTION_joketags_tags = []
    REACTION_reaction_like = []
    REACTION_reaction_dislike = []
    REACTION_reaction_comment = []
    REACTION_reaction_rate = []
    USERACTIVITY_TIMESTAMP = []
    USERACTIVITY_useractivity_id = []
    USERACTIVITY_useractivity_activity = []
    USERACTIVITY_user_username = []
    JOKETAGS_TIMESTAMP = []
    JOKETAGS_joke_id = []
    JOKETAGS_joketags_tag = []
    
    joke_app_USERS_csv_reader = pd.read_csv("joke_app_USERS.csv")
    USERS_user_username = joke_app_USERS_csv_reader['username'].values.tolist()
    USERS_user_password = joke_app_USERS_csv_reader['password'].values.tolist()
    USERS_user_name = joke_app_USERS_csv_reader['Name'].values.tolist()

    joke_app_USERS_LOGIN_csv_reader = pd.read_csv("joke_app_USER_LOGIN.csv")
    USERSLOGIN_TIMESTAMP = joke_app_USERS_LOGIN_csv_reader['TIMESTAMP'].values.tolist()
    USERLOGIN_userlogin_id = joke_app_USERS_LOGIN_csv_reader['user login ID'].values.tolist()
    USERSLOGIN_user_username = joke_app_USERS_LOGIN_csv_reader['username'].values.tolist()
    USERSLOGIN_userlogin_count = joke_app_USERS_LOGIN_csv_reader['user login count'].values.tolist()

    joke_app_JOKE_csv_reader = pd.read_csv("joke_app_JOKE.csv")
    JOKE_TIMESTAMP = joke_app_JOKE_csv_reader['TIMESTAMP'].values.tolist()
    JOKE_joke_id = joke_app_JOKE_csv_reader['joke ID'].values.tolist()
    JOKE_joke_content = joke_app_JOKE_csv_reader['joke Content'].values.tolist()
    JOKE_user_username_creator = joke_app_JOKE_csv_reader['Creator username'].values.tolist()
    
    joke_app_REACTION_csv_reader = pd.read_csv("joke_app_REACTION.csv")
    REACTION_TIMESTAMP = joke_app_REACTION_csv_reader['TIMESTAMP'].values.tolist()
    REACTION_reaction_id = joke_app_REACTION_csv_reader['reaction'].values.tolist()
    REACTION_user_username = joke_app_REACTION_csv_reader['reaction username'].values.tolist()
    REACTION_joketags_tags = joke_app_REACTION_csv_reader['joke tags'].values.tolist()
    REACTION_reaction_like = joke_app_REACTION_csv_reader['like'].values.tolist()
    REACTION_reaction_dislike = joke_app_REACTION_csv_reader['dislike'].values.tolist()
    REACTION_reaction_comment = joke_app_REACTION_csv_reader['comment'].values.tolist()
    REACTION_reaction_rate = joke_app_REACTION_csv_reader['rate (0 to 10)'].values.tolist()

    joke_app_USER_ACTIVITY_csv_reader = pd.read_csv("joke_app_USER_ACTIVITY.csv")
    USERACTIVITY_TIMESTAMP = joke_app_USER_ACTIVITY_csv_reader['TIMESTAMP'].values.tolist()
    USERACTIVITY_useractivity_id = joke_app_USER_ACTIVITY_csv_reader['useractivity ID'].values.tolist()
    USERACTIVITY_useractivity_activity = joke_app_USER_ACTIVITY_csv_reader['useractivity activity'].values.tolist()
    USERACTIVITY_user_username = joke_app_USER_ACTIVITY_csv_reader['reaction username'].values.tolist()

    joke_app_JOKE_TAGS_csv_reader = pd.read_csv("joke_app_JOKE_TAGS.csv")
    JOKETAGS_TIMESTAMP = joke_app_JOKE_TAGS_csv_reader['TIMESTAMP'].values.tolist()
    JOKETAGS_joke_id = joke_app_JOKE_TAGS_csv_reader['joke ID'].values.tolist()
    JOKETAGS_joketags_tag = joke_app_JOKE_TAGS_csv_reader['joke tags'].values.tolist()

def random_id():
    letters_list_qwerty = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    r_i = randint(0,99999999999999999999999)
    r_l_1 = random.choice(letters_list_qwerty)
    r_l_2 = random.choice(letters_list_qwerty)
    r_l_3 = random.choice(letters_list_qwerty)
    r_l_4 = random.choice(letters_list_qwerty)
    r_i = str(r_i)
    random_id_for_use = r_l_1 + r_l_2 + r_i + r_l_3 + r_l_4
    return random_id_for_use

def activity_user(a,b):
    # a = user_username
    # b = useractivity_activity
    input_datetime = datetime.now()
    USERACTIVITY_TIMESTAMP.append(input_datetime)
    h = True
    while h == True:
        i_id = random_id()
        if i_id in USERACTIVITY_useractivity_id:
            pass
        else:
            USERACTIVITY_useractivity_id.append(i_id)
            h = False
    USERACTIVITY_user_username.append(a)
    USERACTIVITY_useractivity_activity.append(b)

def login_user(a):
    # a = user_username
    input_datetime = datetime.now()
    i_qwerty_list = [i for i, value in enumerate(USERSLOGIN_user_username) if value == a]
    i = len(i_qwerty_list)
    USERSLOGIN_TIMESTAMP.append(input_datetime)
    USERSLOGIN_user_username.append(a)
    USERSLOGIN_userlogin_count.append(i)
    h = True
    while h == True:
        i_id = random_id()
        if i_id in USERLOGIN_userlogin_id:
            pass
        else:
            USERLOGIN_userlogin_id.append(i_id)
            h = False

def joke_tag_add(a,b):
    # a = joke_ID
    # b = joke_tag
    input_datetime = datetime.now()
    JOKETAGS_TIMESTAMP.append(input_datetime)
    JOKETAGS_joke_id.append(a)
    JOKETAGS_joketags_tag.append(b)

def joke_add(a,b,c):
    # a = joke ID 
    # b = joke CONTENT 
    # c = username CREATOR
    input_datetime = datetime.now()
    JOKE_TIMESTAMP.append(input_datetime)
    JOKE_joke_id.append(a)
    JOKE_joke_content.append(b)
    JOKE_user_username_creator.append(c)

def reaction_add(a,b,c):
# a = username user 
    # b = joketag 
    # c = joke_id
    # reaction_like = like 
    # reaction_dislike = dislike 
    # reaction_comment = comment
    # reaction_rate = rate
    reaction_id = str
    h = True
    while h == True:
        i_id = random_id()
        if i_id in REACTION_reaction_id:
            pass
        else:
            REACTION_reaction_id.append(i_id)
            h = False
            reaction_id = i_id

    hw_reaction_like = True
    while hw_reaction_like == True:
        print('do you like or dislike the joke')
        reaction_like_dislike = str(input(' like / dislike : '))
        if (reaction_like_dislike == 'like') or (reaction_like_dislike == 'dislike'):
            hw_reaction_like = False
            if reaction_like_dislike == 'like':
                qwerty_text = 'user liked joke '
                c = str(c)
                qwerty = qwerty_text + c
                activity_user(username_user,qwerty)
                reaction_like = 1
                reaction_dislike = 0
            if reaction_like_dislike == 'dislike':
                qwerty_text = 'user disliked joke '
                c = str(c)
                qwerty = qwerty_text + c
                activity_user(username_user,qwerty)
                reaction_like = 0
                reaction_dislike = 1
        else:
            print('Invalid Input')
    
    hw_reaction_comment = True
    while hw_reaction_comment == True:
        print('do you want to comment : ')
        reaction_comment_choice = str(input(' yes / no : '))
        if (reaction_comment_choice == 'yes') or (reaction_comment_choice == 'no'):
            if reaction_comment_choice == 'yes':
                qwerty_text = 'user chose to comment on joke '
                c = str(c)
                qwerty = qwerty_text + c
                activity_user(username_user,qwerty)
                hw_reaction_comment = False
                hw_reaction_comment_yes = True
                while hw_reaction_comment_yes == True:
                    reaction_comment = str(input('enter comment for joke : '))
                    qwerty_text = 'user entered comment '
                    qwerty_text_1 = ' on joke '
                    c = str(c)
                    qwerty = qwerty_text + reaction_comment + qwerty_text_1 + c
                    activity_user(username_user,qwerty)
                    print('your comment is ',reaction_comment)
                    reaction_comment_confirmation = str(input(' yes / no : '))
                    if (reaction_comment_confirmation == 'yes') or (reaction_comment_confirmation == 'no'):
                        if reaction_comment_confirmation == 'yes':
                            qwerty_qwerty_text = 'user confirmed joke comment '
                            qwerty_qwerty_text_1 = ' for reaction '
                            qwerty_qwerty_text_2 = ' on joke '
                            c = str(c)
                            qwerty_qwerty = qwerty_qwerty_text + reaction_comment + qwerty_qwerty_text_1 + reaction_id + qwerty_qwerty_text_2 + c
                            activity_user(username_user,qwerty_qwerty)
                            hw_reaction_comment_yes = False
                        if reaction_comment_confirmation == 'no':
                            pass
                    else:
                        print('Invalid Input')
            if reaction_comment_choice == 'no':
                qwerty = 'user chose to not comment on joke '
                c = str(c)
                qwerty_text = qwerty + c
                activity_user(username_user,qwerty_text)
                hw_reaction_comment = False
                reaction_comment = 'N/A'
        else:
            print('Invalid Input')
            hw_reaction_comment = True
    
    hw_reaction_rate = True
    while hw_reaction_rate == True:
        print('do you want to rate : ')
        reaction_rate_choice = str(input(' yes / no : '))
        if (reaction_rate_choice == 'yes') or (reaction_rate_choice == 'no'):
            if reaction_rate_choice == 'yes':
                qwerty_text = 'user chose to rate joke '
                c = str(c)
                qwerty = qwerty_text + c
                activity_user(username_user,qwerty)
                hw_reaction_rate = False
                hw_reaction_rate_yes = True
                while hw_reaction_rate_yes == True:
                    print('rate this joke from 0 to 10 \n i.e 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 or 10')
                    reaction_rate = int(input(' 0 to 10 : '))
                    reaction_rate_str = str(reaction_rate)
                    qwerty_text = 'user rated '
                    qwerty_text_1 = ' for joke '
                    c = str(c)
                    qwerty = qwerty_text + str(reaction_rate) + qwerty_text_1 + c
                    activity_user(username_user,qwerty)
                    print('you rated this joke ',reaction_rate,' out of 10')
                    reaction_rate_confirm = str(input(' yes / no : '))
                    if (reaction_rate_confirm == 'yes') or (reaction_rate_confirm == 'no'):
                        if reaction_rate_confirm == 'yes':
                            qwerty_text = 'user confirmed rating'
                            qwerty_text_1 = ' for reaction '
                            qwerty_text_2 = ' on joke '
                            qwerty = qwerty_text + reaction_rate_str + qwerty_text_1 + reaction_rate_str + qwerty_text_2 + c
                            activity_user(username_user,qwerty)
                            hw_reaction_rate_yes = False
                        if reaction_rate_confirm == 'no':
                            hw_reaction_rate_yes = True
                    else:
                        print('Invalid Input')
            if reaction_rate_choice == 'no':
                qwerty_text = 'user chose not to rate joke '
                qwerty = qwerty_text + c
                activity_user(username_user,qwerty)
                reaction_rate = 'N/A'
                hw_reaction_rate = False
        else:
            print('Invalid Input')
    
    input_datetime = datetime.now()
    REACTION_TIMESTAMP.append(input_datetime)
    REACTION_user_username.append(a)
    REACTION_joketags_tags.append(b)
    REACTION_reaction_like.append(reaction_like)
    REACTION_reaction_dislike.append(reaction_dislike)
    REACTION_reaction_comment.append(reaction_comment)
    REACTION_reaction_rate.append(reaction_rate)
    USER_ACTIVITY_update_csv()
    REACTION_update_csv()

def USERS_update_csv():
    dict = {'username' : USERS_user_username, 'password' : USERS_user_password, 'Name' : USERS_user_name}
    df = pd.DataFrame(dict)
    df.to_csv('joke_app_USERS.csv')

def USERSLOGIN_update_csv():
    dict = {'TIMESTAMP' : USERSLOGIN_TIMESTAMP, 'user login ID' : USERLOGIN_userlogin_id, 'username' : USERSLOGIN_user_username, 'user login count' : USERSLOGIN_userlogin_count}
    df = pd.DataFrame(dict)
    df.to_csv('joke_app_USER_LOGIN.csv')

def JOKE_update_csv():
    dict = {'TIMESTAMP' : JOKE_TIMESTAMP, 'joke ID' : JOKE_joke_id, 'joke Content' : JOKE_joke_content, 'Creator username' : JOKE_user_username_creator}
    df = pd.DataFrame(dict)
    df.to_csv('joke_app_JOKE.csv')

def REACTION_update_csv():
    dict = {'TIMESTAMP' : REACTION_TIMESTAMP, 'reaction ID' : REACTION_reaction_id, 'reaction username' : REACTION_user_username, 'joke tags' : REACTION_joketags_tags, 'like' : REACTION_reaction_like, 'dislike' : REACTION_reaction_dislike, 'comment' : REACTION_reaction_comment, 'rate (0 to 10)' : REACTION_reaction_rate}
    df = pd.DataFrame(dict)
    df.to_csv('joke_app_REACTION.csv')

def USER_ACTIVITY_update_csv():
    dict = {'TIMESTAMP' : USERACTIVITY_TIMESTAMP, 'useractivity ID' : USERACTIVITY_useractivity_id, 'useractivity activity' : USERACTIVITY_useractivity_activity, 'user' : USERACTIVITY_user_username}
    df = pd.DataFrame(dict)
    df.to_csv('joke_app_USER_ACTIVITY.csv')

def JOKETAGS_update_csv():
    dict = {'TIMESTAMP' : JOKETAGS_TIMESTAMP, 'joke ID' : JOKETAGS_joke_id, 'joke tags' : JOKETAGS_joketags_tag}
    df = pd.DataFrame(dict)
    df.to_csv('joke_app_JOKE_TAGS.csv')
hw = True
hw_authentication = True
while hw == True:
    USER_ACTIVITY_update_csv()
    while hw_authentication == True:
        USER_ACTIVITY_update_csv()
        print(' to log in type login \n to sign up type signup \n to stop the program type stop')
        user_input_authentication = str(input(' login / signup / stop : '))
        if (user_input_authentication == 'login') or (user_input_authentication == 'signup') or (user_input_authentication == 'stop'):
            
            if user_input_authentication == 'stop':
                activity_user(username_user,'stopped program')
                USER_ACTIVITY_update_csv()
                hw_authentication = False
                hw = False
                hw_app = False
            
            if user_input_authentication == 'login':
                
                hw_login = True
                while hw_login == True:
                    # update USER_ACTIVITY.csv
                    USER_ACTIVITY_update_csv()
                    print(q)
                    user_input_login_username = str(input('enter username for login : '))
                    user_input_login_password = str(input('enter password for login : '))
                    if user_input_login_username in USERS_user_username:
                        res_list = [i for i, value in enumerate(USERS_user_username) if value == user_input_login_username]
                        user_login_qwerty = res_list[0]
                        user_required_password = USERS_user_password[user_login_qwerty]
                        if user_input_login_password == user_required_password:
                            name_user = USERS_user_name[user_login_qwerty]
                            username_user = USERS_user_username[user_login_qwerty]
                            print('SECURITY PASSED', name_user)
                            hw_login = False
                            hw_authentication = False
                            hw_app = True
                            login_user(username_user)
                            activity_user(username_user,'Security Passed Login successful')
                            USERS_update_csv()
                            USERSLOGIN_update_csv()
                            JOKE_update_csv()
                            REACTION_update_csv()
                            USER_ACTIVITY_update_csv()
                            JOKETAGS_update_csv()
                            break
                        else:
                            print('Invalid Password')
                            activity_user(username_user,'Incorrect password Login failed')
                            USER_ACTIVITY_update_csv()
                    else:
                        print('InValid username')
                        activity_user(username_user,'Incorrect username Login failed')
                        USER_ACTIVITY_update_csv()

            if user_input_authentication == 'signup':

                hw_signup = True
                while hw_signup == True:
                    # update USER_ACTIVITY.csv
                    USER_ACTIVITY_update_csv()
                    print(q)
                    user_input_signup_username = str(input('enter username for signup : '))
                    if user_input_signup_username in USERS_user_username:
                        print('username already exists')
                    else:

                        hw_signup_password = True
                        while hw_signup_password == True:
                            user_input_signup_passsword = str(input('enter new password for signup : '))
                            user_input_signup_passsword_confirm = str(input('confirm new password for signup : '))
                            if user_input_signup_passsword == user_input_signup_passsword_confirm:
                                print('passwords match')
                                hw_signup_password = False
                            else:
                                print('passwords do not match')
                        
                        hw_signup_name = True
                        while hw_signup_name == True:
                            # update USER_ACTIVITY.csv
                            USER_ACTIVITY_update_csv()
                            user_input_signup_name = str(input('enter your name : '))
                            print('your name is',user_input_signup_name)
                            user_input_signup_name_confirm = str(input(' yes / no : '))
                            if (user_input_signup_name_confirm == 'yes') or (user_input_signup_name_confirm == 'no'):
                                if user_input_signup_name_confirm == 'yes':
                                    USERS_user_name.append(user_input_signup_name)
                                    USERS_user_username.append(user_input_signup_username)
                                    USERS_user_password.append(user_input_signup_passsword_confirm)
                                    name_user = user_input_signup_name
                                    username_user = user_input_signup_username
                                    hw_signup_name = False
                                    hw_signup = False
                                    hw_authentication = False
                                    hw_app = True
                                    login_user(username_user)
                                    activity_user(username_user,'Sign Up Successful')
                                    # add data to database for USERS.csv#
                                    USERS_update_csv()
                                    USERSLOGIN_update_csv()
                                    JOKE_update_csv()
                                    REACTION_update_csv()
                                    USER_ACTIVITY_update_csv()
                                    JOKETAGS_update_csv()
                                    break
                                if user_input_signup_name_confirm == 'no':
                                    pass
                            else:
                                print('InValid Input')

        else:
            print('InValid Input')

    while hw_app == True:
        USERS_update_csv()
        USERSLOGIN_update_csv()
        JOKE_update_csv()
        REACTION_update_csv()
        USER_ACTIVITY_update_csv()
        JOKETAGS_update_csv()
        # update USER_ACTIVITY.csv
        USER_ACTIVITY_update_csv()
        print(' Welcome to the app main menu',name_user)
        print(' to access the JOKES menu type jokes \n to log out of the app type logout')
        user_input_app_main_menu_choice = str(input(' jokes / logout : '))
        if (user_input_app_main_menu_choice == 'jokes') or (user_input_app_main_menu_choice == 'logout'):
            if user_input_app_main_menu_choice == 'logout':
                USERS_update_csv()
                USERSLOGIN_update_csv()
                JOKE_update_csv()
                REACTION_update_csv()
                USER_ACTIVITY_update_csv()
                JOKETAGS_update_csv()
                hw_app = False
                hw_authentication = True
                activity_user(username_user,'App Log Out')
                # update USER_ACTIVITY.csv
                USER_ACTIVITY_update_csv()
                break
            if user_input_app_main_menu_choice == 'jokes':
                USERS_update_csv()
                USERSLOGIN_update_csv()
                JOKE_update_csv()
                REACTION_update_csv()
                USER_ACTIVITY_update_csv()
                JOKETAGS_update_csv()
                activity_user(username_user,'JOKE menu access')
                hw_joke = True
                while hw_joke == True:
                    # update USER_ACTIVITY.csv
                    USERS_update_csv()
                    USERSLOGIN_update_csv()
                    JOKE_update_csv()
                    REACTION_update_csv()
                    USER_ACTIVITY_update_csv()
                    JOKETAGS_update_csv()
                    print(' to add a joke type add \n to view a joke type view \n to go back type back')
                    user_input_joke_main_menu_choice = str(input(' add / view / back : '))
                    if (user_input_joke_main_menu_choice == 'add') or (user_input_joke_main_menu_choice == 'view') or (user_input_joke_main_menu_choice == 'back'):
                        USERS_update_csv()
                        USERSLOGIN_update_csv()
                        JOKE_update_csv()
                        REACTION_update_csv()
                        USER_ACTIVITY_update_csv()
                        JOKETAGS_update_csv()
                        if user_input_joke_main_menu_choice == 'back':
                            activity_user(username_user,'Joke Main Menu to App Main Menu')
                            hw_joke = False
                            hw_app = True
                            break
                        if user_input_joke_main_menu_choice == 'add':
                            USERS_update_csv()
                            USERSLOGIN_update_csv()
                            JOKE_update_csv()
                            REACTION_update_csv()
                            USER_ACTIVITY_update_csv()
                            JOKETAGS_update_csv()
                            hw_add_joke = True
                            while hw_add_joke == True:
                                activity_user(username_user,'accessed add joke menu')
                                h = True
                                while h == True:
                                    input_JOKE_joke_id = random_id()
                                    if input_JOKE_joke_id in JOKE_joke_id:
                                        pass
                                    else:
                                        h = False
                                hw_add_joke_JOKE_joke_content = True
                                while hw_add_joke_JOKE_joke_content == True:
                                    print('the joke content is the main joke')
                                    user_input_JOKE_joke_content = str(input('enter joke content : '))
                                    print(' your joke is : \n ', user_input_JOKE_joke_content)
                                    hw_add_joke_JOKE_joke_content_confirmation = True
                                    while hw_add_joke_JOKE_joke_content_confirmation == True:
                                        user_input_JOKE_joke_content_confirmation = str(input(' yes / no : '))
                                        if (user_input_JOKE_joke_content_confirmation == 'yes') or (user_input_JOKE_joke_content_confirmation == 'no'):
                                            if user_input_JOKE_joke_content_confirmation == 'yes':
                                                hw_add_joke_JOKE_joke_content_confirmation = False
                                                hw_add_joke_JOKE_joke_content = False
                                                break
                                            if user_input_JOKE_joke_content_confirmation == 'no':
                                                pass
                                        else:
                                            print('Invalid Input')
                                    input_JOKE_joke_username_creator = username_user
                                    input_JOKE_TIMESTAMP = datetime.now()
                                    hw_add_joke_JOKETAGS_joketags_tags = True
                                    while hw_add_joke_JOKETAGS_joketags_tags == True:
                                        print('the joke tag is similar to a hashtag')
                                        user_input_JOKETAGS_joketags_tags = str(input('enter joke tag : '))
                                        hw_add_joke_JOKETAGS_joketags_tags_confiration = True
                                        while hw_add_joke_JOKETAGS_joketags_tags_confiration == True:
                                            print('joke tag is',user_input_JOKETAGS_joketags_tags)
                                            user_input_JOKETAGS_joketags_tags_confirmation = str(input(' yes / no : '))
                                            if (user_input_JOKETAGS_joketags_tags_confirmation == 'yes') or (user_input_JOKETAGS_joketags_tags_confirmation == 'no'):
                                                if user_input_JOKETAGS_joketags_tags_confirmation == 'yes':
                                                    joke_tag_add(input_JOKE_joke_id,user_input_JOKETAGS_joketags_tags)
                                                    JOKETAGS_update_csv()
                                                    hw_add_joke_JOKETAGS_joketags_tags_confiration = False
                                                    hw_add_joke_JOKETAGS_joketags_tags = True
                                                if user_input_JOKETAGS_joketags_tags_confirmation == 'no':
                                                    hw_add_joke_JOKETAGS_joketags_tags_confiration = False
                                                    hw_add_joke_JOKETAGS_joketags_tags = True
                                            else:
                                                print('Invalid Input')
                                        hw_add_joke_JOKETAGS_joketags_tags_again = True
                                        while hw_add_joke_JOKETAGS_joketags_tags_again == True:
                                            print('do you want to add another tag for the same joke')
                                            user_input_JOKETAGS_joketags_tags_again = str(input(' yes / no : '))
                                            if (user_input_JOKETAGS_joketags_tags_again == 'yes') or (user_input_JOKETAGS_joketags_tags_again == 'no'):
                                                if user_input_JOKETAGS_joketags_tags_again == 'yes':
                                                    hw_add_joke_JOKETAGS_joketags_tags_again = False
                                                    hw_add_joke_JOKETAGS_joketags_tags = True
                                                if user_input_JOKETAGS_joketags_tags_again == 'no':
                                                    hw_add_joke_JOKETAGS_joketags_tags_again = False
                                                    hw_add_joke = False
                                                    hw_add_joke_JOKETAGS_joketags_tags = False
                                            else:
                                                print('Invalid Input')

                            activity_user(username_user,'added joke')
                            joke_add(input_JOKE_joke_id,user_input_JOKE_joke_content,username_user)
                            USERS_update_csv()
                            USERSLOGIN_update_csv()
                            JOKE_update_csv()
                            REACTION_update_csv()
                            USER_ACTIVITY_update_csv()
                            JOKETAGS_update_csv()
                        if user_input_joke_main_menu_choice == 'view':
                            activity_user(username_user,'viewed joke')
                            USER_ACTIVITY_update_csv()
                            qwerty_qwerty = -1
                            output_joke_tags = str
                            for a in JOKE_joke_id:
                                qwerty_qwerty += 1
                                output_joke_creator_username = JOKE_user_username_creator[qwerty_qwerty]
                                output_joke_content = JOKE_joke_content[qwerty_qwerty]
                                joke_tags_list = [i for i, value in enumerate(JOKETAGS_joke_id) if value == a]
                                joke_tags_output_list = []
                                for abc in joke_tags_list:
                                    joke_tags_output_list.append(JOKETAGS_joketags_tag[abc])
                                j = ', '
                                j_qwerty = j.join(joke_tags_output_list)
                                print('**************************************')
                                print('creator : ',output_joke_creator_username)
                                print('content : ',output_joke_content)
                                print('joke tags : ',j.join(joke_tags_output_list))
                                print('**************************************')
                                qwerty_text = 'viewed '
                                qwerty_text_final = qwerty_text + a
                                activity_user(username_user,qwerty_text_final)
                                USER_ACTIVITY_update_csv()
                                reaction_add(username_user,j_qwerty,a)
                                USERS_update_csv()
                                USERSLOGIN_update_csv()
                                JOKE_update_csv()
                                REACTION_update_csv()
                                USER_ACTIVITY_update_csv()
                                JOKETAGS_update_csv()
                    else:
                        print('Invalid Input')
        else:
            print('Invalid Input')