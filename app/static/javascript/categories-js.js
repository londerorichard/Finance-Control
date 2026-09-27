const defaultCategories = [
    {
        name: "Food",
        subcategories: ["Groceries", "Restaurants", "Delivery", "Snacks"]
    },
    {
        name: "Transport",
        subcategories: ["Fuel", "Public Transport", "Uber", "Parking"]
    },
    {
        name: "Housing",
        subcategories: ["Rent", "Electricity", "Water", "Internet"]
    },
    {
        name: "Health",
        subcategories: ["Medicine", "Doctor", "Dentist"]
    },
    {
        name: "Education",
        subcategories: ["Tuition", "Courses", "Books"]
    },
    {
        name: "Entertainment",
        subcategories: ["Movies", "Games", "Streaming"]
    },
    {
        name: "Shopping",
        subcategories: ["Clothing", "Electronics", "Personal Care"]
    },
    {
        name: "Family",
        subcategories: ["Children", "Gifts", "Family Support"]
    },
    {
        name: "Services",
        subcategories: ["Subscriptions", "Cloud Services"]
    },
    {
        name: "Financial",
        subcategories: ["Bank Fees", "Loans", "Credit Card"]
    },
    {
        name: "Leisure",
        subcategories: ["Travel", "Hobbies", "Sports"]
    }
];


const categoryTemplate = document.querySelector("#category-template");
const subcategoryTemplate = document.querySelector("#subcategory-template");
const categoriesList = document.querySelector(".categories-list");


function createSubcategory(name) {

    const subcategory = subcategoryTemplate.content.cloneNode(true);

    const title = subcategory.querySelector(".category-title");

    title.textContent = name;

    return subcategory;
}


function createCategory(categoryData) {

    const category = categoryTemplate.content.cloneNode(true);

    const title = category.querySelector(".category-title");
    const subcategoriesList = category.querySelector(".subcategories");

    title.textContent = categoryData.name;

    categoryData.subcategories?.forEach(subcategoryName => {

        const subcategory = createSubcategory(subcategoryName);

        subcategoriesList.append(subcategory);
    });

    return category;
}


function generateCategories() {

    defaultCategories.forEach(categoryData => {

        const category = createCategory(categoryData);

        categoriesList.append(category);
    });
}


generateCategories();


// Reusable pallete color
function createColorOptions(palette, onColorSelected) {
    const colors = [

        "#FF0000", "#FF4000", "#FF8000", "#FFBF00", "#FFFF00", "#BFFF00",
        "#80FF00", "#40FF00", "#00FF00", "#00FF40", "#00FF80", "#00FFBF",
        "#00FFFF", "#00BFFF", "#0080FF", "#0040FF", "#0000FF", "#4000FF",
        "#8000FF", "#BF00FF", "#FF00FF", "#FF00BF", "#FF0080", "#FF0040",
        "#800000", "#804000", "#808000", "#408000", "#008000", "#008040",
        "#008080", "#004080", "#000080", "#400080", "#800080", "#800040",
        "#000000", "#202020", "#404040", "#606060", "#808080", "#A0A0A0",
        "#C0C0C0", "#D0D0D0", "#E0E0E0", "#F0F0F0", "#F8F8F8", "#FFFFFF",
        "#8B4513", "#A0522D", "#CD853F", "#DEB887", "#F5DEB3", "#FFE4C4"

    ];

    colors.forEach(color => {

        const colorOption =
            document.createElement("button");

        colorOption.type = "button";

        colorOption.classList.add("color-option");

        colorOption.style.backgroundColor = color;

        palette.appendChild(colorOption);


        colorOption.addEventListener("click", () => {

            onColorSelected(color);

        });
    });
}

function closeAllColorPalettes() {

    document
        .querySelectorAll(".color-palette, .edit-color-palette")
        .forEach(palette => {

            palette.classList.remove("open");
            palette.classList.add("hidden");

        });
}


function setupColorPalettes() {

    const categoryItems =
        document.querySelectorAll(".category, .subcategory");


    categoryItems.forEach(category => {

        const header =
            category.querySelector(".category-header");

        const button =
            header.querySelector(".category-main");

        const palette =
            header.querySelector(".color-palette");

        const iconContainer =
            category.querySelector(".icon-container");


        if (!button || !palette) {
            return;
        }


        // Create the color options
        createColorOptions(palette, color => {

            // Change button color
            button.style.backgroundColor = color;

            // Change icon container color
            if (iconContainer) {
                iconContainer.style.backgroundColor = color;
            }

            // Close palette
            palette.classList.remove("open");
        });


        // Open / close palette
        button.addEventListener("click", event => {

            event.stopPropagation();

            const isOpen =
                palette.classList.contains("open");

            closeAllColorPalettes();

            if (!isOpen) {
                palette.classList.add("open");
            }
        });

    });


    // Close palettes when clicking outside
    document.addEventListener("click", event => {

        if (
            !event.target.closest(".category-header") &&
            !event.target.closest(".color-palette")
        ) {

            document
                .querySelectorAll(".color-palette")
                .forEach(palette => {

                    palette.classList.remove("open");

                });
        }
    });
}

