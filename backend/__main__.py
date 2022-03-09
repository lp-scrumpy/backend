import logging
from flask import Flask, Blueprint
from backend.users import user

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info("application started")
    app.run(host='0.0.0.0', port=8080, debug=False)

app = Flask(__name__)
app.register_blueprint(user, url_prefix='/api/u/users')

if __name__ == '__main__':
    main()