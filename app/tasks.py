from celery import Celery

app = Celery('tasks', backend='amqp', broker='amqp://')

@app.task
def pager(ids, msg, data):
    for user in data['recipientList']:
        msg.pager(id=user)
        msg.message(data['message'])
        code, message = msg.help()
        msg.send()

    if code == 250:
        from app.testdict import memory_data
        memory_data[ids-1]['status'] = 'processed'
        print memory_data


    return 'processed' and msg.quit()
