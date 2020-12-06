function upload(uid,full_name){
    var title=document.getElementById("title")
    var description=document.getElementById("description")
    var price=document.getElementById("price")
    var duration = document.getElementById("duration")
    var priceWithDuration = String(price.value) + " per " + String(duration.value)
    const ref=firebase.storage().ref();
    const file=document.getElementById("customFile").files[0];
    // console.log(file)
    const name=new Date()+'-'+file.name;
    const metaData={
        contentType:file.type
    }
    const task=ref.child('lease').child(uid).child(name).put(file,metaData);
    task
    .then(snapshot => snapshot.ref.getDownloadURL())
    .then(url => {
        alert("Ad created successfully. Please reload the page to see the new entry.")
        firebase.database().ref("/lease").child(uid).push({
            0:title.value,
            1:description.value,
            2:full_name,
            3:url,
            4:priceWithDuration
        }).then((snap) => {
            const key = snap.key
            console.log(key);
            firebase.database().ref("/lease_titles").child(document.getElementById("title").value.toLowerCase()).push({
                0:uid,
                1:key
            });
            title.value="";
            description.value="";
            price.value="";
            duration.value="";
        });
    });

}
