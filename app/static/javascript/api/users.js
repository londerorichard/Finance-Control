export async function updateUserProfile(email) {
    const response = await fetch(
        "http://127.0.0.1:8000/users/update",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: email
            })
        }
    );

    const data = await response.json();

    if (!response.ok) {
        throw new Error(data.detail || "Could not update user profile");
    }

    return data;
}


export async function deleteProfile() {
    const response = await fetch(
        "http://127.0.0.1:8000/users/delete_profile",
        {
            method: "DELETE",
            headers: {
                "Authorization": `Bearer ${token}`
            }
        }   
    );

    const data = await response.json();

    if (!response.ok) {
        throw new Error(data.detail || "Coud not delete user profile");
    }

    return data;
}