# Examination Platform API

## Details

The Examination Platform is a robust system for efficient exam management within educational institutions. It features distinct user roles - administrators, instructors, and students. The platform ensures secure authentication, comprehensive user data management, and effective exam handling. With an intuitive interface, it prioritizes user-friendly design and scalability to accommodate growth. Results access control is implemented, and considerations include audit trails, notifications, and data integrity. The platform aims to streamline examination processes, providing a reliable and user-centric solution.

<div align="center">
   <img src="./assets/images/cover.jpg">
</div>

## ⚙ Tools and Technologies used

1. **[Python](https://www.python.org/)**: Primary programming language chosen for its simplicity, readability, and vast ecosystem of libraries and frameworks.
2. **[Django](https://www.djangoproject.com/)**: A high-level Python web framework renowned for its scalability, security features, and rapid development capabilities.
3. **[Django Rest Framework (DRF)](https://www.django-rest-framework.org/)**: Built on top of Django, DRF provides powerful tools for building RESTful APIs, simplifying the creation of web services.
4. **[PostgreSQL](https://www.postgresql.org/)**: A robust open-source relational database management system known for its reliability, extensibility, and support for complex queries and transactions.
5. **[JWT (JSON Web Tokens)](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)**: A standard for securely transmitting information between parties as JSON objects, commonly used for authentication and authorization in web applications.
6. **[Docker](https://www.docker.com/)**: Containerization platform that simplifies the deployment and management of applications by packaging them into portable containers, ensuring consistency across different environments.
7. **[Docker Compose](https://docs.docker.com/compose/)**: Tool for defining and running multi-container Docker applications, enabling seamless configuration and orchestration of complex application architectures.

## 🛠 Installation and setup

1. Install Docker [here](https://www.docker.com/get-started/)
2. Install Git [here](https://git-scm.com/downloads)
3. Create a working directory:

   ```bash
   mkdir ~/MAAT && cd ~/MAAT
   ```

4. Clone the repository

   ```bash
   git clone https://github.com/ak4m410x01/Examination_Platform_API.git .
   ```

5. Start the application

   ```bash
    docker-compose up -d
   ```

6. Access API: http://127.0.0.1/api/

7. Access DB: 127.0.0.1:5432

8. Don't forget .env file with variables

| Variable          | Value                                                                 |
| ----------------- | --------------------------------------------------------------------- |
| SECRET_KEY        | 'django-insecure-%2dmqnqj9v2e&8yk\*t=#b+2-=i!45+153*@-g0*=&%1od16z^m' |
| DEBUG             | False                                                                 |
| ALLOWED_HOSTS     | 172.0.0.1,\*                                                          |
| DATABASE_ENGINE   | django.db.backends.postgresql                                         |
| DATABASE_HOST     | postgres                                                                    |
| DATABASE_PORT     | 5432                                                                  |
| DATABASE_NAME     | maat                                                                  |
| DATABASE_USER     | maat                                                                  |
| DATABASE_PASSWORD | maat                                                                  |
| JWT_SECRET_KEY    | JWT_S3CR3T_K3Y                                                        |
| POSTGRES_DB       | maat                                                                  |
| POSTGRES_USER     | maat                                                                  |
| POSTGRES_PASSWORD | maat                                                                  |

note:
these variables are for the lab environment only... don't use these in xxx production environments xxx

---

## 🛠 Documentation and Endpoints

1. [Postman](https://documenter.getpostman.com/view/27192844/2sA2xnxA2s)
2. [Apidog](https://3ew4wjhnzp.apidog.io/)

---

## PIP Packages

    +-------------------------------+---------+---------------------------+
    | Name                          | Version | Use                       |
    | ----------------------------- | ------- | ------------------------- |
    | Python                        | 3.11.7  | Programming Lang          |
    | Django                        | 5.0.2   | Django Framework          |
    | djangorestframework           | 3.14.0  | Restful Framework         |
    | djangorestframework-simplejwt | 5.3.1   | Restful Framework Jwt     |
    | django-filter                 | 23.5    | Restful Framework filters |
    | django-cors-headers           | 4.3.1   | Restful Framework CORS    |
    | psycopg2-binary               | 2.9.9   | PostgreSQL DB lib         |
    | pthon-decouple                | 3.8     | To use .env file          |
    +-------------------------------+---------+---------------------------+
