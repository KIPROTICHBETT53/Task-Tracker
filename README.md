https://roadmap.sh/projects/task-tracker
Task Tracker CLI
A simple command-line interface (CLI) application to manage and track tasks. It allows you to add, update, delete tasks, and manage their status.

Features
Add, update, and delete tasks.
Mark tasks as not done, in progress, or done.
List tasks based on their status.
Store tasks in a JSON file to persist data between sessions.
Prerequisites
Python 3.x installed.
You can check your Python version by running:

bash
Copy code
python --version
Git (optional, if you want to clone the repository):

bash
Copy code
git --version
Installation
Clone the repository (or download the project files):

bash
Copy code
git clone https://github.com/KIPROTICHBETT53/Task-Tracker.git
cd Task-Tracker
(Optional) Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate      # On macOS/Linux
.\venv\Scripts\activate       # On Windows
Verify Python installation: Ensure Python is installed and working correctly by running:

bash
Copy code
python --version
Usage
Make sure you are in the project directory, then use the following commands to interact with the CLI:

1. Add a New Task
bash
Copy code
python app.py add "finish project"
2. List All Tasks
bash
Copy code
python app.py list
3. Update Task Title
bash
Copy code
python app.py update <index> "new task title"
Example:

bash
Copy code
python app.py update 0 "Finalize the report"
4. Update Task Status
bash
Copy code
python app.py status <index> <status>
Status options: not done, in progress, done
Example:

bash
Copy code
python app.py status 0 done
5. Delete a Task
bash
Copy code
python app.py delete <index>
Example:

bash
Copy code
python app.py delete 0
6. List Tasks by Status
List all tasks that are done:

bash
Copy code
python app.py list-done
List all tasks that are not done:

bash
Copy code
python app.py list-not-done
List all tasks in progress:

bash
Copy code
python app.py list-in-progress
How it Works
When you add or update tasks, they are stored in a tasks.json file located in the same directory.
If the JSON file does not exist, it will be created automatically on the first run.
Tasks are identified by their index in the list, starting from 0.
Troubleshooting
If you encounter an error saying 'python' is not recognized as an internal or external command, ensure Python is added to your system's PATH.
Use python3 instead of python if your system requires it:
bash
Copy code
python3 app.py add "task example"
Example Session
Add a task:

bash
Copy code
python app.py add "Complete project"
List tasks:

bash
Copy code
python app.py list
Output:

bash
Copy code
0. Complete project - not done
Update task status:

bash
Copy code
python app.py status 0 in progress
List tasks in progress:

bash
Copy code
python app.py list-in-progress
Output:

markdown
Copy code
0. Complete project - in progress
License
This project is licensed under the MIT License.
