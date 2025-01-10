# YutoriSpa

! Welcome to YutoriSpa

YutoriSPA
is a web application that offers a variety of massage services to customers. Users can create accounts, book appointments, reschedule, and manage their bookings, all in one convenient place. Our goal is to help you relax and rejuvenate with ease applying the japanese philosophy of Yutori which is **a space to have peace of mind**

![Yutori mockup](/spa/static/images/mockup-Yutori.png)

## Features

- **Navigation Bar:** The navigation includes links to services, appointment booking, and user account options like login and logout, presented in a clean and professional layout
- **Service List:** Users can browse through a range of massage services, each presented with details and booking options.
- **User Authentication:** Customers can create accounts, log in, and manage their personal profiles, including editing information like phone number, address, and email.
- **Appointment Management:** Users can book, reschedule, or cancel their appointments, keeping their schedule flexible.
- **Admin Panel:** Django's built-in admin panel is used to manage users, services, and appointments efficiently.

### The Header

### - The header displays the YutoriSpa logo along with easy-to-use navigation links for services, booking, profile, login and appointments.

- Header Logout

![Header Yutori](/spa/static/images/Header-logout.png)

- Header Login

![Header Yutori](/spa/static/images/Header-login.png)

# torii gate

![Logo torii gate](/spa/static/images/torii-gate-header.png)

- **the logo have a symbolicall meaning:** A torii (Japanese: 鳥居, [to. ɾi. i]) is a traditional Japanese gate most commonly found at the entrance of or within a Shinto shrine, where it symbolically marks the transition from the mundane to the sacred, and a spot where kami are welcomed and thought to travel through

### Service List

- This section displays all the services YutoriSpa offers, allowing users to explore and choose based on their needs.

![Services](/spa/static/images/services-README.png)

### Booking System(login required)

- Our booking system allows customers to pick a service and schedule an appointment with ease. The process is streamlined for convenience.
- The client must to create an account to book a service.

![Booking system](/spa/static/images/Booking.section.png)

### Manage your booking

- This section will allow the user to manage , reschedule and cancel the appointment.

![manage your booking](/spa/static/images/manage-booking.png)

### User Profile

- profile login

![User Profile](/spa/static/images/profile-login.png)

- Customers can update their profiles, including their contact information, photo, and more.

![User Profile](/spa/static/images/my-profile.png)

### Home Page

- The home page give to the users a **welcome to YutoriSpa** with the link to the **explore our services**.

![Hero](/spa/static/images/welcome.png)

### login/register/password

- login

![login/register/password](/spa/static/images/login.btn.png)

- login form

![login/register/password](/spa/static/images/login.form.png)

- register form

![login/register/password](/spa/static/images/register.form.png.png)

- reset password

![login/register/password](/spa/static/images/forgot-pswrd.btn.png)

### - give the option to the users to register an account , and reset the password in case the users forgott.

## Footer with Social Media Links

- The footer contains links to social media profiles, helping customers stay connected with YutoriSpa. Links open in a new tab to avoid disruption of browsing.
- The copyrights and signiture by me , the developer of this application.

![login/register/password](/spa/static/images/footer.readme.png)

## Testing

YutoriSpa has been tested across different devices to ensure responsiveness and usability. Here’s a summary of the tests conducted:

- **Responsiveness:** Tested on various screen sizes to ensure proper display and functionality.

![testing lighthouse](/spa/static/images/lighthouse%20Yutori1.png)

![testing lighthouse](/spa/static/images/lighthouse%20Yutori2.png)

![testing lighthouse](/spa/static/images/lighthouse%20Yutori3.png)

- the project looks good wiht a performance of 99%,
- accesibility of 100%,
- best practices of 100%,
- SEO of 91%,

### responsive in all screen sizes.

![bug](/spa/static/images/debugg-footer.png)

- Check CSS properties such as `position: fixed;`, `flexbox`, or `grid` to ensure the footer stays at the bottom.
- The footer should remain fixed at the bottom of the page, regardless of the content height.

### Validator Testing

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fyutorispa-4e43a431e62f.herokuapp.com%2F)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fyutorispa-4e43a431e62f.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
- JavaScript
  - No errors were found when passing through the official [Jshint validator](https://jshint.com/)
    **Metrics**
    - The following metrics were returned:
    - There are 2 functions in this file.
    - Function with the largest signature take 1 arguments, while the median is 1.
    - Largest function has 2 statements in it, while the median is 1.5.
    - The most complex function has a cyclomatic complexity value of 1 while the median is 1.
  - **One warning**
    - 'arrow function syntax (=>)' is only available in ES6 (use 'esversion: 6').

### PIP8

- **Admin.py**
  ![PIP8 Admin.py](/spa/static/images/pip8%20ADMIN.png)
- **Models.py**
  ![PIP8 Models.py](/spa/static/images/pip8%20models.py.png)
- **Views.py**
  ![PIP8 Views.py](/spa/static/images/pip8-views.py.png)

### Unfixed Bugs

theres not unfixed Bugs.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub)

