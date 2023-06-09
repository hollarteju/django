const menuBar= document.querySelector('#menu-bar');
const menuCnt=	document.querySelector('.menu-container');
const navLink=	document.querySelector('.nav-link-container');
const wifiIcon=	document.querySelector('#wifi');
const nav = document.querySelector("nav");
const navHref = document.querySelectorAll(".nav-link a");
const popUpMsg= document.querySelector(".pop-up-message");


let i=0;

let icons=[
	'bx-wifi-0',
	'bx-wifi-1',
	'bx-wifi-2'];

	navHref.forEach(href=>{
		href.addEventListener("click", ()=>{
			menuBar.classList.remove('bx-x');
	menuCnt.classList.remove('menu-active');
	navLink.classList.remove('nav-link-active');
		})
	});

menuBar.onclick=()=>{	
	menuBar.classList.toggle('bx-x');
	menuCnt.classList.toggle('menu-active');
	navLink.classList.toggle('nav-link-active');
};


	const liveicons=()=>{
	if(i < 3){
 wifiIcon.classList.add(icons[i]);
	i++;
	}
};

	const liveicon=()=>{
	if(i>0){
	i--;
	wifiIcon.classList.remove(icons[i]);
		wifiIcon.classList.remove(icons[i-1]);
		i--;	
	}
};

function back(){
	if(window.scrollY > 900 && window.scrollY < 2600 && window.innerWidth > 215){
		nav.classList.add("nav-active")	
	}
	else{
		nav.classList.remove("nav-active")	
	}
};

const pop=()=>{
	popUpMsg.classList.add("remove-pop")
};

window.addEventListener("scroll",back);

setInterval(liveicons,1000);
setInterval(liveicon,4000);
setInterval(pop,4000);

