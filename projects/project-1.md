---
layout: project
type: project
image: images/micromouse.jpg
title: iRoutePlanner
permalink: projects/iRoutePlanner
# All dates must be YYYY-MM-DD format!
date: 2019-03-10
labels:
  - iOS App Development
  - Swift
summary: My team developed an iOS App that finds the shortest route to take when given a list of addresses the user would like to visit.
---

<div class="ui small rounded images">
  <img class="ui image" src="../images/micromouse-robot.png">
  <img class="ui image" src="../images/micromouse-robot-2.jpg">
  <img class="ui image" src="../images/micromouse.jpg">
  <img class="ui image" src="../images/micromouse-circuit.png">
</div>

Engineers at the University of Hawaii at Manoa have to do a "Senior Design Project" where they collaborate with a group of people and professors in order to create a product that they believe consumers would utilize.  Project leaders have to design a product, gather a team to implement the project idea, and then present their product to a group of professors.  The product that our project leader decided on was an iPhone application that can take in the user's starting location and then a list of locations that the user would like to visit.  The application will then compute the shortest route the user can take in order to get to each location.

For this project, I was the lead Graphical User Interface (GUI) designer.  My resposibility was to create a user interface that easily allowed the user to input their current location, and create a list of locations for the purpose stated above.  The user is able to add and delete locations using this app, but there is no functionality to reorder to locations, since the order would be modified later once the application calculates the shortest path.  Once the path is created, the user can look at the directions to each location on Google Maps.  As you visit each location, you can remove them from the list, and the app will recalculate the shortest path the user should take based on the left over locations.  This way, if the user decides to visit a location out of order, it will be taken into consideration (as well as other factors such as time of day and traffic).

<a ref = "https://github.com/bmwfire-tsp/senior-design-project/">Github Repo</a>
