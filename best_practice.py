#!/uusr/bin/env python3
"""A multi-line comment to describe the script,
   made with triple quotes."""

def main(): # All code should appear within a function.
    """All functions have multiline comments to describe them."""

    my_string = "Your code would go here."    # vars use _ and not camelCase.
    print(my_string)     # Print to standard output.

# Calling main() using this technique allows others to import your code.
if __name__ == "__main__":
    main()
