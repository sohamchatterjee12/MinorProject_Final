from django.shortcuts import render,HttpResponse
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
#######################################################################
# Create your views here.
def home_page(request):
    return render(request,'home_page.html')

def landing_page(request):
    return render(request,'landing_page.html')

def landing_page_register(request):
    if request.method == 'POST':
        fName = request.POST.get("fName")
        lName = request.POST.get("lName")
        email = request.POST.get("email")
        password = request.POST.get("password")
        conPass = request.POST.get("conPass")

        
        data = {
            "fName": fName,
            "lName": lName,
            "email": email,
            "password": password
        }

        db.child("users").push(data)

    return render(request, "landing_page_register.html")