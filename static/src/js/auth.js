const toSignUP = document.getElementById("id-to-signup");
const toLogIn = document.getElementById("id-to-login");
const signupForm = document.getElementById("signup-form");
const showLoginForm = document.getElementById("show-login-form");
const closeSignup = document.getElementById("close-signup-form");
const closeAll = document.getElementById("login-form");

toLogIn.addEventListener("click", function () {
    signupForm.classList.replace("flex", "hidden");
    showLoginForm.classList.replace("hidden", "flex");
});

toSignUP.addEventListener("click", function () {
    signupForm.classList.replace("hidden", "flex");
    showLoginForm.classList.replace("flex", "hidden");
});

closeSignup.addEventListener("click", () => {
    closeAll.classList.replace("flex", "hidden");
});