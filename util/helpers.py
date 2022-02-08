# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
License: MIT
"""

import os, csv

'''
This file should contain primitoves used in other modules
'''

def h_list_to_s( aList, aSeparator=',' ):
    if isinstance(aList, list):
        return aSeparator.join([str(elem) for elem in aList])
    else: 
        return aList

def file_exists( aPath ):

    try:

        if open( aPath, 'r'):
            return True

    except:
        return False   


def file_p( aPath ):

    try:

        f = open( aPath, 'r') 
        
        if f:
            return f

        return None 
    except:
        return None   

def file_read( aPath, as_list=False ):

    try:

        if not file_exists( aPath ):
            return None

        f = open( aPath, 'r')
        if f:

            if as_list:
                content = f.readlines()
            else:
                content = f.read()    
            
            f.close()
            return content

    except UnicodeDecodeError as err:

        return None

    except:
        return None

def file_write( aPath, aContent, isAppend=False ): 

    try:

        f = None

        if file_exists( aPath ):
            if isAppend:    
                f = open( aPath, 'a+')
            else:
                f = open( aPath, 'w+')    
        else:
            f = open( aPath, 'w+')

        if not f:
            return False

        f.seek(0) 
        f.write( aContent )
        f.truncate()
        f.close()

        return True

    except IOError:
        return False

    except:
        return False

def list_write( aPath, aList, isAppend=False ): 

    # if not isinstance(aList, list):
    #    return False

    aContent = ''

    for item in aList:
        
        aContent += item + os.linesep

    return file_write( aPath, aContent, isAppend)
