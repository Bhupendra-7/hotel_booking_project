Hotel Booking System - Django Project

This is a simple hotel booking system built using Django that allows users to:

- View all available hotel rooms
- See details of each room
- Book a room via a booking form
- View both available and unavailable rooms on the homepage
- Manage rooms and bookings via the Django admin panel

Project Structure
Project Name:** `hotel_booking_project`  
App Name:** `booking`


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





   
   
