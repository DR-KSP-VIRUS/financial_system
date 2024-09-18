const myOrderTable = document.getElementById("my-order-table");

document.addEventListener("DOMContentLoaded", async () => {
    const getOrders = async () => {
        let orders = await fetch("/my-orders-json")
        return orders.json();
    }
    let results = await getOrders();
    console.log(results.orders);

    const formatTable = () => {
        let rows = "";
        let total = 0.0;
        results.orders.forEach((record, i) => {
            total += (record.product__price * record.quantity);
            rows += `
                <tr class="bg-white border-t hover:bg-gray-100">
                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">${i + 1}</th>
                    <td class="px-6 py-4 whitespace-nowrap">${record.product__product_name}</td>
                    <td class="px-6 py-4 md:text-center">${record.product__price}</td>
                    <td class="px-6 py-4 flex place-items-center place-content-center md:text-center">
                    <span class="quantities text-lg text-black ">${record.quantity}</span>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap md:text-center">${record.created}</td>
                    <td class="whitespace-nowrap px-6 py-4 md:text-center">Price: Gh &cent; 
                        <span class="subtotal">${(record.product__price * record.quantity).toFixed(2)}</span>
                    </td>
                </tr>
            `;
        });

        rows += `
        <tr class="border-t bg-gray-800 text-white">
            <th scope="row" class="px-6 py-4 font-medium uppercase text-white whitespace-nowrap" colspan="5">Total</th>
            <td class="px-6 py-4 whitespace-nowrap md:text-center">Price: Gh&cent; <span id="record-total">${total.toFixed(2)}</span></td>
        </tr>
        `;
        myOrderTable.innerHTML = rows;
    }

    formatTable();
});