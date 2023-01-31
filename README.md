# course_project
This project implemented two django applications
- Shop
- Sklad

In the shop, the client can register, view books, add to his cart, select the required number of books to purchase and place an order. Created with Django.

The sklad is implemented so that the store receives up-to-date information about the fulfillment of the order and the availability of books. Sklad created with Django Rest Framework.

Synchronization happens with Celery in Celery_Beat
Two periodic tasks to synchronize the number of books and update the status of orders.

The framework works with Docker. To start, you need to run two commands:
  - docker-compose build
  - docker-compose up
