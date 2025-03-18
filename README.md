# FastAPI Side Hustles & Money Quotes API

## Overview
This is a simple FastAPI project that provides two endpoints:
- `/side_hustles` - Returns a random side hustle idea.
- `/money_quotes` - Returns a random money-related quote.

The project is designed to be lightweight and can be deployed on **Vercel** using `vercel.json` configuration.

## Technologies Used
- **FastAPI** - A modern, fast (high-performance) web framework for Python.
- **Vercel** - A platform for frontend frameworks and static sites, that also supports Python backend services.
- **Python** - The core programming language used for the API.

---

## Project Structure
```
📁 fastapi-side-hustles-api
│── 📄 main.py  # Main FastAPI application
│── 📄 requirements.txt  # Dependencies for the project
│── 📄 vercel.json  # Configuration for deploying on Vercel
│── 📄 README.md  # Project documentation
```

---

## FastAPI Endpoints
### Root Endpoint
- **URL:** `/`
- **Method:** GET
- **Response:**
  ```json
  {
    "message": "Hello World, Go to /side_hustles or /money_quotes to get a random side hustle or money quote"
  }
  ```

### Get Random Side Hustle
- **URL:** `/side_hustles`
- **Method:** GET
- **Response Example:**
  ```json
  {
    "side_hustle": "Remote Tutoring - Teach students online from anywhere!"
  }
  ```

### Get Random Money Quote
- **URL:** `/money_quotes`
- **Method:** GET
- **Response Example:**
  ```json
  {
    "money_quote": "An investment in knowledge pays the best interest. – Benjamin Franklin"
  }
  ```

---

## Installation & Running Locally
1. **Clone the repository:**
   ```sh
   git clone https://github.com/muzaffar401/FAST-API.git
   cd FAST-API
   ```
2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the FastAPI app:**
   ```sh
   uvicorn main:app --reload        
   ```
   or
    ```sh
   fastapi dev main.py         
   ```
5. Open the browser and go to:
   ```
   http://127.0.0.1:8000
   ```

---

## Deployment on Vercel
### Step 1: Install Vercel CLI
If you haven’t installed the Vercel CLI yet, install it using npm:
```sh
npm install -g vercel
```

### Step 2: Login to Vercel
```sh
vercel login
```

### Step 3: Initialize the Project on Vercel
Run the following command inside the project folder:
```sh
vercel
```
Follow the prompts and select the necessary configurations.

### Step 4: Deploying with vercel.json
Ensure you have a `vercel.json` file in the project root with the following content:
```json
{
    "version": 2,
    "builds": [
        {
            "src": "./main.py",
            "use": "@vercel/python"
        }
    ],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "/main.py"
        }
    ]
}
```

Then deploy the project:
```sh
vercel --prod
```

### Step 5: Verify Deployment
Once deployment is complete, Vercel will provide a live URL. You can access the API using:
```sh
https://your-vercel-project-url.vercel.app
```
Test the endpoints by navigating to:
- `https://your-vercel-project-url.vercel.app/side_hustles`
- `https://your-vercel-project-url.vercel.app/money_quotes`

---

## Conclusion
You have now successfully set up and deployed your FastAPI project on Vercel. Enjoy building APIs with FastAPI! 🚀

