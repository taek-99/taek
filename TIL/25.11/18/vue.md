1. vue 세팅
npm install @headlessui/vue
npm install @heroicons/vue
npm install tailwindcss @tailwindcss/vite
npm install vue-router
npm install axios


2. 장고 cors 세팅
- pip install django-cors-headers
- MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware',]  추가
- CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",] 주소 등록