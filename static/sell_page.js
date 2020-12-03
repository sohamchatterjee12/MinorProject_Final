function upload(uid){
    const ref=firebase.storage().ref();
    const file=document.getElementById("inputGroupFile01").files[0];
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


    
}