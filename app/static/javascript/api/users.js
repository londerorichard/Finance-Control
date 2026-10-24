export async function getuserById(user_id, token) {
    const response = await fetch(
        `http://127.0.0.1:8000/users/get-by-id/${encodeURIComponent(user_id)}`,
        {
            method: "GET",
            credentials: "include",
            headers: {
                "Authorization": `Bearer ${token}`
            }
        }
    );

    const data = await response.json();

    if (!response.ok) {
        const message = typeof data.detail === "string"
            ? data.detail
            : "Could not find user";

        throw new Error(message);
    }

    return data;
}


export async function updateUserProfile(email, token) {
    const response = await fetch(
        "http://127.0.0.1:8000/users/update",
        {
            method: "POST",
            credentials: "include",
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: email
            })
        }
    );

    const data = await response.json();

    if (!response.ok) {
        const message = typeof data.detail === "string"
            ? data.detail
            : "Could not update user profile";

        throw new Error(message);
    }

    return data;
}


export async function deleteProfile(token) {
    const response = await fetch(
        "http://127.0.0.1:8000/users/delete_profile",
        {
            method: "DELETE",
            credentials: "include",
            headers: {
                "Authorization": `Bearer ${token}`
            }
        }   
    );

    const data = await response.json();

    if (!response.ok) {
        const message = typeof data.detail === "string"
            ? data.detail
            : "Could not delete user profile";

        throw new Error(message);
    }

    return data;
}