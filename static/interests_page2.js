function changeStatus(evt, status, uid, parentKey,itemId,showerId) {
    console.log(evt.currentTarget);
    var x = evt.currentTarget.parentElement;
    console.log(x);
    var y=x.parentElement;
    x.remove();
    var newspanItem = document.createElement("span");

    
    newspanItem.className="response101";
    if (status=="accepted") 
    {
        newspanItem.innerHTML="Interest Accepted";
        firebase.database().ref("/interest_shown").child(uid).child(parentKey).set({
            0:1,
            1:itemId,
            2:showerId
        });

        firebase.database().ref("/interest_received").child(uid).child(parentKey).set({
            0:1,
            1:itemId,
            2:showerId
        });
        
    }
    else {
        newspanItem.innerHTML="Interest Rejected";
    }
    y.appendChild(newspanItem);
}