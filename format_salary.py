# This module is built for college graduate degree earnings

def format_salary(salary):
    """Takes a salary string ($xx,xxx.xx) and returns an integer"""

    return int(float(salary.replace('$', '').replace(',', '')))
