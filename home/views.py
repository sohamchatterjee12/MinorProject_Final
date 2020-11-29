from django.shortcuts import render,HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
##########################Pyrebase####################################
import pyrebase
config = {
    "apiKey": "AIzaSyAXwgisDN7kx6BMZCIwYjj8KNDgmJuz1Mg",
    "authDomain": "exampledjango-4af38.firebaseapp.com",
    "databaseURL": "https://exampledjango-4af38.firebaseio.com",
    "storageBucket": "exampledjango-4af38.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database() ##database reference
authe = firebase.auth()   ##authentication reference
#######################################################################
# Create your views here.
def texts_page(request):
    if request.session.is_empty() == False: 
        try : 
            msgs1 = db.child("messages").child(request.session["uid"]).shallow().get()  
        except:
            pass
        onlineUsers = db.child("onlineUsers").shallow().get()
        # print(msgs1)
        if msgs1.val() is None : 
            context = {
                "names" : None,
            }
            return render(request,"texts_page.html", context)
        # print(onlineUsers.val())
        # print('3' in onlineUsers.val())
        # msgs2 = db.child("messages").child("2").child("1").get()
        # print(type(msgs))
        # print(msgs1.val())
        messages1 = list(msgs1.val())
        names = []
        for userid in messages1:
            eachName = db.child("userId").child(userid).get()

            if userid in onlineUsers.val():
                names.append([eachName.val()["fName"], userid, "online"])
            else:
                print(eachName.val())
                names.append([eachName.val()["fName"], userid, "offline"])



        context = {}
        # context["messages"] = messages?
        context["names"] = names
        context["uid"] = request.session["uid"]
        # print(type(tempMsg))
        # print(messages)
        return render(request,"texts_page.html", context)
    else:
        return landing_page_with_context(request, {'first_login' : True})

def interests_page(request):
    if request.session.is_empty() == False:
        interest_shown_response = db.child("interests_shown").child(request.session["uid"]).get() 
        interest_received_response = db.child("interests_received").child(request.session["uid"]).get() 
        #interest_shown_keys_response=db.child("interests_shown").child(request.session["uid"]).shallow().get()
        #interest_received_keys_response=db.child("interests_received").child(request.session["uid"]).shallow().get() 
        
        interest_shown=interest_shown_response.val()
        interest_received=interest_received_response.val()
        #interest_shown_keys=list(interest_shown_keys_response.val())
        #interest_received_keys=list(interest_received_keys_response.val())
        #print(interest_shown)
        #print(interest_received)
        #print(interest_shown_keys)
        #print(interest_received_keys)
        
        for i in interest_shown.keys():
            shownName=db.child("userId").child(interest_shown[i][2]).get()
            fullName=shownName.val()["fName"]+" "+shownName.val()["lName"]
            interest_shown[i][2]=fullName
            interest_shown[i].append(i)
        interest_shown=list(interest_shown.values())

        for i in interest_received.keys():
            receivedName=db.child("userId").child(interest_received[i][2]).get()
            fullName=receivedName.val()["fName"]+" "+receivedName.val()["lName"]
            interest_received[i][2]=fullName
            interest_received[i].append(i)
        interest_received=list(interest_received.values())
        context={}
        context["interest_shown"]=interest_shown
        context["interest_received"]=interest_received
        context["uid"]=request.session["uid"]
        print(context)
        return render(request,'interests_page.html',context)
    else:
        return landing_page_with_context(request, {'first_login' : True})

def confirmations_page(request):
    if request.session.is_empty() == False:
        return render(request,'confirmations_page.html')
    else:
        return landing_page_with_context(request, {'first_login' : True})

def buy_page(request):
    if request.session.is_empty() == False:
        return render(request,'buy_page.html')
    else:
        return landing_page_with_context(request, {'first_login' : True})

def sell_page(request):
    if request.session.is_empty() == False :
        return render(request,'sell_page.html')
    else:
        return landing_page_with_context(request, {'first_login' : True})

def rent_page(request):
    if request.session.is_empty() == False :
        return render(request,'rent_page.html')
    else:
        return landing_page_with_context(request, {'first_login' : True})

def lease_page(request):
    if request.session.is_empty() == False :
        return render(request,'lease_page.html')
    else:
        return landing_page_with_context(request, {'first_login' : True})

def render_service_page(request):
    if request.session.is_empty() == False :
        return render(request,'render_service_page.html')
    else:
        return landing_page_with_context(request, {'first_login' : True})

def require_service_page(request):
    if request.session.is_empty() == False :
        return render(request,'require_service_page.html')
    else:
        return landing_page_with_context(request, {'first_login' : True})

def account_details_page(request):
    if request.session.is_empty() == False :
        return render(request,'account_details_page.html')
    else:
        return landing_page_with_context(request, {'first_login' : True})

def all_transactions_page(request):
    if request.session.is_empty() == False :
        return render(request,'all_transactions_page.html')
    else:
        return landing_page_with_context(request, {'first_login' : True})

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def landing_page_with_context(request, context):
        return render(request, 'landing_page.html', context)

def landing_page_register(request):
    return render(request, "landing_page_register.html")


def landing_page(request):
    if request.method == 'POST':  ## registering a user
        fName = request.POST.get("fName")
        lName = request.POST.get("lName")
        email = request.POST.get("email")
        password = request.POST.get("password")
        conPass = request.POST.get("conPass")

        users = db.child("users").get()
        
        try:
            # print("absydvsa")
            user = authe.create_user_with_email_and_password(email, password)
            # print(user)
            
            authe.send_email_verification(user['idToken'])

            # print(users)
            count = len(users.val()) + 1

            data = {
                "userId": count
            }
            tempEmail = ""  ## generating mail for firebase DB
            for i in email :
                if i == '@':
                    break
                if i == '.':
                    tempEmail += '@'
                    continue
                tempEmail += i

            # print(tempEmail)

            db.child("users").child(tempEmail).set(data)
            data = {
                "fName": fName,
                "lName": lName,
            }
            db.child("userId").child(count).set(data)
            context = {
                "not_verified_email" : False,
                'bad_login' : False,
                "POST_request" : True,
                "forgot_password" : False,
                "incorrect_email" : False,
                "Email_already_registered" : False,
                "logged_out" : False,
                "first_login" : False
            }
            return render(request, 'landing_page.html', context)

        except:
            context = {
                "not_verified_email" : False,
                'bad_login' : False,
                "POST_request" : False,
                "forgot_password" : False,
                "incorrect_email" : False,
                "Email_already_registered" : True,
                "logged_out" : False,
                "first_login" : False
            }
            return landing_page_with_context(request, context)
    
    context = {
            "not_verified_email" : False,
            'bad_login' : False,
            "POST_request" : False,
            "forgot_password" : False,
            "incorrect_email" : False,
            "Email_already_registered" : False,
            "logged_out" : False,
            "first_login" : False
        }
    return render(request,'landing_page.html', context)

def home_page(request):    
    if request.session.is_empty() == False:
        return render(request,'home_page.html')
    else:
        return landing_page_with_context(request, {'first_login' : True})

def home_page_with_context(request, context):
    if request.session.is_empty() == False:
        return render(request, 'home_page.html', context)
    else:
        return landing_page_with_context(request, {'first_login' : True})

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get("forgot_pass_email")
        try : 
            authe.send_password_reset_email(email)
            context = {
                        "not_verified_email" : False,
                        'bad_login' : False,
                        "POST_request" : False,
                        "forgot_password" : True,
                        "incorrect_email" : False,
                        "Email_already_registered" : False,
                        "logged_out" : False,
                        "first_login" : False
                    }
            return landing_page_with_context(request, context)
        except:
            context = {
                        "not_verified_email" : False,
                        'bad_login' : False,
                        "POST_request" : False,
                        "forgot_password" : False,
                        "incorrect_email" : True,
                        "Email_already_registered" : False,
                        "logged_out" : False,
                        "first_login" : False
                    }
            return landing_page_with_context(request, context)

def logout(request):
    db.child("onlineUsers").child(request.session["uid"]).remove()
    request.session.flush()

    context = {
        "not_verified_email" : False,
        'bad_login' : False,
        "POST_request" : False,
        "forgot_password" : False,
        "incorrect_email" : False,
        "Email_already_registered" : False,
        "logged_out" : True,
        "first_login" : False
    }
    return landing_page_with_context(request, context)

def login(request):
    if request.method == 'POST':  ## signing in user
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = authe.sign_in_with_email_and_password(email, password)
            userInfo = authe.get_account_info(user['idToken'])

            # print(userInfo["users"][0]["emailVerified"])

            if userInfo["users"][0]["emailVerified"] == False : 
                context = {
                    "not_verified_email" : True,
                    "bad_login" : False,
                    "POST_request": False,
                    "forgot_password" : False,
                    "incorrect_email" : False,
                    "Email_already_registered" : False,
                    "logged_out" : False,
                    "first_login" : False
                }
                return landing_page_with_context(request, context)
                
            if userInfo["users"][0]["emailVerified"] == True:
                # print(user)
                tempEmail = ""
                for i in email :
                    if i == '@':
                        break
                    if i == '.':
                        tempEmail += '@'
                        continue
                    tempEmail += i
                userDB = db.child("users").child(tempEmail).get()
                # print(userD)
                
                
                ################# SESSION SETTINGS ############
                request.session["uid"] = userDB.val()["userId"]
                userIdDB = db.child("userId").child(request.session["uid"]).get()
                user["displayName"] = userIdDB.val()["fName"]
                # request.session["email"] = email
                request.session["fName"] = userIdDB.val()["fName"]
                request.session["lName"] = userIdDB.val()["lName"]
                # request.session["tempEmail"] = tempEmail
                ################################################
                
                data = {
                    "active" : True,
                    "userid" : request.session["uid"]
                }
                db.child("onlineUsers").child(request.session["uid"]).set(data)

                context = {
                    'user_name': user["displayName"],
                    "uid" : request.session["uid"],
                    "fName" : request.session["fName"],
                    "lName" : request.session["lName"],
                }
                return home_page_with_context(request, context)
                
        except: ## Wrong Credentials
            context = {
                "not_verified_email" : False,
                'bad_login' : True,
                "POST_request" : False,
                "forgot_password" : False,
                "incorrect_email" : False,
                "Email_already_registered" : False,
                "logged_out" : False,
                "first_login" : False
            }
            return landing_page_with_context(request, context)

def test(request):
    # print(request.session["uid"])
    msgs1 = db.child("messages").child(request.session["uid"]).shallow().get()
    # msgs2 = db.child("messages").child("2").child("1").get()
    # print(type(msgs))
    # print(msgs1.val())
    messages1 = list(msgs1.val())
    names = []
    for userid in messages1:
        eachName = db.child("userId").child(userid).get()
        names.append([eachName.val()["fName"], userid])
    # print(type(messages1))
    # print(messages1)

    # tempMsg1 = list(messages1.values())
    # tempMsg2 = list(messages2.values())

    # tempMsg = tempMsg1
    # tempMsg.sort(key = lambda x : x[1])

    # tempMsg = [x[0] for x in tempMsg]
    # print(tempMsg)
    # x = tuple(tempMsg[0])
    # print(x[1])

    context = {}
    # context["messages"] = messages?
    context["names"] = names
    # print(type(tempMsg))
    # print(messages)
    return render(request,"testTemplate.html")

