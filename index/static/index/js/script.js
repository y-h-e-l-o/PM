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
	if ( window.scrollY > 50){
 	logo.style.transform= " scale(0.3) translate(-95vw, -85vh) ";
	logo.style.transition= "transform 0.7s";
	background.style.bottom="-110vh";
	background.style.transition= "bottom 0.7s";
	horaire.style.transform= " translate(20vw, -20vh) scale(0.8) ";
	horaire.style.transition= "transform 0.6s";
}
 else{
 	logo.style.transform= "scale(1)"
 	logo.style.transition= "transform 0.7s";
 	background.style.bottom="0px";
 	background.style.transition= "bottom 0.7s";
 	horaire.style.transform= "scale(1)";
	horaire.style.transition= "transform 0.6s";

 }
});

