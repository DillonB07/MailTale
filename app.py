from utils.slack import app

import os

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
