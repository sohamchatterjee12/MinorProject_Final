function upload(uid){
    const ref=firebase.storage().ref();
    const file=document.getElementById("customFile").files[0];
    console.log(file)
    const name=new Date()+'-'+file.name;
    const metaData={
        contentType:file.type
    }
    const task=ref.child('sell').child(uid).child(name).put(file,metaData);
    task
    .then(snapshot => snapshot.ref.getDownloadURL())
    .then(url => {
        console.log(url)
        alert("Image upload successful")
    })


    var title=document.getElementById("title")
    var description=document.getElementById("description")
    var price=document.getElementById("price")
    title.value="";
    description.value="";
    price.value="";
}