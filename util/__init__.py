# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
License: MIT
"""

from util.helpers import *

from datetime import datetime
from random import seed, randint
from faker import Faker

import pandas as pd

def test():
    print( 'working!' )

'''
Info: Load a CSV file 
Input:
  - aPath: file path
Output:
  - File contents (if found)
  - None on error  
'''
def csv_load( aPath ):

    try:

        if not file_exists( aPath ):
            return None

        return csv.reader( file_p( aPath ) )   

    except:
        return None   

'''
Info: Print a CVS file
Input:
  - aPath: file path
Output:
  - File contents (if found)
  - Error message (file not found) 
'''
def csv_print( aPath, aLimit=None ):

    try:

        csv_content = csv_load( aPath )

        if not csv_content:

            print( ' > Error Reading CSV File [' + aPath + ']' )
            return

        iter = 0 # used for timestamp
        for row in csv_content:

            if aLimit and iter > aLimit:
                return        

            iter += 1            
            row_str = ','.join([str(elem) for elem in row])
            
            print( row_str )

    except:
        return

'''
Info: Remove Column
Input:
  - aPath: file path
  - aColName: column to remove
  - aReturnContent:
    - False: the original file is updated
    - True: Leave input intact and return content
Output:
  - New File contents (if found)
  - Error message 
'''
def csv_col_remove( aPath, aColName, aReturnContent=False ):

    try:

        aContent    = ''
        csv_content = csv_load( aPath )

        if not csv_content:

            print( ' > Error Reading CSV File [' + aPath + ']' )
            return

        header = next(csv_content)     # ignore header (1st line)

        if not aColName in header:
            s = h_list_to_s( header )
            print( ' > Error: [' + aColName + '] not found in header [' + s + ']' )
            return

        index = header.index( aColName )

        # Remove index from header
        del header[ index ]
        
        aContent += h_list_to_s( header ) + '\n' # os.linesep

        # Print the new header 
        # print ( h_list_to_s( header ) )

        for row in csv_content:
            
            # Remove index from header
            del row[ index ]
            
            aContent += h_list_to_s( row ) + '\n' # os.linesep 

            # Print the new header 
            # print ( h_list_to_s( row ) )

        if aReturnContent:
            return aContent
        else:
            file_write( aPath, aContent )     
            return aContent

    except:
        return 

'''
Info: Update Column
Input:
  - aPath: file path
  - aColName: column to remove
  - aPattern:
    - random_str: a random string
    - random_int: [1 : 999] range
    - timestamp: current unix ts
Output:
  - New File contents (if found)
  - Error message 
'''
def csv_col_update( aPath, aColName, aPattern='random_str' ):

    try:

        aContent    = ''
        csv_content = csv_load( aPath )

        if not csv_content:

            print( ' > Error Reading CSV File [' + aPath + ']' )
            return

        header = next(csv_content)     # ignore header (1st line)

        if not aColName in header:
            s = h_list_to_s( header )
            print( ' > Error: [' + aColName + '] not found in header [' + s + ']' )
            return

        index = header.index( aColName )
        
        aContent += h_list_to_s( header ) + '\n' # os.linesep

        # Print the new header 
        print ( h_list_to_s( header ) )

        # Feed the random seed
        fake = Faker()
        
        for row in csv_content:
            
            # Remove index from header
            
            print(' > LINE   : ' + h_list_to_s( row ) )

            if aPattern == 'timestamp':
                row[ index ] = str( int( datetime.utcnow().timestamp() ) )
            elif aPattern == 'random_int':
                row[ index ] = str( int( randint(1, 499) ) )
            else:
                row[ index ] = fake.name()

            print(' > LINE_u : ' + h_list_to_s( row ) )

            aContent += h_list_to_s( row ) + '\n' # os.linesep 

            # Print the new header 
            # print ( h_list_to_s( row ) )

        file_write( aPath, aContent )     
        return aContent

    except:
        return 

'''
Info: Add Column
Input:
  - aPath: file path
  - aColName: column to remove
  - aPattern:
    - random_str: a random string
    - random_int: [1 : 999] range
    - timestamp: current unix ts
Output:
  - New File contents (if found)
  - Error message 
'''
def csv_col_add( aPath, aColName, aPattern='random_str' ):

    try:

        aContent    = ''
        csv_content = csv_load( aPath )

        if not csv_content:

            print( ' > Error Reading CSV File [' + aPath + ']' )
            return

        header = next(csv_content)     # ignore header (1st line)

        # For existing columns -> update
        if aColName in header:
            return csv_col_update( aPath, aColName, aPattern )

        header.append( aColName )
        
        aContent += h_list_to_s( header ) + '\n' # os.linesep

        # Print the new header 
        print ( h_list_to_s( header ) )

        # Feed the random seed
        fake = Faker()
        
        for row in csv_content:
            
            # Remove index from header
            
            print(' > LINE   : ' + h_list_to_s( row ) )

            val = None

            if aPattern == 'timestamp':
                val = str( int( datetime.utcnow().timestamp() ) )
            elif aPattern == 'random_int':
                val = str( int( randint(1, 499) ) )
            else:
                val = fake.name()

            row.append( val )

            print(' > LINE_u : ' + h_list_to_s( row ) )

            aContent += h_list_to_s( row ) + '\n' # os.linesep 

            # Print the new header 
            # print ( h_list_to_s( row ) )

        file_write( aPath, aContent )     
        return aContent

    except:
        return 

def csv_to_json( aPath ):

    csv_content = csv_load( aPath )
    data = []

    if not csv_content:

        print( ' > Error Reading CSV File [' + aPath + ']' )
        return data

    header = next(csv_content)

    for row in csv_content:

        index = 0
        field_dict = {}

        for field in row:

            if len( header ) != len( row ):
                print( ' > Error processing line [' + h_list_to_s( row ) + ']' )
                continue

            
            field_dict[ header[index] ] = row[ index ]

            index += 1

        # Check for empty(ness) 
        if field_dict:    

            data.append( field_dict )
    
    return data
       