setupColorPalettes();


function setupOpenSubcategories() {

    const categories = document.querySelectorAll(".category");

    categories.forEach(category => {

        const tagBtn = category.querySelector(".category-tag");

        const subcategories =
            category.querySelector(".subcategories-container");

        const settingsPanel =
            category.querySelector(".settings-dropdown");

        if (!tagBtn || !subcategories) {
            return;
        }

        tagBtn.addEventListener("click", event => {

            event.stopPropagation();

            // Close settings in THIS category
            if (settingsPanel) {
                settingsPanel.classList.add("hidden");
            }

            // Close subcategories in OTHER categories
            categories.forEach(otherCategory => {

                const otherSubcategories =
                    otherCategory.querySelector(".subcategories-container");

                if (
                    otherSubcategories &&
                    otherSubcategories !== subcategories
                ) {
                    otherSubcategories.classList.add("hidden");
                }
            });

            // Toggle this category's subcategories
            subcategories.classList.toggle("hidden");
        });
    });

    // Close subcategories when clicking somewhere else
    document.addEventListener("click", event => {

        categories.forEach(category => {

            const subcategories =
                category.querySelector(".subcategories-container");

            const tagBtn =
                category.querySelector(".category-tag");

            if (
                subcategories &&
                !subcategories.contains(event.target) &&
                !tagBtn.contains(event.target)
            ) {
                subcategories.classList.add("hidden");
            }
        });
    });

}

setupOpenSubcategories();


function setupCategoriesSettings() {

    const categories = document.querySelectorAll(".category");

    categories.forEach(category => {

        const categorySettingsBtn =
            category.querySelector(":scope > .category-options > .category-settings");

        const settingsPanel =
            category.querySelector(":scope > .category-options > .settings-dropdown");

        const subcategories =
            category.querySelector(":scope > .category-options .subcategories-container");

        if (!categorySettingsBtn || !settingsPanel) {
            return;
        }

        categorySettingsBtn.addEventListener("click", event => {

            event.stopPropagation();

            if (subcategories) {
                subcategories.classList.add("hidden");
            }

            categories.forEach(otherCategory => {

                const otherPanel =
                    otherCategory.querySelector(
                        ":scope > .category-options > .settings-dropdown"
                    );

                if (otherPanel && otherPanel !== settingsPanel) {
                    otherPanel.classList.add("hidden");
                }
            });

            settingsPanel.classList.toggle("hidden");
        });
    });

    // Close settings when clicking somewhere else
    document.addEventListener("click", event => {

        categories.forEach(category => {

            const settingsPanel =
                category.querySelector(
                    ":scope > .category-options > .settings-dropdown"
                );

            const settingsButton =
                category.querySelector(
                    ":scope > .category-options > .category-settings"
                );

            if (
                settingsPanel &&
                !settingsPanel.contains(event.target) &&
                !settingsButton.contains(event.target)
            ) {
                settingsPanel.classList.add("hidden");
            }
        });
    });
}

setupCategoriesSettings();


function applyEditCategoryColor(
    color,
    colorPickerBtn,
    category
) {
    colorPickerBtn.style.backgroundColor = color;

    const iconContainer =
        category.querySelector(".icon-container");

    if (iconContainer) {
        iconContainer.style.backgroundColor = color;
    }
}


function setupIconPicker() {

    const icons = [
        "utensils",
        "shopping-cart",
        "car",
        "home",
        "coffee",
        "gamepad-2",
        "heart",
        "briefcase",
        "plane",
        "gift",
        "music",
        "book-open",
        "dumbbell",
        "shirt",
        "dog",
        "paw-print"
    ];

    const panel =
        document.querySelector(".icon-picker-panel");

    if (!panel) {
        return;
    }

    icons.forEach(icon => {

        const button =
            document.createElement("button");

        button.type = "button";
        button.classList.add("icon-option");
        button.dataset.icon = icon;

        button.innerHTML =
            `<i data-lucide="${icon}"></i>`;

        panel.appendChild(button);
    });

    lucide.createIcons();
}

setupIconPicker();


let categoryBeingEdited = null;

let editedCategoryName = null;
let editedCategoryColor = null;
let editedCategoryIcon = null;


