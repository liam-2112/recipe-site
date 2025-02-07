# <img src="/static/images/logo.webp" alt="logo" width="80em" /> **Recipe Manager**

### A recipe management and discovery website
Recipe Manager is an innovative online platform that combines the functionality of a social media site with the practicality of a recipe-sharing hub. Designed for food enthusiasts of all kinds, from home cooks to professional chefs, Recipe Manager strives to bring people together by fostering a shared passion for cooking, eating, and culinary discovery.

Live site: <a href="https://recipe-manager-site-9b7bfd4b2c5e.herokuapp.com/" target="_blank">Recipe Manager</a>

![Responsive Devices View]()

## Table of Contents
1. [UX - User Experience](#ux---user-experience)
    - [Overview](#overview)
    - [Design Inspiration](#design-inspiration)
    - [Target User](#target-user)
2. [Project Planning](#project-planning)
    - [Site Goals](#site-goals)
    - [Color Scheme](#color-scheme)
    - [Fonts](#fonts)
    - [Agile Methodologies](#agile-methodologies)
    - [Sprints](#sprints)
3. [User Stories](#user-stories)
    - [User Stories Overview](#user-stories-overview)
    - [List of User Stories](#list-of-user-stories)
4. [wireframes](#wireframes)
5. [Database Planning](#database-planning)
    - [ER Diagram](#er-diagram)
    - [User Flow Diagram](#user-flow-diagram)
6. [Features](#features)
    - [Home Page](#home-page)
    - [Recipes Page](#recipes-page)
    - [Suggestions Page](#suggestions-page)
    - [Registration Page](#registration-page)
    - [Log In Page](#log-in-page)
    - [Log Out Page](#log-out-page)
    - [Nav Bar And Footer](#nav-bar-and-footer)
    - [Confirmation Messages](#confirmation-messages)
    - [CRUD Functionality](#crud-functionality)
7. [Future Features](#future-features)
    - [User Page](#user-page)
8. [Technologies Used](#technologies-used)
9. [Testing](#testing)
    - [Accessability testing](#accessability-testing)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [Javascript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
    - [Automated Testing](#automated-testing)
    - [Manual Testing](#manual-testing)
10. [Deployment](#deployment)
    - [Connecting to GitHub](#connecting-to-github)
    - [Django Project Setup](#django-project-setup)
    - [Cloudinary API](#cloudinary-api)
    - [PostgreSQL](#postgresql)
    - [Heroku deployment](#heroku-deployment)
11. [Resources](#resources)
12. [Credits](#credits)
13. [Acknowledgements](#acknowledgements)
14. [Updates](#updates)


## UX - User Experience

### Overview

The Recipe Manager website is designed to help people discover new ways of cooking and finding new foods. The aim of the site is to be simple and easy to navigate while allowing the user to like and save foods that they find while on the site. It was also made with the possibility in mind of bringing out hidden family recipes that people may want to share with the world.

### Design Inspiration

The inspiration for the design of this website came from the idea of having a food social site where you scroll and save the items you think you may enjoy. There will be a chance to also have this as a social too with future updates, but the main purpose of the site is to be able to find recipes you might not have come across before.

### Target User

- **Experienced Cooks**: Cooks with experience that could add recipe ideas to the site, who could also give tips to other recipes on the site.
- **Cooks With No Experience**: Cooks with no experience looking to learn how to cook dishes but unsure where to start. The site will have a social aspect to it where others can offer advice or help with instructions to cooking items.
- **Cooks Looking To Discover New Recipes**: Cooks who just want to scroll through recipes while they have some downtime in the hopes they could find inspiration for new dishes.
- **Cooks Looking To Share Recipes**:Cook enthusiasts who want to give people the best options of food they can.


##### [ Back To Table Of Contents ](#table-of-contents)

## Project Planning

### site goals
The goals of the website is to bring people together who can share recipes and want to teach or learn how to cook dishes. There will be a user page where the user can keep recipes they like stored. 

### Color Scheme
Before starting the project i had some color schemes in my head ready to use. The use of darker background colors such as black and grey, with a strong orange color for borders really makes the content stand out for me. Mixed with images i find the colors i've used for the website are not too bright and not too dark.

### Fonts
For the fonts i have used sans seriff. This may be subject to change in future updates.

### Agile Methodologies
In developing my Recipe Manager web app, I adopted Agile methodology to ensure flexibility, continuous improvement, and efficient project management. The use of Agile allowed for iterative development, enabling me to frequently reassess and adjust the project scope.

![Project board](docs/wireframes/project-board.png)

#### Kanban Board Overview

### Sprints

##### [ Back To Table Of Contents ](#table-of-contents)

## User Stories

### User Stories Overview

### List of User Stories
**Registration**
- [User registration](https://github.com/liam-2112/recipe-site/issues/2)
- [User login](https://github.com/liam-2112/recipe-site/issues/3)
- [User logout](https://github.com/liam-2112/recipe-site/issues/5)

**Features**
- [Home Page](https://github.com/liam-2112/recipe-site/issues/1)
- [Home Page]()

**Admin**
- [Quality Control](https://github.com/liam-2112/recipe-site/issues/6)


##### [ Back To Table Of Contents ](#table-of-contents)

## Wireframes

Balsamiq Wireframes

### Laptop - Home Page
![user diagram]()


### Phone - Home Page
![user diagram]()

##### [ Back To Table Of Contents ](#table-of-contents)

## Database Planning

### ER Diagram

![ER diagram]()

### User Flow Diagram


![user flow diagram]()


##### [ Back To Table Of Contents ](#table-of-contents)


## Features

### Home Page

### Recipes Page

### Suggestions Page

### Registration Page

### Log In Page

### Log Out Page

### Nav Bar And Footer

### Confirmation Messages

### CRUD functionality


##### [ Back To Table Of Contents ](#table-of-contents)


## Future Features

### User Page

##### [ Back To Table Of Contents ](#table-of-contents)

## Technologies Used
| Technology | Reason |
| --- | --- |
| HTML | Page Structure
| Javascript | Event Listeners, Modals
| CSS | Page Styling
| Bootstrap 5 | Page Styling
| Python | Backend Server
| Django | Backend Framework
| CodeInstitute PostgreSQL | Database
| Balsamiq Wireframes | Design
| Git | Version Control
| GitHub | Code Hosting and Project Management
| Heroku | Project Deployment
| GitPod | IDE
| VSCode | Backup IDE

##### [ Back To Table Of Contents ](#table-of-contents)


## Testing

### Accessibility Testing

lighthouse

### HTML Validation


### CSS Validation


### JavaScript Validation


### Python Validation


### Automated Testing
Django tests to cover filters, forms, views, and models, helping to maintain data accuracy and consistency across the site.


### Manual Testing
User story checks manually

| **User Stories** |  Tested |  Works As Intended |
|  --- | --- | --- |
| As an **admin**, I can **1** | ✅ | ✅
| As an **admin** I can **1** |✅ | ✅
| As an **admin** I can **1** |✅ | ✅
| As an **admin** I **1** |✅ | ✅
| As an **unregistered user** I **1** |✅ | ✅
| As an **unregistered user** I **1** |✅ | ✅
| As an **unregistered user** I **1** |✅ | ✅
| As a **unregistered user**, I can **1** |✅ | ✅
| As a **unregistered user**, I can **1** |✅ | ✅
| As a **unregistered user**, I can **1** |✅ | ✅
| As a **user**, I can **1** |✅ | ✅
| As a **user**, I can **1** |✅ | ✅
| As a **user**, I can **1** |✅ | ✅
| As a **user**, I can **1** |✅ | ✅
| As a **user**, I can **1** |✅ | ✅
| As a **user**, I can **1** |✅ | ✅
| As a **user**, I can **1** |✅ | ✅
| As a **user**, I can **1** |✅ | ✅
| As a **user**, I **1** |✅ | ✅
| As a **user**, I **1** |✅ | ✅
| As a **user**, I can **1** |✅ | ✅

##### [ Back To Table Of Contents ](#table-of-contents)


## Deployment

### Connecting To GitHub

### Django Project Setup

### Cloudinary API

### PostgreSQL

### Heroku Deployment


##### [ Back To Table Of Contents ](#table-of-contents)

## Resources
* [Stack Overflow](https://stackoverflow.com/)
* [W3School](https://www.w3schools.com/)
* [YouTube](https://www.youtube.com/)
* [Django docs](https://www.djangoproject.com/)
* [Crispyforms docs](https://django-crispy-forms.readthedocs.io/en/latest/)

##### [ Back To Table Of Contents ](#table-of-contents)

## Credits
I give credit to https://github.com/Anka-S/hata-na-tata. I was inspired by their work and the layout was very similar to what i wanted to use myself.
I have used their code as a template and changed bits to meet what i need. Some bits of code are still the same, But with future updates i plan to change the code to fit better with my project and the features.

I give credit to Code Institute for helping me through this journey and for giving me code i have used from the LMS Django walkthrough. Thank you to all the facilitators for being there to help too.

I must also credit Mars Oakley and Guy Steele-Perkins from my WECA Boootcamp program for helping me to understand some issues such as merging.

##### [ Back To Table Of Contents ](#table-of-contents)

## Acknoweledgement
Ran out of time to do/finish the README.MD
future updates to come to the website and the readme

##### [ Back To Table Of Contents ](#table-of-contents)

## Updates

##### [ Back To Table Of Contents ](#table-of-contents)