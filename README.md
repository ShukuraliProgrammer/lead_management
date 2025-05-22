# 🧾 Lead Management Application


---

## 🧱 System Design

![System Design Diagram](https://i.postimg.cc/PrNGyhsW/Copy-of-lead-management-sys-design-drawio.png)

You can also view the full interactive system design diagram here:  
🔗 [View System Design](https://app.diagrams.net/?splash=0#G11fVxeiPvarrCkrntGL6YLDcO9IEQavrz#%7B%22pageId%22%3A%22ZP3VNHhl2aMxR3FIKjDi%22%7D)


> **Note:**  
> While the current implementation does **not** include external file storage (e.g., AWS S3 or MinIO),  
> the system design diagram includes this component to illustrate a scalable architecture for future enhancements.

---

## 🗃️ Database Design

![Database Design](https://i.postimg.cc/fL6Hv4xK/Lead-management-db-design.png)

You can view the live diagram here:  
🔗 [View on dbdiagram.io](https://dbdiagram.io/d/Lead_management_db_design-682f1361b9f7446da3b003ae)


## 🔌 API Endpoints

### 📥 Public API

- `POST /api/leads/submit/`  
  Submit a new lead form (first name, last name, email, resume).


- `POST /api/accounts/login/`  
  Log in to get authentication token (usually returns tokens(user_id, role, token)).


### 🔐 Internal API (Requires Authentication)

- `GET /api/leads/`  
  Retrieve a list of all leads.


- `PATCH/PUT /api/leads/<id>/`  
  Update lead status (e.g., mark as "REACHED_OUT").


---

### 📄 API Documentation

You can access the full interactive API docs via Swagger here:  
[http://localhost:8004/swagger/](http://localhost:8000/swagger/)


## ⚙️ Installation Guide

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed
- [Docker Compose](https://docs.docker.com/compose/install/) installed

---

### Steps

1. **Clone the repository**

```bash
git clone https://github.com/ShukuraliProgrammer/lead_management.git
cd lead-management
```

2. **Create environment variables**
```bash
cp .env.example .env
# Edit .env file with your preferred editor
```

3. **Build and start containers**
```bash
 docker-compose up --build
```

**Optional: Running tests**
```bash
docker-compose exec web python manage.py test
```

### Notes
- Make sure the ports (default 8004 for Django, 5432 for PostgreSQL, 6379 for Redis) are free on your machine.

- Adjust settings in .env as needed