- The site was deployed to GitHub pages. The steps to deploy are as follows:
  - In the GitHub repository, navigate to the Settings tab
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

The live link can be found here - https://lionelwise77.github.io/FIFA-World-Cup-Quiz/

## Credits

- This project was developed by Sebastian Perez B.
- tutorials about JS in Youtube , who help to understand better the functions.
-
- CI Material content and chellengues.

### Content

- The content for the services and profile pages was inspired by the wellness industry and massage therapy practices. [ Tutorial begginers JS](https://www.youtube.com/watch?v=W6NZfCO5SIk)
- wikipedia material About FIFA World Cup [content](https://www.pexels.com/search/football/)

### Media

- All images used in this project are either custom-created or sourced from Pexels. [images](https://www.pexels.com/search/football/)
- and Google it.

# YutoriSpa

Welcome to **YutoriSpa**, a web application that offers a variety of massage services to customers. Users can create accounts, book appointments, reschedule, and manage their bookings—all in one convenient place. Our goal is to help you relax and rejuvenate by embracing the Japanese philosophy of **Yutori**, which emphasizes creating **a space for peace of mind**.

---

## Table of Contents

1. [Features](#features)
2. [Design Process](#design-process)
   - [Wireframes](#wireframes)
   - [Mockups](#mockups)
3. [Key Sections](#key-sections)
   - [Header](#header)
   - [Service List](#service-list)
   - [Booking System](#booking-system)
   - [Manage Your Booking](#manage-your-booking)
   - [User Profile](#user-profile)
   - [Footer](#footer)
4. [Testing](#testing)
5. [Deployment](#deployment)
6. [Credits and Acknowledgments](#credits-and-acknowledgments)

---

## Features

- **Navigation Bar**: Clean layout with links to services, appointment booking, user profiles, login, and logout.
- **Service List**: Browse a variety of massage options with details and booking functionality.
- **User Authentication**: Create accounts, log in, and manage personal profiles.
- **Appointment Management**: Book, reschedule, or cancel appointments with ease.
- **Admin Panel**: Efficiently manage users, services, and appointments using Django's admin interface.

---

## Design Process

### Wireframes

Wireframes were created to outline the basic structure and layout of the application. Below are examples of the initial designs:  
_Include wireframe images here._

### Mockups

High-fidelity mockups were designed to visualize the final layout and styling:  
_Include mockup images or links here._

### Diagrams

User flow diagrams illustrate the journey of customers through the application, from registration to booking a service:  
_Include diagrams such as user flow or ERD if applicable._

---

## Key Sections

### Header

The header features the **YutoriSpa** logo and easy-to-use navigation links.

- **Logged-Out View**:  
  ![Header Logout](spa/static/images/Header-logout.png)

- **Logged-In View**:  
  ![Header Login](spa/static/images/Header-login.png)

**Logo Meaning**:  
The logo incorporates a Torii gate, symbolizing the transition from mundane to sacred, aligning with YutoriSpa's mission to provide a tranquil escape.  
![Torii Gate Logo](spa/static/images/torii-gate-header.png)

---

### Service List

Discover services tailored to your relaxation needs.  
![Service List](spa/static/images/services-README.png)

---

### Booking System

The user-friendly system allows customers to select services and schedule appointments effortlessly.

- Customers must create an account to book a service.  
  ![Booking System](spa/static/images/Booking.section.png)

---

### Manage Your Booking

Reschedule or cancel your appointments directly from the user dashboard.  
![Manage Booking](spa/static/images/manage-booking.png)

---

### User Profile

Customers can update personal details and manage their profiles.  
![Profile Login](spa/static/images/profile-login.png)  
![My Profile](spa/static/images/my-profile.png)

---

### Footer

The footer includes social media links and developer credits.  
![Footer](spa/static/images/footer.readme.png)

---

## Testing

### Responsiveness

The application has been tested across various devices to ensure compatibility.

### Performance Metrics

- **Performance**: 99%
- **Accessibility**: 100%
- **Best Practices**: 100%
- **SEO**: 91%

### Validator Testing

- **HTML**: Passed W3C validation.
- **CSS**: Passed Jigsaw validation.
- **JavaScript**: Passed JSHint validation (minor warnings addressed).

---

## Deployment

The application was deployed using [GitHub Pages](https://pages.github.com/).

Steps:

1. Navigate to the repository's **Settings**.
2. In the **Source** section, select `master` or `main` branch.
3. Deployment is completed when the success ribbon appears.

Live Project Link: _Include live link here._

---

## Credits and Acknowledgments

- **Design Inspiration**: Japanese culture and aesthetics.
- **Frameworks & Tools**: Django, Bootstrap, Lighthouse.
