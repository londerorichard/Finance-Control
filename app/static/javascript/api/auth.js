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
        throw new Error(data.detail || "Registration failed");
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
        throw new Error(data.detail || "User couldn't be logged in");
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
        throw new Error(data.detail || "Could not get current user");
    }

    return data;
}