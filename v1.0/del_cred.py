#!/usr/bin/env python3

import sys
import argparse
import keyring

# The main function.
def main(argv):
    # Create parser.
    parser = argparse.ArgumentParser(description='Delete a password from the local credential store.')

    # Add arguments to the parser.
    parser.add_argument('CredentialStoreName', type=str, help='Credential "System" name')
    parser.add_argument('Username', type=str, help='User name in the credential store')
    parser.add_argument('--version', action='version', version='%(prog)s v1.0')

    # Parse the arguments.
    args = parser.parse_args()

    # Get the arguments values.
    system = args.CredentialStoreName
    username = args.Username

    # Delete the password from the credential store, or process the error.
    try:
        # keyring.get_keyring()
        keyring.delete_password(system, username)
        print(f'Credential store "{system}" has been deleted.')
    except keyring.errors.PasswordDeleteError:
        print(f'Failed to delete credential store.')
        print(f'Credential store "{system}" may not exist, or username "{username}" may be incorrect.')
    except keyring.errors.KeyringError:
        print(f'Error: Base Error class for all exceptions in keyring lib')
    except:
        print(f'Ugh, something bad happened')
    return None

# Call the main function to begin the script.
if __name__ == '__main__':
    main(sys.argv)
