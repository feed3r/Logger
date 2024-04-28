import unittest
from logger import logger

def checkLog(filepath, word):
    try:
        with open(filepath, 'r') as file:
            for line in file:
                if word in line:
                    return True
        return False
    except FileNotFoundError:
        print(f"File '{filepath}' not found.")
        return False



class TestLogger(unittest.TestCase):
    def printOnFile(self):
        log = logger.Logger("./logger.test.log")
        log.info("info")
        log.debug("debug")
        log.warning("warning")
        log.error("error")
        log.critical("critical")



    def testPrintLog(self):
        self.printOnFile()
        self.assertTrue(checkLog("./logger.test.log", "info"))
        self.assertTrue(checkLog("./logger.test.log", "debug"))
        self.assertTrue(checkLog("./logger.test.log", "warning"))
        self.assertTrue(checkLog("./logger.test.log", "error"))
        self.assertTrue(checkLog("./logger.test.log", "critical"))



if __name__ == '__main__':
    unittest.main()
