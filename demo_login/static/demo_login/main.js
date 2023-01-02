var btn = document.getElementById('mybtn')
var modal = document.getElementById('mymodal')
var span = document.getElementById('close')

btn.onclick = function(){
    modal.style.display="block";
}

span.onclick = function() {
    modal.style.display="none";
}

window.onclick = function(event){
    if(event.target==modal){
        modal.style.display="none";
    }
}