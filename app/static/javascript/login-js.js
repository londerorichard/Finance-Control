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
