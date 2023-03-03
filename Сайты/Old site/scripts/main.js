let myButton = document.querySelector('button');
let myHeading = document.querySelector('h1');

function setUserName() {
	let userName = prompt('Введите ваше имя');
	if(!userName) {
    		setUserName();
	} else {
		localStorage.setItem('name', userName);
		myHeading.textContent = userName + ' пошел нахуй';
	};
}

if(!localStorage.getItem('name')) {
  setUserName();
} else {
  let storedName = localStorage.getItem('name');
  myHeading.textContent = storedName + ' пошел нахуй';
}

myButton.onclick = function() {
  setUserName();
}