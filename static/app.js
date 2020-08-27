const BASE_URL = "http://127.0.0.1:5000/api/cupcakes";
const search = document.getElementById("flavor-search");
const form = document.getElementById("new-cupcake-form");
showAllCupcakes();

search.addEventListener("keyup", showAllCupcakes);

async function showAllCupcakes() {
    list = document.getElementById("cupcakes-list");
    list.innerHTML = "";
    cupcakes = await getCupcakes();

    for (let cupcake of cupcakes) {
        div = document.createElement("div");
        div.innerHTML = `<img style="width: 50px"src="${cupcake.image}">
        <ul>
            <li>Flavor: ${cupcake.flavor}
                <ul>
                    <li>Rating: ${cupcake.rating}</li>
                    <li>Size: ${cupcake.size}</li>
                </ul>
            </li>
        <ul>`;
        list.append(div);
    }
}

async function getCupcakes() {
    data = search.value;
    const response = await axios.get(`${BASE_URL}`, { params: { data } });
    return response.data.cupcakes;
}

form.addEventListener("submit", function(evt) {
    evt.preventDefault();
    addCupcake({
        flavor: event.target[1].value,
        image: event.target[2].value,
        rating: event.target[3].value,
        size: event.target[4].value
    });
});

async function addCupcake(obj) {
    await axios.post(`${BASE_URL}`, obj);
    showAllCupcakes();
}