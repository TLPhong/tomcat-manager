import controller

flask_application = controller.app

if __name__ == '__main__':
    flask_application.debug = True
    flask_application.run()
