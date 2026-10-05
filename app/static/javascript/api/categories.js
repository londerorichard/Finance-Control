export async function createCategory(newCategoryName) {
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
        throw new Error(data.detail || "Could not create new category");
    }

    return data;
}


export async function listCategories() {
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
        throw new Error(data.detail || "Could not list categories");
    }

    return data;
}


export async function getCategoryByName(categoryName) {
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
        throw new Error(data.detail || "Could not get category");
    }

    return data;
}