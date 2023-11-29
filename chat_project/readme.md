# Chat Web Application with WebSocket

Welcome to the Chat project using WebSocket.

## Getting Started

To get started, follow these steps:

1. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:

    - **On Windows:**

      ```bash
      .\venv\Scripts\activate
      ```

    - **On macOS/Linux:**

      ```bash
      source venv/bin/activate
      ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations and create the database:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to start using the application.

## Registration

For full functionality, register in the system. After registration, the following features will be available:

- Create chat rooms
- Participate in chat rooms
- View profiles of other participants
- Send private messages to other participants

## API Usage

This chat application also provides a RESTful API. To test it, you can use [httpie](https://httpie.io/). Install it with:

```bash
pip install httpie

- http GET http://127.0.0.1:8000/api/group-chats/
## Author


The project is developed by Vladislav Varaksin.