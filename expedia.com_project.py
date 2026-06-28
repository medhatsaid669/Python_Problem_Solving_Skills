# Expedia.com Project

"""Python Programming
Expedia.com Project
Functional Requirements
● In expedia, a user creates several itineraries, each itinerary consists of
several reservations as following
○ 0 or more flights, hotels, cars, etc. E.g. 4 flights, 2 hotels and 2 cars.
● Each reservation may has its own info
○ E.g. Hotel cost: total nights x price per night
● The itinerary cost = sum of its inner reservations
● For simplicity
○ Don’t use files / Use dummy data when convenient + store in memory
○ 2 types of users: Admin & customer. Focus of your code is on Customer part
○ Don’t burn time validating inputs or minor concerns
○ The core goal is OOP design skills
APIs
● Expedia needs to contact several APIs
● Flights APIs
○ Companies such as AirCanada, TurkishAirlines and others allow them to do online query to
get current available flights
○ Then after the customer make a choice, you ask them to cancel/reserve
● Hotel APIs: In a similar way, hotels such as Hilton, Marriott provide APIs
● Payments: Expedia uses one of the payments APIs (e.g. Square/Stripe, etc)
● Follow the homework. Your code should be loosely coupled with these APIs
● Your code should be extensible: Future similar APIs might be used
● Content of the APIs is not hours. Put dummy data to simulate
● APIs code is given. Download it.
Login interface
● I added a dummy user to use for login
○ Do proper validation for the login part
○ Initially, skip sign up
● The user can do 4 major actions
○ Step 2 and 3 are major goals
● Let’s make an itinerary (choice 2)
Make itinerary Interface
● The user can add 0 or more flights. Same for hotels
○ This menu will keep appearing to add as much as the user wants
● The user can reserve all added items or cancel all
○ Once user is done, he either choose 3 or 4
● Let’s add an hotel (choice 2)
Add hotel
● Enter hotel info. Search through hotel APIs and list them, then user choose
● In a similar way, we can do the add flight
5
Add flight
Reserve and Pay
● If the user decided to reserve the itinerary, then he should pay
● The customer profile has added payment cards. Let him choose
More on payment logic
● Let’s say the user itinerary is 2 flights and 3 hotels reservation
● First, sum the total cost of all of them. Say $5000
● Contact the payment API to pay money
○ It may fail if no enough money or any network/system error
○ If it passed, start to reserve the 5 reservations
■ Say after reserving 2 flights and 1 hotel, then next reservation failed!
● You need to cancel the payment
● You need to cancel the 3 reservations
● For simplicity: assume cancellation always works with no issues
● You may raise reasonable exceptions for different errors
Listing your itineraries
● So far we have 1. Let’s print it
Flights APIs: AirCanada
Hotels APIs: Hilton
Payment APIs: Paypal
Tip
● Although the whole project looks big, but consider:
○ We did homework about payment and reservation to prepare for the project
○ The idea of the different airlines & hotel is exactly the same. Once you implemented one of
them properly, all others are matter of copy-paste
■ E.g. finish Air-Canada Flight part first properly
○ The goal of having these similar parts is to force you build extensible code
■ E.g. later we add Car and Cruise reservation
○ Another goal is to learn build common interfaces for close behaviours
○ And another goal to structure your code in several (sub)-packages
● Something missing? Make your own assumptions
Code Structure: High Level
● Split your code to backend and front end
○ Backend: core logic. NEVER print to user from it
■ Think backend is a remote machine
■ User: using his own web browser or mobile
○ Frontend: Where use sees the screen
■ Menu options, selections and printing
● Next
○ Last slide: optional
○ My code overall structure
Code Structure: Low Level
● You don’t have to follow that
● Don’t bother why such file names/split
● Just in case it is inpsiring"""