console.log("d");
let text=document.getElementById("mt")
let btn=document.getElementById("rs");
let submit=document.getElementById("mp")
btn.addEventListener("click",del);
function del(){
    text.value="";
}
submit.addEventListener("click",sub);
function sub(){
    text.value
}
//btn.addEventListener("click",sub);
