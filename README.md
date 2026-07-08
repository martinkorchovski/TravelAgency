# Travel Agency

Проект за туристичка агенција што го изработивме со Django (бекенд) и Vue 3 (фронтенд).

## Технологии што ги користев
- **Backend:** Django, Django REST Framework, Simple JWT (за автентикација), django-cors-headers, PostgreSQL
- **Frontend:** Vue 3 + TypeScript, Vite, Pinia, Vue Router, Tailwind CSS

## Структура на проектот
-travel-agency-backend/    # Django API - апликации: destinations, bookings, users, hotels, reviews...
travel-agency-frontend/   # Vue 3 апликација - views, components, stores, api

## Како да се стартува апликацијата

**Backend**
```bash
cd travel-agency-backend
python -m venv venv && source venv/bin/activate
pip install django djangorestframework djangorestframework-simplejwt django-cors-headers psycopg2-binary
python manage.py migrate
python manage.py runserver
```

**Frontend**
```bash
cd travel-agency-frontend
npm install
npm run dev
```

## Алатки што ги користевме за развој
- Backend го работев во **PyCharm**
- Frontend го работев во **Visual Studio Code**, со Vue.volar екстензија
