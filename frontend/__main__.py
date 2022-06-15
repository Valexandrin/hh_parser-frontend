from frontend.app import create_app
from frontend.config import config


def main():
    app = create_app()
    app.run(
        port=config.server.port,
        host=config.server.host,
        debug=False,
    )


if __name__ == '__main__':
    main()
