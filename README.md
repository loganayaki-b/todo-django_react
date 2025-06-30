# 📝 Todo List Application

A full-stack todo list application with a **Django backend** and **React frontend**, integrated with **MongoDB** for persistent storage and built with a clean, modern UI using **Tailwind CSS**.

## Features

### ✨ Core Features
- ➕ **Add Tasks**: Add tasks with title and description
- ✅ **Mark Completed**: Instantly mark tasks as complete
- ✏️ **Edit Tasks**: Edit any task details with ease
- 🗑️ **Delete Tasks**: Remove tasks from your list
- 🧹 **Clear Completed**: Remove all completed tasks at once

### 🎯 Advanced Features
- 🔍 **Search & Filter**: Filter by all, pending, or completed
- 🎨 **Priority Tags**: (Coming soon) Color-coded priority levels
- 📅 **Due Date Warning**: (Coming soon) Highlights overdue tasks
- 🌙 **Dark/Light Mode**: Switch themes instantly
- 🏷️ **Task Labels**: (Coming soon) Tag tasks by type
- 📱 **Responsive UI**: Mobile-friendly design
- 🖱️ **Interactive UI**: Hover effects, visual indicators
- 💾 **MongoDB Storage**: Save tasks persistently

## Tech Stack

### Backend
- **Django 5.x**: Backend server
- **PyMongo**: Connects Django with MongoDB
- **MongoDB**: NoSQL database
- **Django CORS Headers**: Enable cross-origin access

### Frontend
- **React 19+**: UI framework
- **Tailwind CSS**: Utility-first styling
- **Fetch API**: Communicate with backend
- **React Hooks**: State management

## Project Structure

project-root/
├── backend/
│ ├── views.py # Django views (CRUD for tasks)
│ ├── urls.py # API routes
│ └── ...
├── frontend/
│ ├── src/
│ │ ├── components/ # Todo UI components
│ │ ├── App.js # Main component
│ │ └── index.js # Entry point
│ └── public/
└── mongodb/ # MongoDB setup (local/Atlas)

markdown
Copy
Edit

## Setup Instructions

### Prerequisites
- Python 3.10+
- Node.js 18+
- MongoDB installed or Atlas account

### Backend Setup

1. Create a virtual environment:
```bash
python -m venv venv
Activate it:

bash
Copy
Edit
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install django pymongo django-cors-headers
Start Django server:

bash
Copy
Edit
python manage.py runserver
API available at: http://localhost:8000/tasks/

Frontend Setup
Navigate to frontend:

bash
Copy
Edit
cd frontend
Install dependencies:

bash
Copy
Edit
npm install
Start React app:

bash
Copy
Edit
npm start
App opens at: http://localhost:3000/

API Endpoints
Method	Endpoint	Description
GET	/tasks/	Get all tasks
POST	/tasks/	Create a new task
PUT	/tasks/<id>/	Update a task
DELETE	/tasks/<id>/	Delete a task

Usage Guide
➕ Add Task
Fill in the task title and description

Click "Save" to create the task

✅ Manage Tasks
Complete: Click checkbox

Edit: Click ✏️ icon

Delete: Click 🗑️ icon

🎨 UI Features
Light/Dark mode toggle

Colored badges for task status

Responsive layout for all devices

Development Notes
Backend built with class-based views

MongoDB integrated using PyMongo

React frontend uses functional components and hooks

Styled entirely with Tailwind CSS

Contributing
Fork this repository

Create a feature branch

Commit and push your changes

Open a pull request

License
This project is licensed under the MIT License.

Support
For issues or questions, open an issue in the repository.



