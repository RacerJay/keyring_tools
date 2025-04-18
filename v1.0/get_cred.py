#!/usr/bin/env python3

import sys
import argparse
import keyring

# The main function.
def main(argv):
    # Create parser.
    parser = argparse.ArgumentParser(description='Retrieve a password from the local credential store.')

    # Add arguments to the parser.
    parser.add_argument('CredentialStoreName', type=str, help='Credential "System" name')
    parser.add_argument('Username', type=str, help='User name in the credential store')
    parser.add_argument('--version', action='version', version='%(prog)s v1.0.1')

    # Parse the arguments.
    args = parser.parse_args()

    # Get the arguments values.
    system = args.CredentialStoreName
    username = args.Username

    # Retrieve the password from the credential store.
    # keyring.get_keyring()
    result = keyring.get_password(system, username)

    # Process the result.
    if result == None:
        print(f'No credential store or password found: {system} / {username}')
    else:
        print(result)
    return result

# Call the main function to begin the script.
if __name__ == '__main__':
    main(sys.argv)
