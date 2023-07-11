# Library

![Python](https://img.shields.io/badge/Python-316192?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-7952B3?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white).

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
   ![pageLogin](https://github.com/Andessonreis/library-py/assets/105820333/1d1f1e69-7774-41f3-8980-3aaad187c807)

- Registration Page
   ![Registration Page](https://github.com/Andessonreis/library-py/assets/105820333/429014f2-6d21-42ca-8393-b2bc9db42944)

- Home Page
   ![Home](https://github.com/Andessonreis/library-py/assets/105820333/647975ff-44c0-442a-8567-8887dc862222)

- Book Record
   ![register](https://github.com/Andessonreis/library-py/assets/105820333/eabe2e47-16ce-4806-9d64-9addb4ea5331)

- Book View Page
   ![bookview](https://github.com/Andessonreis/library-py/assets/105820333/8c612619-0e88-47aa-92f8-a777d0d0536d)

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

If you encounter any issues or have any questions, please [open an issue](https://github.com/Andessonreis/library-py/issues). We're here to help!

## Creator

This project was created by [Andesson Reis](https://github.com/Andessonreis).

## License

This project is licensed under the terms of the MIT license. Please refer to the [LICENSE](LICENSE) file for more information.
