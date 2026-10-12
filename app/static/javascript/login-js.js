import { loginUser } from "./api/auth.js";

function activateIconEye() {
    const boxes = document.querySelectorAll(".password-box");

    boxes.forEach((box) => {
        const input = box.querySelector("input");
        const button = box.querySelector(".toggle-password");
        const eye = box.querySelector(".icon-eye");
        const eyeOff = box.querySelector(".icon-eye-off");

        button.addEventListener("click", () => {
            const isHidden = input.type === "password";

            input.type = isHidden ? "text" : "password";

            eye.classList.toggle("hidden", !isHidden);
            eyeOff.classList.toggle("hidden", isHidden);
        });
    });
}
activateIconEye();

// ======================================
// ===========FORM VALIDATION============
// ======================================

function validateEmail() {
    const email = document.querySelector("#email").value;
    const confirmEmail = document.querySelector("#confirm-email").value;

    if (email.includes("@") && email.includes(".")) {
        if (confirmEmail === email) {
            console.log("Email Válido!")
        }
    } else {
        console.log("Email inválido!")
    }
}
validateEmail();


function setupLoginUser() {
    const loginBox = document.querySelector(".login-box");
    const errorBox = document.querySelector(".error-message");

    loginBox.addEventListener("submit", async (event) => {
        event.preventDefault();

        const email = loginBox.querySelector("#email").value;
        const password = loginBox.querySelector("#password").value;

        try {
            const data = await loginUser(email, password);

            console.log("SUCCESS:", data);

            loginBox.reset();
            errorBox.textContent = "";
        } catch (error) {
            console.error("Login failed:", error);
            errorBox.textContent = error.message;
        }
    });
}
setupLoginUser();
