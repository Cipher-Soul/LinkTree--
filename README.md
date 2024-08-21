
# LinkTree☘️ --Django Project

<p>A simple Django-based application inspired by [Linktree](https://linktr.ee/). This project allows users to create a personalized page with links to their social profiles, websites, or any other URLs.</p>

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Running the Project](#running-the-project)
- [Deployment](#deployment)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication (sign up, login, logout)
- Customizable link page (add, edit, remove links)
- Drag-and-drop ordering of links
- Simple analytics for tracking link clicks
- Mobile-friendly design

## Demo

You can try a demo of the application at [Demo URL](https://example.com).

## Prerequisites

Before setting up the project, ensure that you have the following installed on your machine:

- Python 3.x
- Django 4.x
- PostgreSQL (or other supported database)

  
## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Cipher-Soul/LinkTree--/
    cd LinkTree--
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database and apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser for the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

6. Collect static files:

    ```bash
    python manage.py collectstatic
    ```


