import logging

# Create a custom logger_obj  
logger=logging.getLogger(__name__)

#Setting the threshold of logger to DEBUG  
logger.setLevel(logging.INFO)

#formatting the output
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler= logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)

# Add handlers to the logger_obj  
logger.addHandler(file_handler)

#Create and configure logger using the basicConfig() function  
#logging.basicConfig(filename="employee.log",level=logging.INFO,
#format='%(asctime)s:%(levelname)s:%(message)s')

class Employee:
    """Employee class """

    def __init__(self,first,last):
        self.first=first
        self.last=last

        logger.info("Employee name is : {} {}".format(self.first,self.last))

if __name__=="__main__":
    emp1=Employee('Kanchan','Jaiswal')
    emp2=Employee('Priya','Jaiswal')

