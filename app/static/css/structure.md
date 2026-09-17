# CSS Organization Guide

## 1. Reset

* [ ] CSS Reset
* [ ] `box-sizing`
* [ ] Remove default margins and paddings

---

## 2. Variables

* [ ] Colors
* [ ] Typography
* [ ] Spacing
* [ ] Border radius
* [ ] Shadows
* [ ] Transitions

---

## 3. Base Styles

* [ ] `body`
* [ ] `html`
* [ ] `h1` – `h6`
* [ ] `p`
* [ ] `a`
* [ ] `img`
* [ ] `ul`
* [ ] `ol`
* [ ] `button`
* [ ] `input`

---

## 4. Layout

* [ ] Hero
* [ ] Container
* [ ] Grid
* [ ] Navbar
* [ ] Sidebar
* [ ] Main
* [ ] Footer

---

## 5. Components

* [ ] Buttons
* [ ] Cards
* [ ] Forms
* [ ] Inputs
* [ ] Search
* [ ] Avatar
* [ ] Divider
* [ ] Tables
* [ ] Modals
* [ ] Dropdowns
* [ ] Notifications
* [ ] Profile Menu
* [ ] Pagination
* [ ] Tooltips
* [ ] Badges

---

## 6. States

* [ ] `:hover`
* [ ] `:active`
* [ ] `:focus`
* [ ] `:disabled`
* [ ] `.hidden`
* [ ] `.active`
* [ ] `.selected`
* [ ] `.error`
* [ ] `.success`

---

## 7. Utilities

* [ ] `.hidden`
* [ ] `.visually-hidden`
* [ ] `.text-center`
* [ ] `.text-left`
* [ ] `.text-right`
* [ ] `.sr-only`
* [ ] `.flex`
* [ ] `.grid`

---

# Recommended CSS Property Order

```css
.selector {
    /* ===================================
       Layout
    =================================== */

    display:
    position:
    top:
    right:
    bottom:
    left:
    z-index:

    /* ===================================
       Size
    =================================== */

    width:
    min-width:
    max-width:

    height:
    min-height:
    max-height:

    /* ===================================
       Spacing
    =================================== */

    margin:
    padding:
    gap:

    /* ===================================
       Appearance
    =================================== */

    border:
    border-radius:
    outline:
    background:

    /* ===================================
       Typography
    =================================== */

    font-family:
    font-size:
    font-weight:
    line-height:
    text-align:
    text-decoration:
    color:

    /* ===================================
       Effects
    =================================== */

    opacity:
    overflow:
    box-shadow:
    transition:
    transform:

    /* ===================================
       Interaction
    =================================== */

    cursor:
}
```

