function changeStatus(evt, status) {
    console.log(evt.currentTarget);
    var x = evt.currentTarget.parentElement;
    console.log(x);
    var y=x.parentElement;
    x.remove();
   

}