function setupEditCategory() {

    const categories =
        document.querySelectorAll(".category");

    const editCategoryPanel =
        document.querySelector(".edit-category");

    const input =
        editCategoryPanel.querySelector(".edit-category-input");

    const colorPickerBtn =
        editCategoryPanel.querySelector(".collor-picker-btn");

    const colorPalette =
        editCategoryPanel.querySelector(".edit-color-palette");

    const iconPickerBtn =
        editCategoryPanel.querySelector(".icon-picker-btn");

    const iconPickerPanel =
        editCategoryPanel.querySelector(".icon-picker-panel");

    const saveChanges =
        editCategoryPanel.querySelector(".save-category-edition");

    const cancelChanges =
        editCategoryPanel.querySelector(".cancel-category-edition");


    // Create color options once

    createColorOptions(colorPalette, color => {

        if (!categoryBeingEdited) {
            return;
        }

        // Change only the temporary value
        editedCategoryColor = color;

        // Update both picker buttons
        colorPickerBtn.style.backgroundColor = color;
        iconPickerBtn.style.backgroundColor = color;

        colorPalette.classList.add("hidden");
    });


    // Setup Edit buttons

    categories.forEach(category => {

        const editCategoryBtn =
            category.querySelector(
                ":scope > .category-options > .settings-dropdown > .edit-option-btn"
            );

        if (!editCategoryBtn) {
            return;
        }


        editCategoryBtn.addEventListener("click", event => {

            event.stopPropagation();

            categoryBeingEdited = category;


            // Get current category name

            const categoryTitle =
                category.querySelector(".category-title");

            editedCategoryName =
                categoryTitle.textContent;

            input.value =
                editedCategoryName;


            // Get current category color
            // The icon-container is the source of truth

            const iconContainer =
                category.querySelector(".icon-container");

            if (iconContainer) {

                editedCategoryColor =
                    getComputedStyle(iconContainer).backgroundColor;

                colorPickerBtn.style.backgroundColor =
                    editedCategoryColor;

                iconPickerBtn.style.backgroundColor =
                    editedCategoryColor;
            }


            // Get current category icon

            const categoryIcon =
                category.querySelector(".icon-container svg");

            if (categoryIcon) {

                editedCategoryIcon =
                    categoryIcon.getAttribute("data-lucide");

                iconPickerBtn.innerHTML = "";

                const pickerIcon =
                    categoryIcon.cloneNode(true);

                iconPickerBtn.appendChild(pickerIcon);

                lucide.createIcons();
            }


            // Close pickers when opening modal

            colorPalette.classList.add("hidden");

            iconPickerPanel.classList.add("hidden");


            // Show edit modal

            editCategoryPanel.showModal();



            // Hide settings panel when one option is clicked

            const settingsPanel = category.querySelector(
                ":scope > .category-options > .settings-dropdown"
            );

            settingsPanel.classList.add("hidden");

        });
    });


    // Update temporary name

    input.addEventListener("input", () => {

        editedCategoryName =
            input.value;
    });


    // Open / close edit color picker

    colorPickerBtn.addEventListener("click", event => {

        event.stopPropagation();

        const isHidden =
            colorPalette.classList.contains("hidden");

        closeAllColorPalettes();

        iconPickerPanel.classList.add("hidden");

        if (isHidden) {
            colorPalette.classList.remove("hidden");
        }
        
    });


    // Close edit color picker when clicking outside

    document.addEventListener("click", event => {

        if (
            !colorPalette.contains(event.target) &&
            !colorPickerBtn.contains(event.target)
        ) {
            colorPalette.classList.add("hidden");
        }
    });


    // Open / close edit icon picker

    iconPickerBtn.addEventListener("click", event => {
        event.stopPropagation();

        const isHidden = iconPickerPanel.classList.contains("hidden");

        colorPalette.classList.add("hidden");

        if (isHidden) {
            iconPickerPanel.classList.remove("hidden");
        }
    });


    // Icon selection

    iconPickerPanel.addEventListener("click", event => {

        const iconOption =
            event.target.closest(".icon-option");

        if (!iconOption) {
            return;
        }

        editedCategoryIcon =
            iconOption.dataset.icon;


        // Show selected icon in modal

        iconPickerBtn.innerHTML = "";

        const selectedIcon =
            document.createElement("i");

        selectedIcon.setAttribute(
            "data-lucide",
            editedCategoryIcon
        );

        iconPickerBtn.appendChild(selectedIcon);

        lucide.createIcons();

        iconPickerPanel.classList.add("hidden");
    });


    // Close edit icon picker when clicking outside

    document.addEventListener("click", event => {

        if (
            !iconPickerPanel.contains(event.target) &&
            !iconPickerBtn.contains(event.target)
        ) {
            iconPickerPanel.classList.add("hidden");
        }
    });


    // SAVE

    saveChanges.addEventListener("click", event => {

        event.stopPropagation();

        if (!categoryBeingEdited) {
            return;
        }


        // Apply name

        const categoryTitle =
            categoryBeingEdited.querySelector(".category-title");

        categoryTitle.textContent =
            editedCategoryName;


        // Apply color

        applyEditCategoryColor(
            editedCategoryColor,
            colorPickerBtn,
            categoryBeingEdited
        );


        // Apply icon

        if (editedCategoryIcon) {

            const categoryIconContainer =
                categoryBeingEdited.querySelector(
                    ".icon-container"
                );

            categoryIconContainer.innerHTML = "";

            const newIcon =
                document.createElement("i");

            newIcon.setAttribute(
                "data-lucide",
                editedCategoryIcon
            );

            categoryIconContainer.appendChild(newIcon);

            lucide.createIcons();
        }


        // Close modal

        editCategoryPanel.close();

        categoryBeingEdited = null;
        editedCategoryName = null;
        editedCategoryColor = null;
        editedCategoryIcon = null;
    });


    // CANCEL

    cancelChanges.addEventListener("click", event => {

        event.stopPropagation();

        // Nothing needs to be restored because
        // the real category was never modified.

        editCategoryPanel.close();

        categoryBeingEdited = null;
        editedCategoryName = null;
        editedCategoryColor = null;
        editedCategoryIcon = null;
    });
}

