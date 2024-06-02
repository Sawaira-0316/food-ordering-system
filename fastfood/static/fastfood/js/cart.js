document.addEventListener('DOMContentLoaded', function() {
    var nam = document.querySelector("#name");
    var size = document.querySelector("#size");
    var price = document.querySelector("#price");
    var bill = document.querySelector("#total");
    var cartCount = document.querySelector("#cart");

    if (!nam || !size || !price || !bill || !cartCount) {
        console.error('Required elements not found');
        return;
    }

    // Initialize orders and total if not already
    var orders = JSON.parse(localStorage.getItem('orders')) || [];
    var total = parseFloat(localStorage.getItem('total')) || 0;

    function addItem(type, id) {
        var itemId = '#' + type + id;
        var name = document.querySelector(itemId).innerHTML;

        var radio = type + id;
        var pri = document.getElementsByName(radio);
        var size, price;
        if (pri[0].checked) {
            price = pri[0].value.trim();
            size = 'M';
        } else {
            price = pri[1].value.trim();
            size = 'L';
        }

        orders.push({ name: name, size: size, price: price });
        localStorage.setItem('orders', JSON.stringify(orders));

        total += parseFloat(price);
        localStorage.setItem('total', total);

        updateCartView();
    }

    function updateCartView() {
        nam.innerHTML = '<h3>Name</h3>';
        size.innerHTML = '<h3>Size</h3>';
        price.innerHTML = '<h3>Price</h3>';

        orders.forEach(function(order, index) {
            var removeButton = '<div style="display: inline-block; background-color: red; color: white; width: 20px; height: 20px; text-align: center; line-height: 20px; cursor: pointer; margin-left: 10px;" onclick="removeItem('+ index +')">X</div>';
            nam.innerHTML += '<h4>' + order.name + '</h4>';
            size.innerHTML += '<h4>' + order.size + '</h4>';
            price.innerHTML += '<h4>' + order.price + ' Rs' + removeButton + '</h4>';
        });

        bill.innerHTML = 'Total: ' + total.toFixed(2) + ' Rs';
        updateCartCount(orders.length);
    }

    function removeItem(index) {
        total -= parseFloat(orders[index].price);
        orders.splice(index, 1);

        localStorage.setItem('orders', JSON.stringify(orders));
        localStorage.setItem('total', total);

        updateCartView();
    }

    function updateCartCount(count) {
        cartCount.innerHTML = count;
    }

    // Make functions globally accessible
    window.addPizza = function(pid) { addItem('pizza', pid); };
    window.addBurger = function(bid) { addItem('burger', bid); };
    window.removeItem = removeItem;

    // Initialize cart view
    updateCartView();
});

function order() {
    var messageElement = document.getElementById('message');
    var order = localStorage.getItem('order');


    var msg = messageElement.value;  // Correctly capture the value from the input field
    var ur = '/fastfood/order/';   // Correct URL for your Django view
    var orderData = { 
        'note': msg,      // Send both note
        'order': order    // and order data
    };

    $.ajax({
        url: ur,
        type: "POST",
        data: orderData,
        success: function(data) {
            console.log("The data was sent");
            console.log(data);
            window.location.replace('/fastfood/success/'); // Redirect to success page on success
        },
        error: function(xhr, status, error) {
            console.error("An error occurred:", error);
        }
    });
}
