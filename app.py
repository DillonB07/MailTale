from utils.env import env
from utils.slack import app


if __name__ == "__main__":
    app.start(port=env.port)
