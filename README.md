
# Glow On You SPA(Single Page Application)


Glow On You(Glow) is inspired by "Glow And Grow" from GA. 
GA SEI cohorts share feedback - glow(something ) & grow(something to improve) with each other on our projects.
Glow app allows users to share Glow (more positive messages!) by creating a board with a title/topic(i.e. "J - Graduation Project") that many other users can leave glow messages on. 

- - - -




## Planning, process and problem-solving strategy


- Day 1: Planning - User stories, Wireframes, ERD, front end/back end repo setup, catalog of routes, and building backend model schema and serializers
- Day 2: Working details of back end functionality - relationships between resources
- Day 3: Front end page views and basic outline for styling of application
- Day 4: Deploy front end and back end




## User Stories


- As an unregistered user, I would like to sign up with email and password.
- As a registered user, I would like to sign in with email and password.
- As a signed in user, I would like to change password.
- As a signed in user, I would like to sign out.
- As a signed in user, I would like to create/update/delete a board
- As a signed in user, I would like to view a single or multiple boards I created
- As a signed in user, I would like to create/update/view/delete a glow message on the board
- As a signed in user, I would like to view a single or multiple glow messages of the board




## ERD 


- User - Board : one to many relationship/ many to many relationship
- User - Glow: One to many relationship
- Board - Glow: one to many relationship

![ERD](https://i.imgur.com/i1tsy7V.png)




## WireFrames


![wireframe1](https://i.imgur.com/KxaLnXr.png)
![wireframe2](https://i.imgur.com/dweAeh1.png)
![wireframe3](https://i.imgur.com/SbWGbAF.png)
![wireframe4](https://i.imgur.com/G5yzgL7.png)


## Glow On You API


| HTTP Method   | URL Path      | Result              | 
|:--------------|:--------------|:--------------------| 
| GET           | /home         | index of boards     | 
| POST          | /boards       | create boards       | 
| GET           | /boards/`:id` | show single board   | 
| PATCH         | /boards/`:id` | update board        | 
| DELETE        | /boards/`:id` | delete board        |

| HTTP Method   | URL Path      | Result              |
|:--------------|:--------------|:--------------------|
| POST          | /glows        | create glow         |
| GET           | /glows/`:id`  | show single glow    |
| PATCH         | /glows/`:id`  | update glow         |
| DELETE        | /glows/`:id`  | delete glow         |



## Important Links


- [Project Front End Repo](https://github.com/JeheeChoi/Glow-client)
- [Project Back End Repo]
- [Deployed API]
- [Deployed Client]




## Technologies Used


- Python
- Django(SQL)
- PostgreSQL
- REST framework
- Git/GitHub
- Postman



