function search_clicked() {
    var search_item=document.getElementById("search_bar").value
    console.log(search_item)
    console.log(typeof search_item)
    var list_of_items=firebase.database().ref("/titles").orderByKey().equalTo(search_item);
    list_of_items.on('value', (snapshot) =>{
        const data = snapshot.val();
        var keys = Object.keys(data[search_item]);
        for(var i = 0; i < keys.length; i++){
            var k = keys[i];
            
        
        }

    });
}