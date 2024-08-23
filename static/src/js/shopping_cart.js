let cart = document.getElementById("cart");

const shoppingCart = document.getElementById("shopping-cart");
const orderForm = document.getElementById("order-form");
const closeSale = document.getElementById("close-sale");

const cartBtns = document.querySelectorAll(".cart-btns");
const orderTable = document.getElementById("order-table");

const submitOrders = document.getElementById("submit-orders");

const showOrderinfo = document.getElementById("show-order-info");
const orderInfo = document.getElementById("order-info");
const closeInfo = document.getElementById("close-info");

let records = [];
let total = 0



cartBtns.forEach((btn, i) => {
    btn.addEventListener("click", () => {
        let data = `${btn.previousElementSibling.value}`.split(',');
        records.push({
            id: parseInt(data[0]),
            product: data[1],
            quantity: 1,
            amount: data[2]
        });
        total += parseFloat(data[2]);
        cart.textContent = records.length;

    });
});


shoppingCart.addEventListener("click", () => {
    orderForm.classList.replace("hidden", "flex");
    formatTable();
    const minus = document.querySelectorAll(".minus");
    const plus = document.querySelectorAll(".plus");
    const quantities = document.querySelectorAll(".quantities");
    const subtotal = document.querySelectorAll(".subtotal");
    const totalRecord = document.getElementById("record-total");

    // calculate the additions from the records
    for (const key in plus) {
        if (Object.prototype.hasOwnProperty.call(plus, key)) {
            const element = plus[key];
            element.addEventListener("click", () => {
                records[key].quantity += 1;
                quantities[key].textContent = records[key].quantity;
                subtotal[key].textContent = (records[key].amount * records[key].quantity).toFixed(2);

                totalRecord.textContent = (records.reduce((acc, el) => {
                    return acc += el.amount * el.quantity;
                }, 0)).toFixed(2);
                //console.log(currentTotal);
            });
        }
    }

    // calculate substractions from the records
    for (const key in minus) {
        if (Object.prototype.hasOwnProperty.call(minus, key)) {
            const element = minus[key];
            element.addEventListener("click", () => {
                if (records[key].quantity > 1) {
                    records[key].quantity -= 1;
                    quantities[key].textContent = records[key].quantity;
                    subtotal[key].textContent = (records[key].amount * records[key].quantity).toFixed(2);
                    totalRecord.textContent = (records.reduce((acc, el) => {
                        return acc += el.amount * el.quantity;
                    }, 0)).toFixed(2);
                }

            });
        }
    }
});

closeSale.addEventListener("click", () => {
    records = [];
    cart.textContent = records.length;
    total = 0.00
    orderForm.classList.replace("flex", "hidden");
});

const formatTable = () => {
    let rows = "";
    records.forEach((record, i) => {
        rows += `
        <tr class="bg-white border-t hover:bg-gray-100">
            <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">${i + 1}</th>
            <td class="px-6 py-4 whitespace-nowrap">${record.product}</td>
            <td class="px-6 py-4 md:text-center">${record.amount}</td>
            <td class="px-6 py-4 flex place-items-center place-content-center md:text-center">
                <button class="minus transition text-2xl cursor-pointer font-bold text-gray-600 mx-2 px-4 bg-white border rounded active:scale-90 ">&minus;</button>
                <span class="quantities text-lg text-black ">${record.quantity}</span>
                <button class="plus text-2xl font-bold text-emerald-600 mx-2 cursor-pointer px-4 bg-white border rounded transition-all active:scale-90">&plus;</button>
            </td>
            <td class="whitespace-nowrap px-6 py-4 md:text-center">Price: Gh&cent; 
            <span class="subtotal">${record.amount}</span></td>
        </tr>
    `;
    });

    rows += `<tr class="border-t bg-gray-800 text-white">
        <th scope="row" class="px-6 py-4 font-medium uppercase text-white whitespace-nowrap" colspan="4">Total</th>
        <td class="px-6 py-4 whitespace-nowrap md:text-center">Price: Gh&cent; <span id="record-total">${total.toFixed(2)}</span></td>
    </tr>
    `;
    orderTable.innerHTML = rows;
}

submitOrders.addEventListener("click", async () => {
    if (records.length !== 0) {
        try {
            let res = await fetch("/place-orders",
                {
                    method: "POST",
                    credentials: "same-origin",
                    mode: "cors",
                    headers: {
                        "X-CSRFToken": getCookie("csrftoken"),
                        "Accept": "application/json",
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(records),
                }
            );
            let data = await res.json();

            const message = data.message;
            records = [];
            cart.textContent = records.length;
            total = 0.00
            orderForm.classList.replace("flex", "hidden");
            showOrderInfo(message)
        } catch (error) {
            console.log(error);
        }
    } else {
        orderForm.classList.replace("flex", "hidden");
        const message = "Order list must not be empty";
        showOrderInfo(message)
    }
});

function getCookie(name) {
    //getting the csrftoken from jquery
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.
                    length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const showOrderInfo = (message) => {
    showOrderinfo.classList.replace("hidden", "flex");
    orderInfo.textContent = message;
}

closeInfo.addEventListener("click", () => {
    showOrderinfo.classList.replace("flex", "hidden");
})