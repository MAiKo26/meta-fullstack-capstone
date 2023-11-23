# Meta Full Stack Course Project - Little Lemon Booking System

## Project Overview

This project is the culmination of the Meta Full Stack Course, where I implemented a dynamic booking system for the Little Lemon restaurant website. The system is built using Django, Django Rest Framework (DRF), and JavaScript to handle form components dynamically.

## Key Features

- **Reservation Form:** Users can easily make reservations by entering their name, selecting a reservation date, and choosing an available time slot.
  
- **Dynamic Updates:** The system dynamically updates the available time slots based on the selected date, preventing duplicate bookings and ensuring a smooth user experience.

- **API Integration:** The project integrates with an API to fetch and display current reservations for a specific date, allowing users to view real-time booking data.

## Technologies Used

- **Django:** The web framework used for the back-end development.
  
- **Django Rest Framework (DRF):** Employed to build a robust API for handling reservations.

- **JavaScript:** Used to implement dynamic form interactions and handle user inputs.

- **MySQL:** The database management system used to store reservation data.

## Setup Instructions

### Prerequisites

- [Install Python](https://www.python.org/downloads/)
  
- [Install MySQL](https://dev.mysql.com/downloads/)

### Installation

1. Clone the repository: `git clone https://github.com/MAiKo26/meta-thefullstack-course.git`

2. Navigate to the project directory: `cd meta-thefullstack-course`

3. Ensure that you change the python versions in pipfiles to your version

4. Add your MySQL settings to littlelemon/settings.py

5. Create a virtual environment: `pipenv shell`

6. Install dependencies: `pipenv install`

7. Run migrations: `python manage.py makemigrations` and `python manage.py migrate`

8. Start the local server: `python manage.py runserver`

9. Access the application at [http://localhost:8000](http://localhost:8000)

