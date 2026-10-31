const defaultCategories = [
    {
        name: "Food",
        type: "food",
        icon: "utensils",
        color: "#F59E0B",
        subcategories: ["Groceries", "Restaurants", "Delivery", "Snacks"]
    },
    {
        name: "Transport",
        type: "transport",
        icon: "car",
        color: "#3B82F6",
        subcategories: ["Fuel", "Public Transport", "Uber", "Parking"]
    },
    {
        name: "Housing",
        type: "housing",
        icon: "house",
        color: "#A855F7",
        subcategories: ["Rent", "Electricity", "Water", "Internet"]
    },
    {
        name: "Health",
        type: "health",
        icon: "heart-pulse",
        color: "#EF4444",
        subcategories: ["Medicine", "Doctor", "Dentist"]
    },
    {
        name: "Education",
        type: "education",
        icon: "book-open",
        color: "#06B6D4",
        subcategories: ["Tuition", "Courses", "Books"]
    },
    {
        name: "Entertainment",
        type: "entertainment",
        icon: "gamepad-2",
        color: "#EC4899",
        subcategories: ["Movies", "Games", "Streaming"]
    },
    {
        name: "Shopping",
        type: "shopping",
        icon: "shopping-bag",
        color: "#EAB308",
        subcategories: ["Clothing", "Electronics", "Personal Care"]
    },
    {
        name: "Family",
        type: "family",
        icon: "users",
        color: "#F97316",
        subcategories: ["Children", "Gifts", "Family Support"]
    },
    {
        name: "Services",
        type: "services",
        icon: "wrench",
        color: "#64748B",
        subcategories: ["Subscriptions", "Cloud Services"]
    },
    {
        name: "Financial",
        type: "financial",
        icon: "wallet",
        color: "#10B981",
        subcategories: ["Bank Fees", "Loans", "Credit Card"]
    },
    {
        name: "Leisure",
        type: "leisure",
        icon: "plane",
        color: "#14B8A6",
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

    const categoryElement = category.querySelector(".category");
    const title = category.querySelector(".category-title");
    const subcategoriesList = category.querySelector(".subcategories");

    categoryElement.style.setProperty(
        "--category-color",
        categoryData.color
    );

    categoryElement.dataset.category = categoryData.type;
    categoryElement.dataset.color = categoryData.color;

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
    const categoriesContainer = document.querySelector(".categories-list");

    if (!categoriesContainer) {
        return;
    }

    categoriesContainer.addEventListener("click", event => {
        const tagBtn = event.target.closest(".category-tag");

        if (!tagBtn) {
            return;
        }

        event.stopPropagation();

        const category = tagBtn.closest(".category");

        if (!category) {
            return;
        }

        const subcategories = category.querySelector(
            ":scope > .category-options .subcategories-container"
        );

        if (!subcategories) {
            return;
        }

        // Close ALL settings panels
        categoriesContainer
            .querySelectorAll(".settings-dropdown")
            .forEach(settingsPanel => {
                settingsPanel.classList.add("hidden");
            });

        // Close subcategories in OTHER categories
        categoriesContainer
            .querySelectorAll(".subcategories-container")
            .forEach(otherSubcategories => {
                if (otherSubcategories !== subcategories) {
                    otherSubcategories.classList.add("hidden");
                }
            });

        // Toggle this category's subcategories
        subcategories.classList.toggle("hidden");
    });

    document.addEventListener("click", event => {
        if (event.target.closest(".category-tag")) {
            return;
        }

        categoriesContainer
            .querySelectorAll(".subcategories-container")
            .forEach(subcategories => {
                if (!subcategories.contains(event.target)) {
                    subcategories.classList.add("hidden");
                }
            });
    });
}

setupOpenSubcategories();


function setupCategoriesSettings() {
    const categories = document.querySelectorAll(".category, .subcategory");

    function getSettingsButton(category) {
        return category.querySelector(
            ":scope > .category-options > .category-settings, :scope > .category-settings"
        );
    }

    function getSettingsPanel(category) {
        return category.querySelector(
            ":scope > .category-options > .settings-dropdown, :scope > .settings-dropdown"
        );
    }

    categories.forEach(category => {
        const settingsButton = getSettingsButton(category);
        const settingsPanel = getSettingsPanel(category);

        const subcategories = category.querySelector(
            ":scope > .category-options > .subcategories-container"
        );

        if (!settingsButton || !settingsPanel) return;

        settingsButton.addEventListener("click", event => {
            event.stopPropagation();

            if (subcategories) {
                subcategories.classList.add("hidden");
            }

            categories.forEach(otherCategory => {
                const otherPanel = getSettingsPanel(otherCategory);

                if (otherPanel && otherPanel !== settingsPanel) {
                    otherPanel.classList.add("hidden");
                }
            });

            settingsPanel.classList.toggle("hidden");
        });
    });

    document.addEventListener("click", event => {
        categories.forEach(category => {
            const settingsPanel = getSettingsPanel(category);
            const settingsButton = getSettingsButton(category);

            if (
                settingsPanel &&
                settingsButton &&
                !settingsPanel.contains(event.target) &&
                !settingsButton.contains(event.target)
            ) {
                settingsPanel.classList.add("hidden");
            }
        });
    });
}

setupCategoriesSettings();


function initializeEditCategoryColor(category, colorPickerBtn) {
    const color = category.dataset.color;

    console.log("Category color:", color);

    colorPickerBtn.style.backgroundColor = color;

    console.log(
        "Picker background:",
        getComputedStyle(colorPickerBtn).backgroundColor
    );
}

function applyEditCategoryColor(color, colorPickerBtn, category) {
    colorPickerBtn.style.backgroundColor = color;
    category.style.setProperty("--category-color", color);
}

function openEditCategory(category) {
    const colorPickerBtn = editCategoryDialog.querySelector(".collor-picker-btn");

    initializeEditCategoryColor(category, colorPickerBtn);

    editCategoryDialog.showModal();
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
    const categories = document.querySelectorAll(".category, .subcategory");

    const editCategoryPanel = document.querySelector(".edit-category");

    if (!editCategoryPanel) {
        console.error("Edit category panel not found.");
        return;
    }

    const input = editCategoryPanel.querySelector(".edit-category-input");
    const colorPickerBtn = editCategoryPanel.querySelector(".collor-picker-btn");
    const colorPalette = editCategoryPanel.querySelector(".edit-color-palette");
    const iconPickerBtn = editCategoryPanel.querySelector(".icon-picker-btn");
    const iconPickerPanel = editCategoryPanel.querySelector(".icon-picker-panel");
    const saveChanges = editCategoryPanel.querySelector(".save-category-edition");
    const cancelChanges = editCategoryPanel.querySelector(".cancel-category-edition");

    if (
        !input ||
        !colorPickerBtn ||
        !colorPalette ||
        !iconPickerBtn ||
        !iconPickerPanel ||
        !saveChanges ||
        !cancelChanges
    ) {
        console.error("One or more edit category panel elements were not found.");
        return;
    }

    // Create color options once
    createColorOptions(colorPalette, color => {
        if (!categoryBeingEdited) {
            return;
        }

        editedCategoryColor = color;

        colorPickerBtn.style.backgroundColor = color;
        iconPickerBtn.style.backgroundColor = color;

        colorPalette.classList.add("hidden");
    });

    // Setup Edit buttons for categories and subcategories
    categories.forEach(category => {
        const editCategoryBtn = category.querySelector(
            ":scope > .category-options > .settings-dropdown > .edit-option-btn, " +
            ":scope > .settings-dropdown > .edit-option-btn"
        );

        if (!editCategoryBtn) {
            return;
        }

        editCategoryBtn.addEventListener("click", event => {
            event.stopPropagation();

            categoryBeingEdited = category;

            // Get current category name
            const categoryTitle = category.querySelector(".category-title");

            editedCategoryName = categoryTitle.textContent;
            input.value = editedCategoryName;

            // Get current category color
            const iconContainer = category.querySelector(".icon-container");

            if (iconContainer) {
                editedCategoryColor =
                    getComputedStyle(iconContainer).backgroundColor;

                colorPickerBtn.style.backgroundColor = editedCategoryColor;
                iconPickerBtn.style.backgroundColor = editedCategoryColor;
            }

            // Get current category icon
            const categoryIcon = category.querySelector(".icon-container svg, .icon-container i");

            if (categoryIcon) {
                editedCategoryIcon =
                    categoryIcon.getAttribute("data-lucide");

                iconPickerBtn.innerHTML = "";

                const pickerIcon = categoryIcon.cloneNode(true);
                iconPickerBtn.appendChild(pickerIcon);

                lucide.createIcons();
            }

            // Close pickers when opening modal
            colorPalette.classList.add("hidden");
            iconPickerPanel.classList.add("hidden");

            // Show edit modal
            editCategoryPanel.showModal();

            // Hide settings dropdown
            const settingsPanel = category.querySelector(
                ":scope > .category-options > .settings-dropdown, " +
                ":scope > .settings-dropdown"
            );

            if (settingsPanel) {
                settingsPanel.classList.add("hidden");
            }
        });
    });

    // Update temporary name
    input.addEventListener("input", () => {
        editedCategoryName = input.value;
    });

    // Open / close edit color picker
    colorPickerBtn.addEventListener("click", event => {
        event.stopPropagation();

        const isHidden = colorPalette.classList.contains("hidden");

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
        const iconOption = event.target.closest(".icon-option");

        if (!iconOption) {
            return;
        }

        editedCategoryIcon = iconOption.dataset.icon;

        // Show selected icon in modal
        iconPickerBtn.innerHTML = "";

        const selectedIcon = document.createElement("i");
        selectedIcon.setAttribute("data-lucide", editedCategoryIcon);

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

        categoryTitle.textContent = editedCategoryName;

        // Apply color
        applyEditCategoryColor(
            editedCategoryColor,
            colorPickerBtn,
            categoryBeingEdited
        );

        // Apply icon
        if (editedCategoryIcon) {
            const categoryIconContainer =
                categoryBeingEdited.querySelector(".icon-container");

            categoryIconContainer.innerHTML = "";

            const newIcon = document.createElement("i");

            newIcon.setAttribute("data-lucide", editedCategoryIcon);

            categoryIconContainer.appendChild(newIcon);

            lucide.createIcons();
        }

        // Close modal and reset temporary values
        editCategoryPanel.close();

        categoryBeingEdited = null;
        editedCategoryName = null;
        editedCategoryColor = null;
        editedCategoryIcon = null;
    });

    // CANCEL
    cancelChanges.addEventListener("click", event => {
        event.stopPropagation();

        // The actual category wasn't changed before saving
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
    const categories = document.querySelectorAll(".category, .subcategory");

    const removePanel = document.querySelector(".remove-panel");
    const removeCategoryName = document.querySelector(".remove-category-name");
    const chooseCategoryRemoveBtn = document.querySelector(".choose-category-remove");
    const defaultCategoryRemoveBtn = document.querySelector(".default-remove-category");
    const cancelCategoryRemoveBtn = document.querySelector(".cancel-remove-category");
    const chooseCategoriesPanel = document.querySelector(".safe-remove-panel");
    const removeCategoriesList = document.querySelector(".categories-remove-list");
    const closeRemoveCategoriesListBtn = document.querySelector(".cancel-category-remove");

    if (
        !removePanel ||
        !removeCategoryName ||
        !chooseCategoryRemoveBtn ||
        !defaultCategoryRemoveBtn ||
        !cancelCategoryRemoveBtn ||
        !chooseCategoriesPanel ||
        !removeCategoriesList ||
        !closeRemoveCategoriesListBtn
    ) {
        console.error("One or more remove category panel elements were not found.");
        return;
    }

    // Setup Delete buttons for categories and subcategories
    categories.forEach(category => {
        const removePanelBtn = category.querySelector(
            ":scope > .category-options > .settings-dropdown > .delete-option-btn, " +
            ":scope > .settings-dropdown > .delete-option-btn"
        );

        const settingsPanel = category.querySelector(
            ":scope > .category-options > .settings-dropdown, " +
            ":scope > .settings-dropdown"
        );

        const categoryTitle = category.querySelector(".category-title");

        if (!removePanelBtn || !settingsPanel || !categoryTitle) {
            return;
        }

        removePanelBtn.addEventListener("click", event => {
            event.stopPropagation();

            categoryBeingRemoved = category;

            removeCategoryName.textContent = categoryTitle.textContent;

            settingsPanel.classList.add("hidden");

            removePanel.showModal();
        });
    });

    // Choose another category to receive the transactions
    chooseCategoryRemoveBtn.addEventListener("click", event => {
        event.stopPropagation();

        removeCategoriesList.innerHTML = "";

        categories.forEach(category => {
            if (category === categoryBeingRemoved) {
                return;
            }

            const categoryTitle = category.querySelector(".category-title");

            if (!categoryTitle) {
                return;
            }

            const categoryListItem = document.createElement("li");
            const categoryButton = document.createElement("button");

            categoryButton.type = "button";
            categoryButton.className = "category-button";
            categoryButton.textContent = categoryTitle.textContent;

            categoryButton.addEventListener("click", event => {
                event.stopPropagation();

                // Move transactions to the selected category here.
                // categoryBeingRemoved is the category being deleted.
                // category is the selected destination.
            });

            categoryListItem.appendChild(categoryButton);
            removeCategoriesList.appendChild(categoryListItem);
        });

        removePanel.close();
        chooseCategoriesPanel.showModal();
    });

    // Close the destination selection and return to the removal dialog
    closeRemoveCategoriesListBtn.addEventListener("click", event => {
        event.stopPropagation();

        chooseCategoriesPanel.close();
        removePanel.showModal();
    });

    // Remove the category and move its transactions to "Others"
    defaultCategoryRemoveBtn.addEventListener("click", event => {
        event.stopPropagation();

        // Move transactions to "Others" here.
    });

    // Cancel removal
    cancelCategoryRemoveBtn.addEventListener("click", event => {
        event.stopPropagation();

        removePanel.close();
        categoryBeingRemoved = null;
    });
}

setupRemoveCategory();


// function setupMoveCategories(categoryBeingRemoved) {
    
// }


function setSameIcon(category) {
    const categoryIcon = category.querySelector(".icon-container svg");
    const pickerBtn = editCategoryDialog.querySelector(".icon-picker-btn");
    const colorPickerBtn = editCategoryDialog.querySelector(".collor-picker-btn");

    if (!categoryIcon || !pickerBtn || !colorPickerBtn) return;

    // Get the original category color
    const categoryColor = category.dataset.color;

    // Initialize color picker
    colorPickerBtn.style.backgroundColor = categoryColor;

    // Initialize icon picker
    pickerBtn.innerHTML = "";
    pickerBtn.appendChild(categoryIcon.cloneNode(true));

    // Initialize icon picker background
    pickerBtn.style.backgroundColor = categoryColor;
}

setSameIcon(category);



