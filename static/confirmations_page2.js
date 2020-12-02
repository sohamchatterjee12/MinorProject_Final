function changeStatus(evt, status, uid, parentKey,toFromId,productId) {
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

        firebase.database().ref("/confirmations_received").child(toFromId).child(parentKey).set({
            0:0,
            1:productId,
            2:uid
        });
        
    }
    else if (status=="not_shipped") {

        firebase.database().ref("/confirmations_shipped").child(uid).child(parentKey).update({
            0:-1
        });

        firebase.database().ref("/confirmations_received").child(toFromId).child(parentKey).set({
            0:-1,
            1:productId,
            2:uid
        });

    }
    else if (status=="received") {

        firebase.database().ref("/confirmations_received").child(uid).child(parentKey).update({
            0:1
        });

        currentTime=String(new Date()).replace(" GMT+0530 (India Standard Time)","");
        console.log(currentTime)
        firebase.database().ref("/all_transactions").child(uid).push({
            0:currentTime,
            1:productId,
            2:toFromId,
            3:1
        });

        firebase.database().ref("/all_transactions").child(toFromId).push({
            0:currentTime,
            1:productId,
            2:uid,
            3:2
        });
    }
    else {

        firebase.database().ref("/confirmations_received").child(uid).child(parentKey).update({
            0:-1
        });

        firebase.database().ref("/confirmations_shipped").child(toFromId).child(parentKey).update({
            0:-1,
        });
    }

}
