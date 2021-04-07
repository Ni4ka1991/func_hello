#!/usr/bin/env Python3

from os import system

def hi( lang, name ):
    
    if( lang == "ru" ):
        print( f"Привет, {name}" )
    elif( lang == "en"):
        print( f"Hello, {name}" )
    elif( lang == "ro"):
        print( f"Salut, {name}" )
    else:
        print( f"ERROR {lang} not exist in list" )

# #####################

system( "clear" )

hi( "ru", "Андрей" )
hi( "ro", "Stefan")
hi( "en", "Piter")





