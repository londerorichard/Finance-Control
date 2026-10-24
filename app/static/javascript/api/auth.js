export async function registerUser(email, password) {
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
        const message = typeof data.detail === "string"
            ? data.detail
            : "Registration failed";

        throw new Error(message);
    }

    return data;
}


export async function loginUser(email, password) {
    const response = await fetch(
        "http://127.0.0.1:8000/auth/login",
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
        const message = typeof data.detail === "string"
            ? data.detail
            : "User coundn't be logged in";

        throw new Error(message);
    }

    return data;
}


export async function getCurrentUser(token) {
    const response = await fetch(
        "http://127.0.0.1:8000/auth/me",
        {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${token}`
            }
        }
    );

    const data = await response.json();

    if (!response.ok) {
        const message = typeof data.detail === "string"
            ? data.detail
            : "Could not get current user";

        throw new Error(message);
    }

    return data;
}


export async function changePassword(current_password, new_password, token) {
    if (new_password.length < 8) {
        throw new Error("The new password must contain at least 8 characters.");
    }

    const response = await fetch("http://127.0.0.1:8000/auth/change-password", {
        method: "PUT",
        headers: {
            "Authorization": `Bearer ${token}`,
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            current_password,
            new_password
        })
    });

    const data = await response.json();

    if (!response.ok) {
        const message = typeof data.detail === "string"
            ? data.detail
            : "Could not change password";

        throw new Error(message);
    }

    return data;
}


export function googleLogin() {
    window.location.href = "http://127.0.0.1:8000/auth/google";
}

