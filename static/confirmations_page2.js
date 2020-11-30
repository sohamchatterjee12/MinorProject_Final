function changeStatus(evt, status, uid, parentKey,showerId,productId) {
    console.log(evt.currentTarget);
    var x = evt.currentTarget.parentElement;
    console.log(x);
    var y=x.parentElement;
    y.parentElement.remove();

    console.log(uid)
    console.log(parentKey)
    if (status=="shipped") {

        firebase.database().ref("/confirmations_shipped").child(uid).child(parentKey).update({
            0:1
        });

    }
    else if (status=="not_shipped") {

        firebase.database().ref("/confirmations_shipped").child(uid).child(parentKey).update({
            0:-1
        });

    }
    else if (status=="received") {

        firebase.database().ref("/confirmations_received").child(uid).child(parentKey).update({
            0:1
        });
    }
    else {

        firebase.database().ref("/confirmations_received").child(uid).child(parentKey).update({
            0:-1
        });
    }

   

}
