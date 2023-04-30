const menuBar= document.querySelector('#menu-bar');
const menuCnt=	document.querySelector('.menu-container');
const navLink=	document.querySelector('.nav-link-container');
const wifiIcon=	document.querySelector('#wifi');
const nav = document.querySelector("nav");


let i=0;

let icons=[
	'bx-wifi-0',
	'bx-wifi-1',
	'bx-wifi-2'];
	

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
	liveIcon.classList.remove(icons[i]);
		liveIcon.classList.remove(icons[i-1]);
		i--;	
	}
};

setInterval(liveicons,1000);
setInterval(liveicon,4000);

