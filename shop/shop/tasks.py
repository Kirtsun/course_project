from celery import shared_task


@shared_task
def foo(x, y):
    print('Hello')
