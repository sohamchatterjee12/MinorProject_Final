function checkPassAndConPass(){
    var password = document.getElementById("pass");
    var conPass = document.getElementById("conPass");
    var conPassLength = conPass.value.length;

    console.log(password.value);
    console.log(conPass.value);
    console.log(conPassLength);
   
    var passAfterLength = conPass.value.substring(0, conPassLength);

    // console.log(passAfterLength);
    console.log(password.value);

    if(conPass.value != password.value){
        document.getElementById("message").innerHTML= "<span style='color:red'>Password and confirm password not matching</span>";
        document.getElementById("Register").disabled = true;
    }
    else
    if(conPass.value === password.value){
        document.getElementById("message").innerHTML= "<span style='color:green'>Password and confirm password matching</span>";
        document.getElementById("Register").disabled = false;
    }
}
