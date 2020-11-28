function changeStatus(evt, status) {
    console.log(evt.currentTarget);
    var x = evt.currentTarget.parentElement;
    console.log(x);
    var y=x.parentElement;
    x.remove()
    var newspanItem = document.createElement("span");
    newspanItem.className="response101";
    if (status=="accepted") 
    {
        newspanItem.innerHTML="Interest Accepted";
    }
    else {
        newspanItem.innerHTML="Interest Rejected";
    }
    y.appendChild(newspanItem);
}