FROM python:3-slim-buster as builder

WORKDIR "/app"

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --no-input


FROM nginx

COPY --from=builder /app/staticfiles /usr/share/nginx/html
