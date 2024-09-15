def handle_subscription(ack, respond, body):
    ack()
    print("Running subscription command")
    respond("You can't manage your subscription yet!")
