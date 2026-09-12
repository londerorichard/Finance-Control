function setupColorPalettes() {

    const categoryItems = document.querySelectorAll(".category, .subcategory");

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

    categoryItems.forEach(category => {

        const header = category.querySelector(".category-header");
        const button = header.querySelector(".category-main");
        const palette = header.querySelector(".color-palette");
        const iconContainer = category.querySelector(".icon-container");

        if (!button || !palette) {
            return;
        }

        // Create the color options
        colors.forEach(color => {

            const colorOption = document.createElement("button");

            colorOption.type = "button";
            colorOption.classList.add("color-option");
            colorOption.style.backgroundColor = color;

            palette.appendChild(colorOption);

            colorOption.addEventListener("click", () => {

                // Change icon color
                button.style.backgroundColor = color;

                // Change tag color
                if (iconContainer) {
                    iconContainer.style.backgroundColor = color;
                }

                // Close palette
                palette.classList.remove("open");
            });
        });

        // Open/close palette
        button.addEventListener("click", () => {

            // Close all other palettes
            categoryItems.forEach(otherCategory => {

                const otherPalette =
                    otherCategory.querySelector(".color-palette");

                if (otherPalette && otherPalette !== palette) {
                    otherPalette.classList.remove("open");
                }
            });

            // Toggle current palette
            palette.classList.toggle("open");
        });
    });

    // Close palettes when clicking outside
    document.addEventListener("click", event => {

        if (
            !event.target.closest(".category-header") &&
            !event.target.closest(".color-palette")
        ) {
            document.querySelectorAll(".color-palette").forEach(palette => {
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


let categoryBeingEdited = null;

function setupEditCategory() {

    const categories = document.querySelectorAll(".category");
    const editCategoryPanel = document.querySelector(".edit-category");

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

            // Remember which category was selected
            categoryBeingEdited = category;

            // Open modal
            editCategoryPanel.classList.remove("hidden");
        });
    });
}

setupEditCategory();


function setSameIcon() {
    const categoryIcon = category.querySelector(".icon-container svg");
    const pickerBtn = category.querySelector(".icon-picker-btn");

    const pickerIcon = categoryIcon.cloneNode(true);

    pickerBtn.appendChild(pickerIcon);
}

setSameIcon();


// setupIconPicker() {

//     const icons = [
//         "utensils",
//         "shopping-cart",
//         "car",
//         "home",
//         "coffee",
//         "gamepad-2",
//         "heart",
//         "briefcase",
//         "plane",
//         "gift",
//         "music",
//         "book-open",
//         "dumbbell",
//         "shirt",
//         "dog",
//         "paw-print"
//     ];

//     const panel = document.querySelector(".icon-picker-panel");

//     icons.forEach(icon => {
//         const button = document.createElement("button");

//         button.type = "button";
//         button.classList.add("icon-option");
//         button.dataset.icon = icon;

//         button.innerHTML = `<i data-lucide="${icon}"></i>`;

//         panel.appendChild(button);
//     });

//     lucide.createIcons();
// }