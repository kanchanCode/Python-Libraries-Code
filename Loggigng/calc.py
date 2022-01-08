import logging 
#using logging module

import employee
'''
USAGE OF LOGGING
Logging is a means of tracking events that happen when some software runs.

Logging is beneficial to store the logging records. Suppose there is no logging record, 
and the program is interrupted during its execution, we will be unable to find the actual cause of the problem.

LELVES IN LOGGING
0 NOTSET
10 DEBUG: Detailed info when any problems diagnosed
20 INFO: Confirmation that things are working as expected
30 WARNING: Something unpexpected happened indication but things are working as expected
40 ERROR: Due to some serious problem , the software has not been able to perform func.
50 CRITICAL: A serious error, indicating that the program itself may be unable to continue running

DEFAULT LEVEL is warning 
'''

# Create a custom logger_obj  
logger=logging.getLogger(__name__)

#Setting the threshold of logger to DEBUG  
logger.setLevel(logging.DEBUG)

#formatting the output
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

#handling file 
file_handler= logging.FileHandler('test.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

#to print output in console also
stream_handler= logging.StreamHandler()
stream_handler.setFormatter(formatter)

# Add handlers to the logger_obj  
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

#Create and configure logger using the basicConfig() function  
#logging.basicConfig(filename='test.log',level=logging.DEBUG,
#format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

def add(x,y):
    """Add function """
    return x+y

def sub(x,y):
    """Subtract function """
    return x-y

def mul(x,y):
    """Multiply function """
    return x*y

def div(x,y):
    """Divide function """
    try:
        result=x/y
    except ZeroDivisionError:
        #logger.error("Invalid input 0")
        logger.exception("Invalid input 0")
    else:
        return x//y

if __name__=="__main__":
    a=40
    b=0

    add_result=add(a,b)
    sub_result=sub(a,b)
    mul_result=mul(a,b)
    div_result=div(a,b)

    
    # print("Add",add_result)
    # print("Subtarct",sub_result)
    # print("Multiply",mul_result)
    # print("Division",div_result)

    logger.debug('Add :{} + {} = {}'.format(a,b,add_result))
    logger.debug('Subtract:{} - {} = {}'.format(a,b,sub_result))
    logger.debug('Multiply:{} * {} = {}'.format(a,b,mul_result))
    logger.debug('Division:{} / {} = {}'.format(a,b,div_result))