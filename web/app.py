from main import create_app
from main.config import Config

app = create_app()

if __name__ == "__main__":
	app.run(host=Config.APP_HOST, port = Config.APP_PORT, threaded=True)