Com certeza! Aqui está o arquivo README.md traduzido para o inglês:

```markdown
# Library

[![Python](https://img.shields.io/badge/Python-3.9-blue?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.2-green?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple?style=flat&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Contributing](#contributing)
- [Support](#support)
- [Creator](#creator)
- [License](#license)

## Description

This repository contains the Library project, a web application developed with Django and Bootstrap. The application is a library management system, allowing users to register, edit, delete, and loan books. The project also includes advanced security features, such as login validations and access control.

## Features

- Login Page: allows users to log in to the application with security validations.
- Home: displays general information and menu options for authenticated users.
- Registration: allows new users to register in the application.
- Book View: shows the details of a specific book, only for the owner user.
- Book Registration: allows registering a new book in the library.
- Book Edit: allows editing the information of an existing book, if the user is the owner.
- Book Deletion: allows deleting a book from the library, with user access control.
- Book Loan: allows lending a book to another user and marks the book as borrowed.
- Book Return: enables the return of a borrowed book, updating the return date.
- Category Registration: allows registering book categories for organization.

## Screenshots

Here are some screenshots of the application:

- Login Page
![Login Page](screenshots/login.png)

- Registration Page
![Registration Page](screenshots/registro.png)

- Home Page
![Home Page](screenshots/home.png)

- Book View Page
![Book View Page](screenshots/book_view.png)

## Installation

1. Make sure you have Python 3.9 installed. If not, you can download it from [python.org](https://www.python.org/).

2. Clone this repository to your local machine:

```bash
git clone https://github.com/Andessonreis/library-py.git
```

3. Navigate to the project directory:

```bash
cd library-py
```

4. Create a virtual environment and activate it:

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

5. Install the project dependencies:

```bash
pip install -r requirements.txt
```

6. Run Django migrations to create the database:

```bash
python manage.py migrate
```

7. Start the development server:

```bash
python manage.py runserver
```

8. Open your browser and go to [http://localhost:8000](http://localhost:8000) to view the application.

## Contributing

Contributions to the Library are welcome! If you have any suggestions, bug reports, or would like to contribute code, please contact the project creator at andessonreys@gmail.com.

## Support

If you

 encounter any issues or have any questions, please [open an issue](https://github.com/Andessonreis/library-py/issues). We're here to help!

## Creator

This project was created by [Andesson Reis](https://github.com/Andessonreis).

## License

This project is licensed under the terms of the MIT license. Please refer to the [LICENSE](LICENSE) file for more information.
```

I hope you find this helpful! Let me know if there's anything else I can assist you with.