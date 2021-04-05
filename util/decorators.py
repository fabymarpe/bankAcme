import sys, os, functools
from inspect import getframeinfo, stack
from util import logger


def log_decorator(_func=None):
    def log_decorator_info(func):
        @functools.wraps(func)
        def log_decorator_wrapper(self, *args, **kwargs):
            # Build logger object
            logger_obj = logger.get_logger(log_file_name=self.log_file_name)

            args_passed_in_function = [repr(a) for a in args]
            kwargs_passed_in_function = [f"{k}={v!r}" for k, v in kwargs.items()]
            formatted_arguments = ", ".join(args_passed_in_function + kwargs_passed_in_function)

            logger_obj.info(f"Function Name: {func.__name__} - Arguments: {formatted_arguments} - Begin function")
            try:
                value = func(self, *args, **kwargs)
                logger_obj.info(f"Returned: - End function {value!r}")
            except Exception as e:
                logger_obj.error(f"Exception: {str(sys.exc_info())}")
                raise
            return value
        return log_decorator_wrapper
    if _func is None:
        return log_decorator_info
    else:
        return log_decorator_info(_func)