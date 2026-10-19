export async function createCategory(newCategoryName, token) {
    const response = await fetch(
        "http://127.0.0.1:8000/categories/create",
        {
            method: "POST",
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                newCategoryName
            })
        }
    );

    const data = await response.json();

    if (!response.ok) {
        const message = typeof data.detail === "string"
            ? data.detail
            : "Could not create category";

        throw new Error(message);
    }

    return data;
}


export async function listCategories(token) {
    const response = await fetch(
        "http://127.0.0.1:8000/categories/list",
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
            : "Could not list category";

        throw new Error(message);
    }

    return data;
}


export async function getCategoryByName(categoryName, token) {
    const response = await fetch(
        `http://127.0.0.1:8000/categories/get-by-name?categoryName=${encodeURIComponent(categoryName)}`,
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
            : "Could not update category";

        throw new Error(message);
    }

    return data;
}


export async function getCategoryById(category_id, token) {
    const response = await fetch(
        `http://127.0.0.1:8000/categories/get-by-id/${encodeURIComponent(category_id)}`,
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
            : "Could not update category";

        throw new Error(message);
    }

    return data;
}


export async function updateCategory(category_id, token, categoryUpdated) {
    const response = await fetch(
        `http://127.0.0.1:8000/categories/update-category/${encodeURIComponent(category_id)}`,
        {
            method: "PUT",
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify(categoryUpdated)
        }
    );

    const data = await response.json();

    if (!response.ok) {
        const message = typeof data.detail === "string"
            ? data.detail
            : "Could not update category";

        throw new Error(message);
    }

    return data;
}


export async function deleteCategory(category_id, token) {
    const response = await fetch(
        `http://127.0.0.1:8000/categories/delete-category/${encodeURIComponent(category_id)}`,
        {
            method: "DELETE",
            headers: {
                "Authorization": `Bearer ${token}`,
            }
        }
    );

    const data = await response.json();

    if (!response.ok) {
        const message = typeof data.detail === "string"
            ? data.detail
            : "Could not delete category";

        throw new Error(message);
    }

    return data;
}


