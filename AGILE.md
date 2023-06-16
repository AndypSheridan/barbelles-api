# Agile Methodologies

* **Agile Methodologies**
  * [Overview](#overview)
  * [Sprint Notes](#sprint-notes)
    * [Sprint 1](#sprint-1)
    * [Sprint 2](#sprint-2)
  * [Epics](#epics)
  * [Learning Outcomes](#learning-outcomes)

<hr>

## **Overview**

This was my second project developed using Agile Methodologies and I encountered challenges, and some occasional confusion, along the way. The first challenge was the plethora of information I had absorbed in a short space of time. I was attempting to apply a number of Agile methods and use various different platforms to help the planning process: 

I used a [Smartsheet](https://www.smartsheet.com) template to help plan six sprints for this project:

![Sprint Planning 1](docs/agile/barbelles-api-sprint-1.png)

![Sprint Planning 2](docs/agile/barbelles-api-sprint-2.png)

I used the Github [project board](https://github.com/users/AndypSheridan/projects/3) to create and track issues and User Stories. I then integrated these within my Smartsheet template.

This proved instrumental in keeping me focused on tasks and creating the necessary features for the project. As this was only my second experience of using Github projects, I found that on several occasions I underestimated or overestimated the amount of time and/or tasks for each particular sprint but, on the whole, the schedule worked well. Using the Milestones feature I created Epics in Github and to these I added my User Stories, although I had already begun work on the by this point. I also created labels for the project was extremely helpful when it came to prioritising requirements for the project. 

It has been a steep learning curve, and I felt that my plan was continually evolving rather than being something I rigidly adhered to. On reflection, I consider this to be a good thing in some respects.

Sprints 1 and 2 were where I carried out all of the work on the API and I have outlined a brief summary of these below.


<hr>

### *Sprint 1*

* 7th - 12th May
  * Planning phase

The purpose of this five day sprint was to thoroughly plan the project. This involved an initial meeting with the client, Kate Ross, to discuss her expected outcomes of the project. This was the first in a series of highly productive meetings where we looked at core functionality of what the finished site might have. Miss Ross was hoping to be the owner of a content-sharing website where female clients could share their fitness journeys away from the regular social media sites, thus creating a more private community. The outcome of this meeting was that the finished site would implement the following features: user posts, tutorials provided by the site owner, the facility to comment on both tutorials and posts, to like and save both, as well as a feature for users to follow other members of the community and view posts by those they follow.

This meeting was instrumental in determining the database models to be used in the project, see below:

![Database models](docs/schema/barbelles-api-schema.png)

We settled on nine models to provide the features that had been discussed. At the end of the sprint, a second meeting with the client was arranged where we decided we were happy that these models would be sufficient and it was time to move on to the next sprint.

### *Sprint 2*

* 12th - 19th May
  * Sprint two was slightly longer and the intention was to start and finish work on the API.

With the data models in place, work on the back-end started well, gradually building out the functionality for actions that would be performed by the user on the front-end. CRUD functionality for all agreed features was in place, and all API endpoints were covered. Details of the back-end-only testing can be found [here](/TESTING.md)

In order for the front-end to connect to the API, it was also necessary to deploy the API via Heroku. This is a fairly lengthy process which is detailed [here](/DEPLOYMENT.md)

At the end of this sprint, a third consultation where I demonstrated the functionality of the deployed API, helping the client visualise how this would translate to actions performed on the front-end site.

This concluded sprint two; further details of subsequent sprints and the entire process can be found in the Readme for the front-end project.

<hr>

## **Epics**

To assist with the development process of the project, it was divided into seven Epics using Github Milestones: each representing a feature of the project as a whole. All User stories were assigned to an Epic and are summarised below.

![Epics Summary](docs/agile/barbelles-epic-summary.png)

<br>

### 1. Comments

All CRUD functionality for comments on both posts and tutorials.

![Comment Epic Summary](docs/agile/barbelles-epic-comments.png)
<br>

### 2. Followers

All CRUD functionality for the followers feature.

![Followers Epic Summary](docs/agile/barbelles-epic-followers.png)
<br>

### 3. Navigation and Authentication

All User Stories relating to navigating the front-end site as well as signing up, signing and signing out are grouped in the Epic below:

![Navigation and Authentication Epic Summary](docs/agile/barbelles-epic-nav-auth.png)
<br>

### 4. Posts

All CRUD functionality for the posts feature.

![Posts Epic Summary](docs/agile/barbelles-epic-posts.png)
<br>

### 5. Presentation

Presentation-related User Stories were linked to this milestone.

![Presentation Epic Summary](docs/agile/barbelles-epic-presentation.png)
<br>

### 6. Profiles

All CRUD functionality for the profiles feature.

![Profiles Epic Summary](docs/agile/barbelles-epic-profiles.png)
<br>

### 7. Tutorials

All CRUD functionality for the tutorials feature.

![Tutorials Epic Summary](docs/agile//barbelles-epic-tutorials.png)
<br>

<hr>

## Learning Outcomes

I have enjoyed this project and it has been a wonderful learning experience. I think this second attempt using Agile methodologies has set me on a course I look forward to refining and developing continually. Working on a back-end and front-end to deliver an overall project has been enormously challenging but the methodologies outlined in this file have helped keep me focused and on-track even when it has felt overwhelming at times.


<hr>

[Back to Readme](/README.md)