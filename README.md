# Todo Manager

## Overview

Todo Manager is a Django-based application that allows users to manage their tasks. It provides features such as creating, listing, and uploading photos for tasks. Additionally, it includes algorithmic endpoints for rotating arrays, finding the k-th largest element, and determining the longest increasing path in a matrix.

## Features

- Create and list tasks
- Upload photos for tasks
- Update and delete tasks
- Get task with closest due date
- Rotate array endpoint
- K-th largest element endpoint
- Longest increasing path endpoint

## Installation

To get started with the Todo Manager, follow these steps:

1. **Clone the repository**:

   ```sh
   git clone https://github.com/VaclavJirka/todo_manager.git
   cd todo-manager
   ```

2. **Create a virtual environment**:

   ```sh
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations**:

   ```sh
   python manage.py migrate
   ```

5. **Run the development server**:
   ```sh
   python manage.py runserver
   ```

## Usage

Once the server is running, you can access the application at `http://127.0.0.1:8000/`. Use the following endpoints to interact with the application:

### Task Endpoints

- **Create Task**: `POST /api/tasks/`
- **List Tasks**: `GET /api/tasks/`
- **Retrieve Task**: `GET /api/tasks/<id>/`
- **Update Task**: `PUT /api/tasks/<id>/`
- **Delete Task**: `DELETE /api/tasks/<id>/`
- **Nearest Due Task**: `GET /api/tasks/nearest-deadline/`

### Leetcode Endpoints

- **Rotate Array**: `POST /api/leetcode/rotate-array/`
- **K-th Largest Element**: `POST /api/leetcode/kth-largest/`
- **Longest Increasing Path**: `POST /api/leetcode/longest-increasing-path/`

## Testing

To run the tests for the application, use the following command:

```sh
python manage.py test
```
