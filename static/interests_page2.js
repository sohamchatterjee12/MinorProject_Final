function changeStatus(evt, status, uid, parentKey,showerId,productId) {
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
    //var add_msg_Received=firebase.database().ref("/messages");
    if (status=="accepted") 
    {
        newspanItem.innerHTML="Interest Accepted";
        received_interestToChange.update({
            0:1,
        });
        
        shown_interestToChange.update({
            0:1,
        });
        console.log(typeof uid)
        console.log(uid)
        firebase.database().ref("/messages").child(uid).child(showerId).push({
            0:"You can chat with me now (This is an auto generated message)",
            1:Date.now(),
            2:uid
        });

        firebase.database().ref("/messages").child(showerId).child(uid).push({
            0:"You can chat with me now (This is an auto generated message)",
            1:Date.now(),
            2:showerId
        });

        var confirmation_count_response=firebase.database().ref("/count").child("confirmations")
        
        confirmation_count_response.once('value', (snapshot) =>{


            const data = snapshot.val();
            var confirmation_id='"'+String(data+1)+'"';
            console.log(confirmation_id)

        firebase.database().ref("/confirmations_shipped").child(uid).child(confirmation_id).set({
            0:0,
            1:productId,
            2:showerId
        });


        firebase.database().ref("/count").update({
            confirmations:data+1
        })

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
