function ShowAlert(){


var username=document.getElementById('name').value;
var first_name=document.getElementById('first').value;
var last_name=document.getElementById('last').value;
var email=document.getElementById('email').value;
var password=document.getElementById('pass').value;
var cpassword=document.getElementById('cpass').value;

if(!username || !first_name ||  !last_name || !email || !password || !cpassword ){

alert("Please fill out all the field")
}
else{

alert('Registration completed, Now you can login')
}
}