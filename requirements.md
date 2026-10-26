# <u>Requirements binderbase</u>

AI ORDER: No cheesey phrases throughout the website.
AI ORDER: No pointing arrows on the website unless specified.

# What technologies are used?

- Frontend: Vue with JavaScript, HTML, and CSS
- Backend: FastAPI and SQLModel using SQLite

# What is BinderBase?

AI ORDER: Do not add anything to the website from what is mentioned in this section. This is simply to get an idea of what the website is supposed to be.

- BuilderBase is a binder planning website for trading cards, specifically Pokemon cards. 
- The user can create binders and add whatever cards they want them. 
- They can upload art to slots of the binder. If these art pieces are next to each other; the user can combine them together to look like one continuous piece of art.
- The back of sleeves made officially by the Pokemon company can be added to binder slots as an additional piece of art.
- Clear sleeve varients can be added behind the card in a binder slot.

# Frontend

## General appearance and style

### Theme

- There's a light, dark, and high contrast theme that the user can switch between on the website.
- The primary highlight colour is a Pokemon-like blue but is slightly lighter or darker based on the theme. 
- The theme is controlled by a button which rotates through the themes. 
- Icons tell the user which theme is next, as well as a hint when the user hovers over the button. The text next to the theme button says what theme is currently in use, e.g. High contrast, Light, Dark.
- When you hover over the theme button it changes the colour of the button slightly depending on what theme is currently active. No other animations are used.

### Font

- The font is Comic sans throughout the website.

### Logo/emblem

- The colour should be the same as the primary highlight colour for the current theme of the website.
- The font of the characters is the same as the rest of the website.
- There are 3 cards which make up the logo. The centre one isn't angled, and the other 2 are angled ~20 degrees in opposite directions away from each other. 
- The 2 cards on the sides have 2 B's inside of them. The centre card is the style of the back of a card but doesn't include a Pokeball for copyright reasons. The 2 cards on the side are a layer in front of the centre card and are close to each other but don't quite intersect.
- The base logo is scaled to fit across the website. For example, any gaps inside the logo should be scaled down if the logo is made smaller.
- The logo appears in the home page and navigation menu.
- The logo is used as the icon for the website and changes colour based on the theme.

## Navigation

![Website navigation map](diagrams/WebsiteMap.png)

- Login and registration when logged out, and logout when logged in, as well as the theme changer are on the right side of the navigation bar. All other navigation elements are on the left side of the navigation bar.

## Home page

- BinderBase has a home page which is the first page the user is greated with upon loading the website with "Welcome to BinderBase.". This page contains everything the user needs to know about the website.
- There is a typewriter animation affect on the phrase "Welcome to BinderBase." which goes round in a loop. Before the typewriter reaches each character, it isn't seen. The animation lasts 5 seconds and there is a 0.5 second pause between starting the animation again. 
- When the user is logged in, the phrase changes to "Welcome to BinderBase _insert_username_." 
- The box surrounding the introduction to the website is the same size whether the user is logged in or not.
- The logo on the home page hovers up and down 30 pixels in a css animation over 6 seconds.