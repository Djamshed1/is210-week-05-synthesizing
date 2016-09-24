#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a function that will return current date."""

import datetime

CURDATE = None

def get_current_date():
    """This fucntion displays the current date.

    Args:
        None
        
    Return:
     date: current computer time will be returned.

    Example:
    >>>CURDATE
    datetime.date(2016, 9, 24

    >>> task_01.get_current_date()
    datetime.date(2016, 9, 24)
    """
    
    return datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
