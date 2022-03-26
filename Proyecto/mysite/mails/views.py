from django.shortcuts import render
from mails import Mail
# import threading

    thread = threading.Thread(target=Mail.send_complete_order, args=(
        order, request.user
    ))
    thread.start()


