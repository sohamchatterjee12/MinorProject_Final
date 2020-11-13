from django.shortcuts import render,HttpResponse
from django.contrib import auth
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

def home_page(request):
    if request.method == 'POST':  ## signing in user
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = authe.sign_in_with_email_and_password(email, password)
            userInfo = authe.get_account_info(user['idToken'])

            print(userInfo["users"][0]["emailVerified"])

            if userInfo["users"][0]["emailVerified"] == False : 
                context = {
                    "not_verified_email" : True,
                    "bad_login" : False,
                    "POST_request": False
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
                user["displayName"] = userDB.val()["fName"]
    
                # print(user)

                context = {
                    'user_name': user["displayName"]
                }
                return render(request, 'home_page.html', context)
        except: ## Wrong Credentials
            context = {
                "not_verified_email" : False,
                'bad_login' : True,
                "POST_request" : False
            }
            return landing_page_with_context(request, context)

    return render(request,'home_page.html')

def landing_page_with_context(request, context):
    return render(request, 'landing_page.html', context)

def landing_page(request):
    if request.method == 'POST':  ## registering a user
        fName = request.POST.get("fName")
        lName = request.POST.get("lName")
        email = request.POST.get("email")
        password = request.POST.get("password")
        conPass = request.POST.get("conPass")

        users = db.child("users").get()

        user = authe.create_user_with_email_and_password(email, password)
        print(user)

        authe.send_email_verification(user['idToken'])

        count = 0
        for user in users:
            count += 1
        count = count + 1

        data = {
            "userId": count,
            "fName": fName,
            "lName": lName
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
        
        context = {
            "not_verified_email" : False,
            'bad_login' : False,
            "POST_request" : True
        }
        return render(request, 'landing_page.html', context)
    
    context = {
            "not_verified_email" : False,
            'bad_login' : False,
            "POST_request" : False
        }
    return render(request,'landing_page.html', context)

def landing_page_register(request):
    return render(request, "landing_page_register.html")