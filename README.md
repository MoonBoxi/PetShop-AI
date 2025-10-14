# GeminiPet: A Case Study in Rapid Prototyping with Django and Generative AI

**[Live Demo Link Here]**

## Project Summary

GeminiPet is a functional e-commerce prototype for a pet supply store, developed as a practical case study on applying Generative AI (Google Gemini) within the software development lifecycle. The goal was to simulate the creation of a complex platform—from database architecture to user interface—in a drastically reduced timeframe.

**Prototype Development Time:** Approximately 2-3 hours.

---

## The Role of Artificial Intelligence in the Process

This project was not "made by AI," but rather **directed by a developer using AI as a core productivity tool.** My role in the process involved:

1.  **Requirements Definition:** Architecting the project's concept, its features, and the technology stack (Django, Bootstrap).
2.  **Prompt Engineering:** Translating the requirements into clear, detailed, and sequential instructions for the Gemini CLI to guide the creation of models, views, templates, and business logic.
3.  **Code Debugging and Refactoring:** Analyzing the generated code, identifying issues (e.g., logic bugs, lack of proper styling, missing features), and creating refinement prompts to correct and enhance the output.
4.  **Integration and Manual Testing:** Setting up the environment, running database migrations, seeding the database (also with AI assistance), and testing the user flow to ensure all components worked together seamlessly.

This approach demonstrates a modern workflow focused on agility and the ability to deliver high-quality, functional prototypes in record time.

---

## Features Implemented

* Product Catalog with Categories
* Product Detail Pages
* Dynamic Homepage Banner System (manageable via Django Admin)
* Functional Search Bar
* User Authentication (Register, Login, Logout)
* Session-based Shopping Cart
* Database seeded with fake data for demonstration purposes.

---

## Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Database:** SQLite
* **AI Tool:** Google Gemini CLI
* **Data Seeding:** Faker Library (Python)

---

## Running the Project Locally

1.  Clone the repository: `git clone [YOUR_REPO_URL]`
2.  Create and activate a virtual environment.
3.  Install dependencies: `pip install -r requirements.txt`
4.  Apply migrations: `python manage.py migrate`
5.  (Optional) Seed the database with sample data: `python manage.py seed_data`
6.  Start the development server: `python manage.py runserver`