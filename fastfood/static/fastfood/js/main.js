var hours = 24;
var now = new Date().getTime();
var stepTime = localStorage.getItem('stepTime');

console.log("Current time:", now);
console.log("Stored stepTime:", stepTime);

if (stepTime === null) {
    console.log("No stepTime found in localStorage. Setting it now.");
    localStorage.setItem('stepTime', now);
} else {
    stepTime = parseInt(stepTime, 10); // Convert stepTime to an integer
    if (now - stepTime > hours * 60 * 60 * 1000) {
        console.log("More than 24 hours passed. Clearing localStorage.");
        localStorage.clear();
        localStorage.setItem('stepTime', now);
    } else {
        console.log("Less than 24 hours passed.");
    }
}

var orders=JSON.parse(localStorage.getItem('orders'));
var total= localStorage.getItem('total');


if(orders === null || orders === undefined){
    localStorage.setItem('orders' , JSON.stringify([]));
    orders = JSON.parse(localStorage.getItem('orders'));
}

if(orders === null || orders === undefined){
    localStorage.setItem('total' , 0)
    total = localStorage.getItem('total');
}

var cart = document.querySelector("#cart");
cart.innerHTML= orders.length;