function changeStatus(evt, status, uid, parentKey,showerId) {
    console.log(evt.currentTarget);
    var x = evt.currentTarget.parentElement;
    console.log(x);
    var y=x.parentElement;
    x.remove();
    var newspanItem = document.createElement("span");
    newspanItem.className="response101";

    parentKey='"'+parentKey+'"'
    console.log(parentKey)
    var received_interestToChange=firebase.database().ref("/interests_received").child(uid).child(parentKey);
    var shown_interestToChange=firebase.database().ref("/interests_shown").child(showerId).child(parentKey);

    if (status=="accepted") 
    {
        newspanItem.innerHTML="Interest Accepted";
        received_interestToChange.update({
            0:1,
        });
        
        shown_interestToChange.update({
            0:1,
        });

        
    }
    else {

        newspanItem.innerHTML="Interest Rejected";
        received_interestToChange.update({
            0:-1
        })

        shown_interestToChange.update({
            0:-1,
        });
    }
    y.appendChild(newspanItem);
}
