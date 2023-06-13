# **BarBelles**
## **API Overview**

The BarBelles API has been developed using the Django Rest Framework in order to serve as the back-end component to Barbelles, an online fitness community for women. The front-end, developed using React, provides women with a safe and inclusive space to share their own personal fitness journeys as well as the opportunity to learn and interact with other in the community. Users can read posts by others, create, update and delete their own posts as well as follow other users. There is also the facility to add, edit or delete comments. Users can learn from video Tutorials added by the site owner, Kate Ross. The BarBelles API provides the functionality for all of these interactions, connecting to an external Postgresql database to store images, profile data, videos, comments and followers.

The entire basis of this project is to facilitate a smooth, seamless user experience on the front-end.

<hr>

![Screenshot of BarBelles API](docs/images/api-home.png)

The deployed API can be found [here](https://barbelles-api.herokuapp.com/).

<hr>

## Table of contents:
1. [**Site Overview**](#site-overview)
1. [**Planning stage**](#planning-stage)
    * [**Strategy**](#strategy)
      * [***Site Aims***](#site-aims)
      * [***Target Audiences***](#target-audiences)
      * [***User Stories***](#user-stories)
    * [***Wireframes***](#wireframes)
    * [***Database Schema***](#database-schema)
    * [***Colour Scheme***](#color-scheme)
    * [***Typography***](#typography)
1. [**Agile Development**](#agile-development)
1. [**Features**](#features)
    * [***Admin Page***](#admin-page)
    * [***Navbar***](#navbar)
    * [***Social Media and Email Links***](#social-media-and-email-links)
    * [***Home Page***](#home-page)
    * [***Books Page***](#books-page)
    * [***Book Detail Page***](#book-detail-page)
    * [***Add Book Page***](#book-detail-page)
    * [***Edit Book Page***](#edit-book-page)
    * [***Delete Book Page***](#delete-book-page)
    * [***Authors Page***](#authors-page)
    * [***Author Detail Page***](#author-detail-page)
    * [***About Page***](#about-page)
    * [***Profile Page***](#profile-page)
    * [***Account Pages***](#account-pages)
      * [***Sign Up***](#sign-up)
      * [***Log In***](#log-in)
      * [***Log Out***](#log-out)
    * [***Messages***](#messages)
    * [***Defensive Design***](#defensive-design)
    * [***User Authentication***](#user-authentication)
    * [***404 Page***](#404-page)
1. [**Future-Enhancements**](#future-enhancements)
1. [**Testing Phase**](#testing-phase)
1. [**Deployment**](#deployment)
1. [**Software and Tech**](#software-and-tech)
1. [**Media**](#media)
1. [**Credits**](#credits)
1. [**Honourable mentions**](#honorable-mentions)

<hr>

## **Planning Stage**

### **API Aims:**

* Provide the back-end component to a front-end site developed with React.js.
* To assist the user in registering, logging in and logging out on the front-end.
* To provide front-end users with CRUD (create, read, update and delete) functionality for posts found on the site.
* To allow users on the front-end to create, edit and delete their own comments and delete their own.
* To facilitate the functionality for front-end users to follow or un-follow other users in the community.
* To give regular users the opportunity to view tutorials added to the site.
* To allow only the site owner to add, edit or remove tutorials from the front-end.
* To allow for greater community interaction by giving users the opportunity to like or un-like posts.
* Provide filtered content for the front-end user based on whether they follow a user or have liked or favourited tutorials.
* Enhance the user experience integrated search function for those trying to find a specific user or post.
* Offer users the opportunity to provide more information about themselves by adding to their user profile. 

<hr>


### **User Stories:**

#### **Site User**
As a **Registered** user I can: 
* *sign in* in order to *view site content and interact with the community*.
* *navigate the site* easily in order to *view its content and interact with others*.
* *view posts by other users* in order to *take inspiration from the community*.
* *create a post* in order to *share my fitness journey with the community*.
* *update or delete a post* in order to *make changes to my own content or keep my contributions relevant*.
* *comment on other users' posts* in order to *share my opinions and interact with the community*.
* *update comments I make on posts or tutorials* in order to *contribute to, and interact with the community*.
* *upload a profile picture or bio* in order to *tell people a little more about myself*.
* *edit or update my profile* in order to *keep my account up to date*.
* *like or unlike a post* in order to *show my appreciation for other users' contributions*.
* *easily logout* in order to *end my session on the site*.
* *view tutorials* in order to *learn from content added by the site owner*.
* *follow or un-follow other users* so their *posts are added to my feed*.


As an **Unregistered** User I can:
* *sign up* in order to *view site content and interact with the community*.


#### **Site Admin**
As a **Site Admin** I can: 
* *add tutorials in the form of youTube videos* in order to *motivate and educate those in the community*.
* *edit or delete tutorials* in order to *correct mistakes or keep content relevant*.
* *view popular profiles within the community* in order to *see who is the most popular*.
* *respond to questions posted in comments* in order to *interact with and educate the community*.

<hr>

### **Wireframes**

No wireframes were required for the API. Wireframes for the front-end site can be found in the Readme.md file for that project.


<hr>

### **Database Schema**

I used [DrawSQL](https://drawsql.app)​ to help visualise my database tables. See the image below:

![Database Schema](docs/schema/barbelles-api-erd.png)

<hr>

### **Colour Scheme:**
​
No color scheme was required for this project. The color scheme for the front-end can be found in the Readme file for that project.

<hr>​

#### **Typography**
​
Typography was not required for this project. The typography for the front-end can be found in the Readme file for that project.

​<hr>

## Agile Development

I used Github projects to create and track issues and User Stories. The Agile processes and methodologies can be viewed [here](/AGILE.md)

<br>
<hr>
<br>

# **Features**

## **Site Navigation**

### **Admin Page**

The Admin page was setup almost immediately. This was crucial as it provided the initial means of adding test data and users to the project.

![Screenshot of admin page](docs/images/admin.png)

<hr>

### **Navbar**
​
The Navbar is a bootstrap component which allows a registered User to navigate their way around the site with ease. When logged out, it displays just the SF|Portal logo and social media / email links:

![Screenshot of navbar](docs/images/navbar-logged-out.png)

When the User is logged in, it offers navigation to the profile, books, authors and about pages:

![Screenshot of navbar](docs/images/navbar-logged-in.png)

To display properly on smaller screens, I used a Bootstrap hamburger menu:

![Screenshot of small-screen navbar](docs/images/navbar-small-screen-before.png)
![Screenshot of small-screen navbar menu](docs/images/navbar-small-screen.png)


<hr>

### Social Media and Email Links

The social media and email icons are situated on the right of the Navbar. The Social Media links are functional and will open in a new tab. 
**NOTE:** There is no actual Social Media Content for this site at the time of writing.

The email icon opens the default email application with the recipient being a test email address for the site.

![Screenshot of social media and email links](docs/images/social-media-links.png)


<hr>

### **Home Page**

The Home Page uses a background chosen to evoke sci-fi imagery and features a human figure standing in front of a Portal, thus linking neatly with the name of the site. It features some simple text outlining the purpose of the site as well as a search bar, which logged-in Users can use to search for content:

![Screenshot of home page](docs/images/sfp-home-page.png)

The Home Page is responsive and works well on smaller devices. This is how it looks on an iPhone SE:

![Screenshot of small-screen home page](docs/images/sfp-home-small.png)

Users can search for books using the search function:

![Screenshot of home page search](docs/images/sfp-search.png)

<hr>

### **Books Page**

The Books Page features a background image of stars which complements the overall colour palette of the site. It consists of a 'Submit Review' button and a paginated list of book reviews made by other Users or Admin. Each review is a Bootstrap card displaying the title, author and an image of the book. If no image is uploaded by the User, it is assigned a default image showing 'Image not available'. This can always be assigned by Admin or the User at a later time. The card also displays a snippet of the synopsis, a User rating, who posted the review the number of likes and comments. 

There are a maximum of six reviews per screen, the User can click 'next' or 'previous' to navigate between the reviews:

![Screenshot of book page](docs/images/books1.png)
![Screenshot of book page](docs/images/books2.png)

The Books page is responsive on smaller screens and the reviews will stack so they can be scrolled. The following screenshot is from an iPhone SE:

![Screenshot of small-screen book page](docs/images/books-small.png)

Assuming the User is logged in, they are able to edit or delete reviews they have posted directly from the Books Page:

![Screenshot of edit and delete book page](docs/images/books-buttons.png)

The User can click on any of the book titles or images to go to the Book Detail page and read that particular review.

<hr>

### **Book Detail Page**

Upon clicking on a review in the Books Page, the User is taken to the Book Detail page:

![Screenshot of book detail page](docs/images/book-detail1.png)
![Screenshot of book detail page](docs/images/book-detail-2.png)

This displays a larger image of the book - if uploaded, the book title, author, review rating and synopsis. The User review is situated below and there is also the opportunity for a User to edit or delete their own reviews. Users can also like or unlike reviews as well as see the number of both:

![Screenshot of book detail edit/delete/likes/comments page](docs/images/book-detail-likes.png)

***Likes***

The like button has two states: a [Font Awesome](https://fontawesome.com/) heart outline if the user has not liked the review:
<br>
![Screenshot of unliked](docs/images/book-likes-before.png)

or a solid heart if the user has liked it:

![Screenshot of liked](docs/images/book-likes-after.png)

The User can like or unlike a review.

<hr>

### **Add Book Page**

If a User clicks 'Submit a Review' they are taken to the Add Book Page:

![Screenshot of Add Book Page 1](docs/images/add-book-1.png)
![Screenshot of Add Book Page 2](docs/images/add-book-2.png)

The User must provide information for all fields in the form other than providing an image, rating and sub-genre. There are default values for the latter three but the User can still alter them.

Any mandatory form fields that are left blank will result in the following prompt:

![Screenshot of Add Book Form errors](docs/images/add-book-form-errors.png)

Upon successful submission of the form, the User is redirected to the Books Page and a message is displayed.


<hr>

***Comments***

Comments can be viewed below the reviews. This displays the User posting the comment, the date and time as well as the comment itself:

![Screenshot of book detail page comments](docs/images/book-detail-comments.png)

**NOTE** All comments must be approved by the Admin in order to filter out objectionable content.

In order to post a comment, the User must complete the comment form at the bottom of the page:

![Screenshot of book detail page comment form](docs/images/book-detail-comments-before.png)

Upon submission of the form, they are presented with the following message:

![Screenshot of book detail page comment submission](docs/images/book-detail-comment-after.png)

When the comment has been approved by the Admin, they will appear with the other comments in the order they were posted.

<hr>

### Edit Book Page

If the User clicks edit on the Books or Book Detail page then they are directed to the edit book page:

![Screenshot of edit book](docs/images/book-edit-1.png)
![Screenshot of edit book](docs/images/book-edit-2.png)

A User is only allowed to edit or delete an admin-approved review that they have posted. If these conditions are met, the edit book page will display a form pre-populated with the existing data from the initial review. This can be edited or updated. The primary reasons for doing so would be to edit typos pr perhaps add an image they couldn't find before.

Upon submission of the form, the User will be redirected to the Books page and shown a success message:

![Screenshot of successful edit book](docs/images/book-edit-success.png)

#### **Responsiveness**

The edit-book page is responsive and scales well on smaller devices. The screenshots below show how it renders on an iPhone SE:

![Screenshot of edit book small screen](docs/images/book-edit-smaller-1.png)
![Screenshot of edit book small screen](docs/images/book-edit-smaller-2.png)

<hr>


### Delete Book Page

If the user chooses to delete one of their book reviews, they are directed to the following page:

![Screenshot of delete book](docs/images/delete-book.png)

There are only two options: the User can click cancel and return to the previous page, or confirm delete of the review and are redirected to the books page where a message displays that the message has been successfully deleted. 

#### **Responsiveness**

Here is how the page displays on an iPhone SE:

![Screenshot of edit book page small screen](docs/images/delete-book-small.png)

<hr>


### Authors Page

If the User navigates to the Authors Page they can view a list of the Featured Authors:

![Screenshot of authors page 1](docs/images/authors1.png)
![Screenshot of authors page 2](docs/images/authors2.png)

This is an ever-growing list which will be to added by the admin over time. The layout is similar to the books page, with a paginated list of authors displayed. Each card displays the name, date of birth, famous works and a snippet of the author's bio. If no image is available, there is a default image displayed. In this instance, it is just for test purposes that there is no image of Isaac Asimov, as there were many available. This feature is reserved for more obscure or emerging artists for whom there might not be an image. The User can click on the image, author name or 'view full bio' link to navigate to the Author Detail Page.

#### **Responsiveness**

Here is how the page displays on an iPhone SE:

![Screenshot of authors page small screen](docs/images/authors-small.png)

<hr>


### Author Detail Page

The aim of this page is to introduce the User to new authors who might appeal to fans of the genre. These will include established authors and luminaries of the science fiction field or perhaps newer, emerging writers. For the purpose of consistency Author Detail Page is similar to the Book Detail Page. The same background image fits the sci-fi theme and the layout of the page features a large image of the author, their name, date of birth, famous works and a bio:

![Screenshot of author detail page 1](docs/images/author-det-1.png)
![Screenshot of author detail page 2](docs/images/author-det-2.png)

#### **Responsiveness**

Here is how the page displays on an iPhone SE:

![Screenshot of author detail page small screen](docs/images/author-det-small.png)

<hr>

### About Page

The About page displays information about the site. The text welcomes the User to the site and explains what they can do as a registered User. There are links to different areas of the site and a reminder to respect other Users in the community:

![Screenshot of about page ](docs/images/about.png)


#### **Responsiveness**

Here is how the page displays on an iPhone SE:

![Screenshot of about page small screen](docs/images/about-small.png)

<hr>


### Profile Page

When the User registers a new account, a profile is automatically created for them to edit in their own time. The purpose of this is so that the User can register and immediately start using the site rather than have to waste time completing a profile they may not wish to use. If the User wishes to, they can click on the Profile icon in the Navbar to view their Profile card:

![Screenshot of Profile page](docs/images/profile-card.png)

If the User clicks the 'Edit Profile' button, it will reveal a form which the User can use to update their details:

![Screenshot of Profile page edit form](docs/images/profile-form.png)

Upon clicking the 'Update' button, the form is submitted and the page reloads with the new details and a success message:

![Screenshot of profile page success](docs/images/profile-form-success.png)

#### **Responsiveness**

Here is how the page displays on an iPhone SE:

![Screenshot of profile page card small screen](docs/images/profile-card-small.png)
![Screenshot of profile page form small screen](docs/images/profile-form-small.png)

<hr>


## Allauth Account Pages

All Account Pages use the same background, again evoking sci-fi imagery. The image is a swirling, nebulous portal which again complements the colour palette used site-wide.

#### Sign Up

I used allauth to handle the account pages for the project. In order to register, the User must complete the form on the Signup Page:

![Screenshot of signup page](docs/images/signup.png)

Once the User has successfully registered, they will be logged in and taken to the Home Page. The form will display error messages in several circumstances:

* The User chooses a Username that is already taken
* The password is not long enough
* The password is too similar to the username or too common
* The passwords do not match

See the example below: 

![Screenshot of signup page errors](docs/images/signup-errors.png)

#### **Responsiveness**

Here is how the page displays on an iPhone SE:

![Screenshot of signup small screen](docs/images/signup-small.png)

<hr>

#### Log In

Existing Users can log in by clicking the Log In button on the Home Page. This will bring them to the Log In Page:

![Screenshot of log in page](docs/images/login-page.png)

If the log in details are not valid, an error message is displayed. For example: 

![Screenshot of log in page errors](docs/images/login-error-message.png)

#### **Responsiveness**

Here is how the page displays on an iPhone SE:

![Screenshot of login small screen](docs/images/login-small.png)
![Screenshot of login error small screen](docs/images/login-error-small.png)

<hr>


#### Log Out

To log out of the site and end the current session, the User can navigate to Log Out in the Navbar. This will direct them to the Log Out Page:

![Screenshot of logout page](docs/images/logout.png)

The User can confirm by clicking the Log Out button or click the cancel button to return to the previous page. If the User chooses to log out, they are redirected to the Home Page and a success message informs them they have been logged out:

![Screenshot of home screen logout success](docs/images/home-logout-success.png)

#### **Responsiveness**

Here is how the pages display on an iPhone SE:

![Screenshot of logout small screen](docs/images/logout-small.png)
![Screenshot of logout success small screen](docs/images/home-logout-success-small.png)


<hr>

## Links and Buttons

### **Links**

I used two different effects for the links in the project. One is a custom CSS effect where a white box-shadow slides from left to right across the link. The feature can be seen on the [site](https://sci-fi-portal.herokuapp.com/)

The second effect present is another custom CSS effect which changes the text-colour when it is hovered over. Generally there is no text decoration for the links as I felt the underline did not work well with either font.

### **Buttons**

I used Bootstrap buttons across the project. The button colours follow the colour scheme of the site, other than the 'edit' and 'delete' book buttons which use the default Bootstrap primary and danger colours in order to stand out.


<hr>

## **Messages**

User feedback is provided in the shape of success messages with the aim of providing a more involved User Experience. These messages are dismissible by clicking the 'x' and will be displayed in the following situations:

**Successful Login**

![Successful login message](docs/images/login-success.png)

**Successful Update Profile**

![Successful update profile](docs/images/profile-success.png)

**Successful Add Book Review**

![Successful add book message](docs/images/add-book-success.png)

**Successful Edit Book Review**

![Successful edit review message](docs/images/edit-success.png)

**Successful Delete Book Review**

![Successful login message](docs/images/delete-success.png)

**Successful Comment Submission**

![Successful Comment Submission message](docs/images/comment-success.png)

**Successful Logout**

![Successful logout message](docs/images/logout-success.png)


<hr>

## **Defensive Design**

In order to avoid the User unintentionally deleting their own content, some simple defensive design programming was implemented. If a User is logged in and clicks delete on one of their reviews, they will be prompted for confirmation they want to do so here:

![Screenshot of delete page](docs/images/delete-book.png)


<hr>

### User Authentication

All pages feature User Authentication meaning that a User must be logged in to view all site content. This encourages Users to signup as well as preventing malicious attempts to edit or delete content. If a user knows or guesses a correct URL without being logged in they will encounter this screen:

![Screenshot of authentication](docs/images/user-authentication.png)


<hr>

### **404 Page**

A custom 404 page was added to catch instances when the User may have mis-typed a URL, or if content has been removed from the site. The 404 page features text displaying the content is not available and features a back button:

![Screenshot of 404 page](docs/images/404.png)


<hr>

### **500 Page**

A custom 500 page was added to catch instances when a potentially malicious User might try to subvert the site, for example to access personal data or delete content. In this case the page below displays and features a back button to redirect them to the previous page:

![Screenshot of 500 page](docs/images/500-page.png)


<hr>

## **Future-Enhancements**
​
There are a number of areas with scope for future improvement. This project has been very challenging and ultimately the project deadline was looming. There is potential to add the following:
​
* Adding movies and games to fit into a 'Categories' drop-down menu.
* The option for Users to add to the Authors section.
* User images to be added to comments and book reviews.
* A community page for User who opt in to have their profiles displayed publicly.
* The search function to be updated to display results in the new categories.
* Using the Google Books API to retrieve book information. I did explore this option before the inception of the project but decided against including it due to time constraints.

<hr>

## User Authentication

All pages feature User Authentication meaning that a User must be logged in to view all site content. This encourages Users to signup as well as preventing malicious attempts to edit or delete content. If a user knows or guesses a correct URL without being logged in they will encounter this screen:

[Screenshot of authentication](docs/images/user-authentication.png)

<hr>

## **Testing Phase**

The testing process, along with bugs, can be viewed [here](/TESTING.md)​

<hr>

## **Deployment**

The Deployment was a fairly lengthy process so I have detailed it in a separate file. It can be found [here](/DEPLOYMENT.md)

The final deployment can be viewed [here](https://sci-fi-portal.herokuapp.com/)

<hr>

## **Software and Tech**

The following software and tech was used:

- [BootStrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) to provide key components such as the navbar and cards.
- [Cloudinary](https://cloudinary.com) to handle static images and files as well as to offer the User a front end method of uploading images.
- CSS to provide custom styling in addition to Bootstrap.
- [Django](https://www.djangoproject.com/) as a Python framework to develop the project.
- [Django all auth](https://django-allauth.readthedocs.io/en/latest/) used to handle user authentication.
- [DrawSQL](https://drawsql.app/) to develop the logic for the project.
- [ElephantSQL](https://www.elephantsql.com/) to handle the PostgreSQL database.
- [Figma](https://www.figma.com/) to assist with the planning phase of the project.
- [Font Awesome](https://fontawesome.com/) to provide search, heart, profile, social media icons etc.
- Git (Gitpod and Github) as my version control for the site.
- [Gitpod](https://gitpod.io/) and VS Code to create, load and push my code to Github.
- [Heroku](https://www.heroku.com/) to deploy the project.
- HTML - The base language to create templates for the site
- JavaScript - only used twice: for the back or cancel buttons and to populate the hidden created_by field in the add_book form.
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) used to implement logic from views.py and models.py.
- Microsoft Excel to develop the logic for the project.
- [Optimizilla](https://imagecompressor.com/) to compress background images for the site.
- Python - Installed packages can be found in the requirements.txt file.
- [Shutterstock](https://www.shutterstock.com/) to source the background images for the site.
- [Summernote](https://summernote.org/) to provide a WYSIWYG text editor in the admin area.

<hr>

## **Media**

* All book images are from [Amazon UK](https://www.amazon.co.uk/)
* All background images came from a free trial subscription to [Shutterstock](https://www.shutterstock.com/)
* All author images and bios are from [Wikipedia](https://www.wikipedia.org/) other than:
  * N.K. Jemisin: bio and image from [author website](https://nkjemisin.com/)
  * Adrian Tchaikovsky: bio taken from [author website](https://adriantchaikovsky.com/)
​
<hr>

## **Credits**

* The colour palette for the project is from [Pinterest](https://www.pinterest.co.uk/pin/204491639320145500/).

* The idea to use Cloudinary to handle static and media files came from the [Code Institute](https://codeinstitute.net/) walkthrough project: 'I Think, Therefore I Blog.

* The [Django Documentation](https://docs.djangoproject.com/en/4.1/) was immensely helpful in helping me gain a greater understanding of the project.

* The JavaScript code used to populate the hidden created-by field in the 'add book' form came from [this](https://www.youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) series of videos by John Elder on YouTube.

* [This Post](https://www.section.io/engineering-education/uploading-images-to-cloudinary-from-django-application/) from Shuaib Oseni was helpful when it came to creating the front end method to upload an image to CLoudinary.

* The idea to automatically create the User Profile came from [this article](https://groups.google.com/g/django-users/c/cvbuURVHN0w) on Google Groups.

* General References:
  * Stack Overflow
  * Code Institute LMS
  * Bootstrap Documentation
  * Jinja Documentation
  * Cloudinary Documentation
  * Geeks for Geeks
  * W3C School
  * Course material on the CodeCademy website which helped reinforce my understanding of Python.

<hr>

## **Honourable mentions**

* The biggest thank you goes to my mentor, Richard Wells, who gave a significant amount of his time to provide me with help, feedback and ideas on the project; he has been invaluable in so many ways and a genuine source of motivation for me.
* Thanks to the Code Institute team for providing me with some basic knowledge of Python and Django.
* Thanks to the Code Institute who helped me overcome a major bug in the final deployment of the project
* Thanks to the Code Institute community on Slack who helped remind me that everyone has difficult days.
* A huge thank you to my family who support my coding journey on a daily basis.

<hr>

Links to additional related files: [AGILE.md](/AGILE.md) | [DEPLOYMENT.md](/DEPLOYMENT.md) | [TESTING.md](/TESTING.md)