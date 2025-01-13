window.addEventListener("load", display);

const logo = document.querySelector(".logo");
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

//-------------BACKGROUND_COLORS------EN--COURS--!------------

function couleurs(){
	let paragraphe = document.getElementsByClassName("paragraphe");
for(i=1; i<100; i++){
	paragraphe.style.backgroundColor = couleurs[i];
}

}


//-------------SCROLLEVENT------------------------
window.addEventListener('scroll', () => {
	if (window.scrollY > 200){
 	logo.style.transform= "translate(310px, -50px) scale(0.6) ";
	logo.style.transition= "transform 0.4s";
}
 else{
 	logo.style.transform= "scale(1) ";
 }
});

