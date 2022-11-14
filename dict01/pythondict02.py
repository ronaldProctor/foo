#!/usr/bin/env python3
"""Understanding dictionaries
    {key: value, key:value, ...}
    using the dict.get() method"""

def main():
    """runtime function"""

    ## create a dictionary with 4 key:value parts
    switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

    ## display the entire dictionary
    print(switch)

    ## proove that switch is indeed a dictionary
    print(type(switch))

    ## display parts of the dictionary
    print( switch["hostname"] )    # displays "sw1"
    print( switch["ip"] )          # displays "10.0.1.1"

    ## request a 'fake' key
    # print( switch["lynx"] )   # Be sure to comment out this line,
                                # or your program will CONTINUE to fail!
                                # if a KEY is requested that does not exist,
                                # an ERROR will be thrown!

    ## request a 'fake' key with .get() method
    print( "First test - .get()" )
    print( switch.get("lynx"), "Key not found." ) # instead of asking for a wrong key directly
    #print(switch.get("lynx", None)) # this is what is happening, dict.get() returns "None" by default

    # to customize the output when key not found
    print( "Second test - .get()" )
    print( switch.get("version") )

# call our main function
if __name__ == "__main__":
    main()

