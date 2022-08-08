__doc__ = """
https://docs.djangoproject.com/en/4.0/topics/logging/
"""

DEBUG = "DEBUG"
INFO = "INFO"
WARNING = "WARNING"
ERROR = "ERROR"
CRITICAL = "CRITICAL"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "utc": {
            # NOTE: you need to include the pythonfile in the classname
            "()": "logger.UTCFormatter",
            "format": "[%(asctime)s.%(msecs)03dZ] %(levelname)s : %(name)s : %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S",
        }
    },
    "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "utc"}},
    #
    # root is default logger
    "root": {"handlers": ["console"], "level": WARNING},
    #
    "loggers": {
        #
        # Define logger
        #
        "azure.identity": {
            "level": WARNING,
        },
        "akvq": {
            "level": DEBUG,
        },
    },
}
