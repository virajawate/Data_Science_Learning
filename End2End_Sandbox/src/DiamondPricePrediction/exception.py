import sys

class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()
        
        
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
    
    def __str__(self):
        return "Error occured in the file name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message))
    
if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e :
        raise CustomException(e, sys)
        