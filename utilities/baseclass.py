import logging

import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        logger = logging.getLogger(__name__)  # __name__ to   generate test case name

        filehandler = logging.FileHandler("/Users/sujeetkumarsharma/Desktop/PythonSelfFrameWork/SeleniumEnd2End/reports/logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)  # filehandler object

        # setting the level

        logger.setLevel(logging.INFO)
        return logger
