window.addEventListener("load", display);

const logo = document.querySelector(".logo");
var horaire = document.querySelector(".horaire");
var background= document.querySelector(".vertfirst");
var width = window.screen.width;
var modal = document.getElementById("myModal");
var btn = document.getElementsByClassName("close")[0];
var couleurs = ["#f8ef88","#5cba9a","white","#f29799"];

//------------DISPLAY-ALERT------------------------
function display(){
let alerte = document.getElementById("alerte").innerHTML;
let isEmpty = document.getElementById("alerte").textContent === "";
		if ( alerte != isEmpty ){
			modal.style.display= "flex";
			btn.style.display= "flex";
		}else{
			modal.style.display= "none";
			btn.style.display= "none";
		}};

//------------CLOSE-DIALOG------------------------
btn.onclick = function() {
  modal.style.display = "none";
  btn.style.display = "none";
}
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
    btn.style.display = "none";
    console.log('KO');
}
};

//-------------SCROLLEVENT------------------------
window.addEventListener('scroll', () => {
	if ( window.scrollY > 100){
 	logo.style.transform= " scale(0.6) translate(-40vw, -35vh) ";
	logo.style.transition= "transform 0.8s";
	logo.style.zIndex="3"
	background.style.opacity="0";
	background.style.transition= "opacity 0.6s";
	background.style.zIndex="-1"
	horaire.style.transform= " translate(20vw, -20vh) scale(0.8) ";
	horaire.style.transition= "transform 0.6s";
	horaire.style.zIndex="3"
}
 else{
 	logo.style.transform= "scale(1)"
 	logo.style.transition= "transform 0.8s";
 	logo.style.zIndex="20"
 	background.style.opacity="1";
 	background.style.transition= "opacity 0.6s";
 	background.style.zIndex="8"
 	horaire.style.transform= "scale(1)";
	horaire.style.transition= "transform 0.6s";
	horaire.style.zIndex="20"

 }
});

