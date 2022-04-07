"""
main.py
Lambda {{cookiecutter.function_name}} function
"""
import logging

def main(event, _):
    """
    main function
    """
    logging.info("Running {{cookiecutter.function_name}}")
    return "Hello from {{cookiecutter.function_name}}!"
