"""
main.py
Lambda {{ parameters.function_name }} function
"""
import logging

def main(event, _):
    """
    main function
    """
    logging.info("Running {{ parameters.function_name }}")
    return "Hello from {{ parameters.function_name }}!"
