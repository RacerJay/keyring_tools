#!/usr/bin/env python3

import sys
import argparse
import keyring

# The main function.
def main(argv):
    # Create parser.
    parser = argparse.ArgumentParser(description='Create a password in the local credential store.')

    # Add arguments to the parser.
    parser.add_argument('CredentialStoreName', type=str, help='Credential "System" name')
    parser.add_argument('Username', type=str, help='User name in the credential store')
    parser.add_argument('Password', type=str, help='Password for the User name in the credential store')
    parser.add_argument('--version', action='version', version='%(prog)s v1.0')

    # Parse the arguments.
    args = parser.parse_args()

    # Get the arguments values.
    system = args.CredentialStoreName
    username = args.Username
    password = args.Password

    # Set a username and password in the credential store.
    keyring.get_keyring()
    try:
        keyring.set_password(system, username, password)
        print(f'Credential store "{system}" with username "{username}" and password "{password}" successfully created.')
    except:
        print(f'Ugh, something bad happened')
    return None

# Call the main function to begin the script.
if __name__ == '__main__':
    main(sys.argv)
