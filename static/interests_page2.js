function changeStatus(evt, status, uid, parentKey,itemId,showerId) {
    console.log(evt.currentTarget);
    var x = evt.currentTarget.parentElement;
    console.log(x);
    var y=x.parentElement;
    x.remove();
    var newspanItem = document.createElement("span");
    //parentKey=String(parentKey)
    //console.log(String(parentKey))
    newspanItem.className="response101";
    x=firebase.database().ref("/interests_received").child(uid).child(parentKey)
    x.on('value', gotData, errData);
    if (status=="accepted") 
    {
        newspanItem.innerHTML="Interest Accepted";
        //console.log(parentKey)
        // x.update({
        //     0:1,
        // });
        
    }
    else {
        newspanItem.innerHTML="Interest Rejected";
    }
    y.appendChild(newspanItem);
}


function gotData(data){
    var tempData = data.val();
    console.log(tempData)
}

function errData(err){
    console.log("Error");
    console.log(err);
}