document.addEventListener('DOMContentLoaded', function() {
    var pcart = document.querySelector('#pcart');
    var ptotal = document.querySelector('#ptotal');
    var cartCount = document.querySelector("#cart");

    // Check if elements exist
    if (!pcart || !ptotal || !cartCount) {
        console.error('Cart, total elements, or cart count element not found');
        return;
    }

    // Initialize orders and total if not already
    var orders = JSON.parse(localStorage.getItem('orders')) || [];
    var total = localStorage.getItem('total') || 0;

    pshoppingCart();

    function addPizza(pid) {
        // get pizza name
        var pizzaId = '#piz' + pid;
        var name = document.querySelector(pizzaId).innerHTML;

        // get pizza price
        var radio = 'pizza' + pid;
        var pri = document.getElementsByName(radio);
        var size, price;
        if (pri[0].checked) {
            price = pri[0].value.trim();
            size = 'M';
        } else {
            price = pri[1].value.trim();
            size = 'L';
        }

        // Add new order
        orders.push({ name: name, size: size, price: price });
        localStorage.setItem('orders', JSON.stringify(orders));

        // Update total
        total = Number(total) + Number(price);
        localStorage.setItem('total', total);

        // Update cart display
        pshoppingCart();
    }

    function pshoppingCart() {
        pcart.innerHTML = '';
        orders.forEach(function(order, index) {
            var butto = '<div style="position: relative; right: 30px; background-color: red; color: white; width: 30px; height: 20px; text-align: center; line-height: 20px; cursor: pointer;" onclick="removePizza('+ index +')">X</div>';
            pcart.innerHTML += '<li>' + order.name + ' ' + order.size + ': ' + order.price + ' Rs' + butto + '</li>';
        });

        ptotal.innerHTML = 'Total: ' + total + ' Rs';
        
        // Update cart count
        updateCartCount(orders.length);
    }

    function removePizza(n) {
        total = Number(total) - Number(orders[n].price);
        orders.splice(n, 1);

        // Update total and orders in localStorage
        localStorage.setItem('orders', JSON.stringify(orders));
        localStorage.setItem('total', total);

        // Update cart display
        pshoppingCart();
    }

    function updateCartCount(count) {
        cartCount.innerHTML = count;
    }

    // Make addPizza globally accessible
    window.addPizza = addPizza;
    window.removePizza = removePizza;
});
