import os, sys

def calculate_volume( length, width, height ):
    'A function to calculate the volume of a rectangular prism.'
    
    
    product = length * width * height
    
    
    
    
    return product

def get_status ( is_running , error_count ) :
    if is_running == True and error_count < 100 :
        # This line is intentionally long to exceed Black's default 88 char limit
        status_message = 'System is operating nominally and the error count remains well below the maximum allowed threshold, which is great!'
    else:
        status_message = "System is halted or has too many errors."
    return status_message

if __name__ == '__main__':
    # Calling the functions with bad spacing
    v = calculate_volume(10,5,2)
    s = get_status(True, 1)

    print ( "Volume calculated:", v )
    print ( "System status:", s )