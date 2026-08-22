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
// ==============PASSWORD================
// ======================================

function hasMinLength(password) {
    return password.length >= 8;
}

function hasUppercase(password) {
    return /[A-Z]/.test(password);
}

function hasNumber(password) {
    return /[0-9]/.test(password);
}

function hasSpecialChar(password) {
    return /[!@#$%^&*(),.?":{}|<>_\-+=/\\[\]]/.test(password);
}

function validatePassword(password) {
    if (!password.trim()) return false;

    return (
        hasMinLength(password) &&
        hasUppercase(password) &&
        hasNumber(password) &&
        hasSpecialChar(password)
    );
}

function validateConfirmPassword(password, confirmPassword) {
    if (!validatePassword(password)) {
        return "Senha inválida";
    }

    if (password !== confirmPassword) {
        return "As senhas não coincidem";
    }

    return null;
}


function getPasswordRules(password) {
    return [
        {
            element: document.querySelector("#minLengthUI"),
            valid: hasMinLength(password),
            text: "8+ Caracteres"
        },
        {
            element: document.querySelector("#uppercaseUI"),
            valid: hasUppercase(password),
            text: "1+ Letra maiúscula"
        },
        {
            element: document.querySelector("#numberUI"),
            valid: hasNumber(password),
            text: "1+ Número"
        },
        {
            element: document.querySelector("#specialCharUI"),
            valid: hasSpecialChar(password),
            text: "1+ Caracter especial"
        }
    ];
}

function checklistValidation(password) {
    const rules = getPasswordRules(password);
    const checklist = document.querySelector(".checklist-validation");

    if (password.length === 0) {
        checklist.classList.add("hidden");

        rules.forEach(rule => {
            rule.element.style.color = "";
            rule.element.textContent = `• ${rule.text}`;
        });

        return;
    }

    checklist.classList.remove("hidden");

    rules.forEach(rule => {
        rule.element.style.color = rule.valid ? "green" : "";
        rule.element.textContent = `${rule.valid ? "✓" : "✗"} ${rule.text}`;
    });
    
}

function uploadCheckValidation() {
    const passwordInput = document.querySelector("#password");

    passwordInput.addEventListener("input", (event) => {
        const password = event.target.value;
        checklistValidation(password);
    });
}
uploadCheckValidation()



// ======================================
// ===============SUBMIT=================
// ======================================

function setupRegisterForm() {
    const registerForm = document.querySelector(".login-box-register");
    const errorBox = document.querySelector(".error-message");

    if (!registerForm || !errorBox) return;

    registerForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const email = document.querySelector("#email").value;
        const password = document.querySelector("#password").value;
        const confirmPassword = document.querySelector("#confirm-password").value;

        // Password validation
        const error = validateConfirmPassword(
            password,
            confirmPassword
        );

        if (error) {
            errorBox.textContent = error;
            return;
        }

        errorBox.textContent = "";

        try {
            const response = await fetch(
                "http://127.0.0.1:8000/auth/register",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        email: email,
                        password: password
                    })
                }
            );

            const data = await response.json();

            if (!response.ok) {
                errorBox.textContent = data.detail;
                return;
            }

            console.log("SUCCESS:", data);

            registerForm.reset();

        } catch (error) {
            console.error("Request failed:", error);
            errorBox.textContent = "Could not connect to the server.";
        }
    });
}

setupRegisterForm();