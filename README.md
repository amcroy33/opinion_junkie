# capstone_movie_rating_site

# Overview
As a movie lover and someone with strong opinions, I want to create a platform where users have the ability to rank and review movies and in turn, be able to choose new movies to watch based on others' recommendations. The project will be built in Django and will utilize an IMDb API. The name of the site will be *Opinion Junkie*.

# Features

As an Admin, I want the user to login.

### Tasks:
- Create database model to store user information
- Create user login page


As a user, I want to be able to view ranked movies by 'all time' as well as 'genre' and 'release year'.

### Tasks:
- Create database of movies
- Create header bar with logo and website title (spanning entire page)
- Create homepage that displays default of 'Top ranked movies of all time'
- Create buttons (in LH column) to filter by genre and release year

As a user, I want to be able leave ratings and reviews on any movie of my choice.

### Tasks:
- Create database model for reviews
- Create a link for each movie, that allows users to leave reviews
- Create ranking system that allows users to rank each movie
- Create add and delete button for each review

As a user, I want to be able to look at my personal ratings and reviews.

### Tasks:
- Create a link (in top RH corner) to click and redirect to user profile
- Create user profile page that displays user ratings and reviews

### Additional Features:
- Utilize IMDb API to host live movies facts such as main characters, release date and overview

# Data Models
- User
    - id
    - first_name (charfield)
    - last_name (charfield)
    - email (charfield)
    - reviewID (foreignKey to review table)

- Review
    - id
    - post (textfield)
    - movieID (foreignKey to movie table)

- Movie
    - id (foreignkey to review table)
    - title (charfield)
    - release_date (charfield)
    - genre (charfield)

# Schedule
## Week 1
- Create and clone repo
- Create virtual enviornment
- Start Django project
- Set up user model, create superuser
- Set up Movie model, create a movie in the admin panel
- Create a url, view and template for the movie list view
- Style the movie tile for the list view

## Week 2
- Create url, view and template for movie detail page, style movie details on the page (the reviews for the movie will be rendered on this page later)
- Repeat steps 2-4 for the Review model
- Create form to create review (this will be rendered on the movie detail page also)
- Create view to process review creation form


## Week 3
- On movie detail page, make HTTP request to the imdb to get additional movie data

# Future Features
- Add Books, TV Shows, Games, etc
- Algorithm that recommends movies to each user based on their interactive history