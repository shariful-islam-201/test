import logging

logging.basicConfig(filename='logs/cal.log', encoding='utf-8', level=logging.DEBUG, filemode="a", format='%(asctime)s - %(levelname)s : %(message)s')

class D_Log():
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b


result = D_Log()
summ = result.add(7, 8)
subtract = result.sub(20, 9)
multiply = result.mul(9, 8)



logging.debug("Results of sum: {}, subtraction: {}, multiplication: {}".format(summ, subtract, multiply))
logging.warning("Results of sum: {}, subtraction: {}, multiplication: {}".format(summ, subtract, multiply))
logging.info("Results of sum: {}, subtraction: {}, multiplication: {}".format(summ, subtract, multiply))
logging.critical("Results of sum: {}, subtraction: {}, multiplication: {}".format(summ, subtract, multiply))
logging.error("Results of sum: {}, subtraction: {}, multiplication: {}".format(summ, subtract, multiply))


#logging.critical("Results of sum: %0.2f, subtraction: %0.2f, multiplication: %0.2f" % (summ, subtract, multiply))

##print("Results are: %0.2f %0.2f %0.2f" % (summ, subtract, multiply))
