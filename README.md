# NanoURL – API that makes long URLs short 🔗

This is a minimalist URL Nanofier built with Django + Django REST Framework (DRF).  
You send a long URL, get back a short one. You send a short one, get back the original.

Easy to implement a redirect to make Nano URLs work.

---

## ✨ Features

- `POST /nanofy/` – submit a long URL, receive a short nano URL  
- `POST /resolve/` – submit a nano URL, get the original long URL  

---

## API Endpoints

### Nanofy an URL

**POST** `/nanofy/`  
**Body:**

```json
{
  "original_url": "https://example.com/super/long/path/that/you/want/to/nanofy"
}
```

### Reverse NANOFY

**POST** `/resolve/`  
**Body:**

```json
{
  "nano_url": "https://example.com/nano_url"
}
```

---

# QUICKSTART

1) git clone https://github.com/paweldobkowski/nanourl.git
2) cd nanourl
3) python -m venv venv
4) source venv/bin/activate  # or venv\Scripts\activate on Windows
5) pip install -r requirements.txt
6) python manage.py migrate
7) python manage.py runserver

---

# 💼 Author
Made by Paweł Dobkowski for __Szkoła W Chmurze__