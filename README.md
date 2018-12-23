# Estimate Your Group Travel for RMOTR Final Project
This is still a work in progress.


# SCOPE

<strong>Early Nov 2018:</strong>
I first tried to do something a little more complex with having a place for the user to request bids to the vendor (supplier) and then the vendor signs in and submits their bid. However, although I would wanted to do this idea I quickly released that I wouldn't be done by the time the project deadline came around. Therefore, I decided to just have the user (agent) fill out the responses he/she received from the vendor to receive the quote. The reason for this idea is that this is a type of thing that is done manually and would like to automate so I thought why not do a final project based on what I already know.

<strong>Mid Nov 2018:</strong>
I started to run into issues with understanding how the models work with the one-to-one, many-to-many, foriegn key, etc. I then watched everything from the advanced classes in RMOTR to what I could find online from Youtube or Udemy. I even got the user forms to be similar to the admin forms with a "+" button that after clicked would use javascript to receive a pop up. I then tested this with a modal, which I may go back to in the future. However, due to time, I wanted to finish the form. Now, when creating a "New Estimate", the user will be taken from one from to another by the use of Class Based Views (these are like magic). I can't say enough great things about Django's Documentation (https://docs.djangoproject.com/en/2.1/), however, I also want to say that I used the following email as well to understand Class Based Views even better: https://ccbv.co.uk/projects/Django/2.0/.

<strong>Early Dec 2018:</strong>
I was running into a problem with my models when I tried to use Many to Many and "through" (https://docs.djangoproject.com/en/2.1/topics/db/models/#extra-fields-on-many-to-many-relationships), because I was also trying to have a foreign key for the id in the wrong model. Instead of using the Many to Many "through" method, I ended up flattening out the forms/models and was able to fix the issue.

<strong>Mid Dec 2018:</strong>
I've submitted my final project and have it available to see here on Heroku - https://group-travel-estimator.herokuapp.com/. I still need to update the PDF to have the actual estimate, a send button that will show the estiamte first with a detailed view in a modal then will allow them to just send everything without dowloading the PDF and sending manually. Also, I need to allow the user to add additional flight legs, and options for each section per group section. I am not sure if I'll do this by a button at the button of the form asking if they would like to create another (with a max of 3 for options and 6 for flight legs). 

# THOUGHTS
I want to say that this experience has been a great one. Learning with other students and from teachers that are experts on the subject beats trying to figure out coding on your own from Youtube or Udemy. I'm not saying these are not great sources because they are and I use them all the time. It was the class that forced me to build something on my own that I started actually understand how all the peices connected. I'm still far from being a pro, but it was here that I made a huge jump on my knowlege of Python & Django. Thanks!
