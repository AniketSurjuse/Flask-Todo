# Flask ToDo App

This is a simple To-Do application built with Flask, a lightweight web framework for Python. The app allows users to manage their tasks by adding, updating, and deleting items on their to-do list.

## Getting Started

### Prerequisites

Make sure you have the following installed on your machine:

- Python (version 3.6 or higher)
- Flask (install it using `pip install Flask`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/flask-todo-app.git
   cd flask-todo-app
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the application:

   ```bash
   flask run
   ```

   The app will be accessible at `http://localhost:5000` in your web browser.

2. Open the app in your web browser and start managing your to-do list.

## Features

- **Add Task:** Enter a new task and click "Add" to add it to your to-do list.

- **Update Task:** Click on a task to mark it as completed or update its details.

- **Delete Task:** Click on the delete icon next to a task to remove it from your list.

## Project Structure

- **app.py:** The main application file containing the Flask application setup and routes.

- **templates/:** This directory contains HTML templates for the application.

- **static/:** Static files (CSS, JavaScript) used in the application.

- **requirements.txt:** List of Python packages required for the project.

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. Your feedback and contributions are highly appreciated.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)

Happy task managing!
