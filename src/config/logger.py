import logging

class Logger:
    # set up logging to file
    logging.basicConfig(
        format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )

    # add the handler to the root logger
    logging.getLogger('').addHandler(
        logging.StreamHandler()
        .setFormatter(
            logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')))

    logging.getLogger(__name__)

    def logError(self, message: str):
        logging.error(message)

    def logInfo(self, message: str):
        logging.info(message)