# Django Services with OIDC-based SSO and Load Balancing

This project demonstrates how to create two Django services that are authenticated using OpenID Connect (OIDC)-based Single Sign-On (SSO) and implement JWT-based authorization. The services are load balanced using Nginx.


### Prerequisites

- Python 3.x
- Django
- Nginx



### Configuration

1. **Auth0 Setup:**

    - Create an Auth0 account
    - Create an OIDC Application and note down the client ID, client secret, and callback URL.
    - Update `myproject/settings.py` with your Auth0 credentials.

2. **Nginx Configuration:**

    - Install Nginx on your server.
    - Configure Nginx to load balance between Service A and Service B. Update the Nginx configuration file.

3. **Run Django Services:**

    ```bash
    python manage.py runserver 8000  # Service A
    python manage.py runserver 8001  # Service B
    ```

4. **Access the Services:**

    - Service A: [http://localhost:8000/service_a/](http://localhost:8000/service_a/)
    - Service B: [http://localhost:8001/service_b/](http://localhost:8001/service_b/)