setupEditCategory();


let categoryBeingRemoved = null;

function setupRemoveCategory() {

    const categories = document.querySelectorAll(".category");

    const removePanel =
        document.querySelector(".remove-panel");

    const removeCategoryName =
        document.querySelector(".remove-category-name");

    const chooseCategoryRemoveBtn =
        document.querySelector(".choose-category-remove");

    const defaultCategoryRemoveBtn =
        document.querySelector(".default-remove-category");

    const cancelCategoryRemoveBtn =
        document.querySelector(".cancel-remove-category");

    const chooseCategoriesPanel =
        document.querySelector(".safe-remove-panel");

    const removeCategoriesList =
        document.querySelector(".categories-remove-list");


    categories.forEach(category => {

        const removePanelBtn =
            category.querySelector(
                ":scope > .category-options > .settings-dropdown > .delete-option-btn"
            );

        const settingsPanel =
            category.querySelector(
                ":scope > .category-options > .settings-dropdown"
            );

        const categoryTitle =
            category.querySelector(".category-title");


        removePanelBtn.addEventListener("click", event => {

            event.stopPropagation();

            categoryBeingRemoved = category;

            const currentCategoryName =
                categoryTitle.textContent;

            settingsPanel.classList.add("hidden");

            removeCategoryName.textContent =
                currentCategoryName;

            removePanel.showModal();
        });
    });


    chooseCategoryRemoveBtn.addEventListener("click", event => {

        event.stopPropagation();

        removeCategoriesList.innerHTML = "";

        categories.forEach(category => {

            if (category === categoryBeingRemoved) {
                return;
            }

            const categoryListItem =
                document.createElement("li");

            categoryListItem.textContent =
                category.querySelector(".category-title").textContent;

            removeCategoriesList.appendChild(categoryListItem);
        });

        removePanel.close();
        chooseCategoriesPanel.classList.remove("hidden");

    });


    defaultCategoryRemoveBtn.addEventListener("click", event => {

        event.stopPropagation();

        // Move transactions to "Others" here.
    });


    cancelCategoryRemoveBtn.addEventListener("click", event => {

        event.stopPropagation();

        removePanel.close();

        categoryBeingRemoved = null;
    });
}

setupRemoveCategory();


function setSameIcon(category) {

    const categoryIcon =
        category.querySelector(".icon-container svg");

    const categoryIconContainer =
        category.querySelector(".icon-container");

    const pickerBtn =
        document.querySelector(".icon-picker-btn");

    const colorPickerBtn =
        document.querySelector(".collor-picker-btn");

    if (!categoryIcon || !categoryIconContainer) {
        return;
    }

    // Icon picker
    pickerBtn.innerHTML = "";

    const pickerIcon =
        categoryIcon.cloneNode(true);

    pickerIcon.style.color =
        getComputedStyle(categoryIcon).color;

    pickerBtn.style.backgroundColor =
        getComputedStyle(categoryIconContainer).backgroundColor;

    pickerBtn.appendChild(pickerIcon);

    // Color picker button
    colorPickerBtn.style.backgroundColor =
        getComputedStyle(categoryIconContainer).backgroundColor;
}

setSameIcon();




