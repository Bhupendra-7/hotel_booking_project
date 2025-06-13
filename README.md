Hotel Booking System - Django Project

This is a simple hotel booking system built using Django that allows users to:

- View all available hotel rooms
- See details of each room
- Book a room via a booking form
- View both available and unavailable rooms on the homepage
- Manage rooms and bookings via the Django admin panel


Features Implemented
- List all available hotel rooms on the homepage  
- View details of a single room  
- Book a room with customer info and booking dates  
- Mark rooms as unavailable after booking  
- Display unavailable rooms below available rooms on the homepage  
- Admin panel for managing rooms and bookings  
- Basic HTML templates with Django templating  
- Form validation including date fields with date picker inputs
  

Project Structure
Project Name: `hotel_booking_project`  
App Name: `booking`


Setup Instructions
1. Clone the repository
   bash
   git clone https://github.com/Bhupendra-7/hotel_booking_project.git

2.Create and activate a virtual environment
python -m venv taskenv
# Windows
taskenv\Scripts\activate
# macOS/Linux
source taskenv/bin/activate


3.Install dependencies
pip install django

4.Apply migrations
python manage.py migrate

4.Create a superuser (admin account)
The one which is already created is Username - admin, Password - admin123, email - admin@email.com
python manage.py createsuperuser

Run the development server
python manage.py runserver

Access the application
Homepage: http://localhost:8000/
Admin panel: http://localhost:8000/admin/





   
   
