

const loginForm = document.getElementById("login-form");
const closeForm = document.getElementById("close-form");
const openLogin = document.getElementById("open-login");



closeForm.addEventListener("click", () => {
    loginForm.classList.replace("flex", "hidden");
});

openLogin.addEventListener("click", () => {
    loginForm.classList.replace("hidden", "flex");
})
