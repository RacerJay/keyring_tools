# Keyring Tools

![Version](https://img.shields.io/badge/version-v1.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Requirements

```[bash]
keyring>=23.9.3
```

```[bash]
> pip install -r requirements.txt
```

or

```[bash]
> pip install keyring
```

---

## Supported credential stores

- macOS Keychain
- Windows Credential Locker
- Freedesktop Secret Service supports many DE including GNOME (requires secretstorage)
- KDE4 & KDE5 KWallet (requires dbus)

## Reference

<https://pypi.org/project/keyring/>

---

## **set_cred.py**

### Description

- Create a password in the local credential store.

### Synopsis

```[bash]
> python set_cred.py -h
```

#### Usage

```[bash]
> set_cred.py [-h] [--version] CredentialStoreName Username Password
```

#### Positional Arguments

Argument | Description
---------|------------
CredentialStoreName | Credential "System" name
Username | User name in the credential store
Password | Password for the User name in the credential store

#### Options

Parameter | Description
----------|------------
-h, --help | show this help message and exit
--version | show program's version number and exit

---

## **get_cred.py**

### Description

- Retrieve a password from the local credential store.

### Synopsis

```[bash]
> python get_cred.py -h
```

#### Usage

```[bash]
> get_cred.py [-h] [--version] CredentialStoreName Username
```

#### Positional Arguments

Argument | Description
---------|------------
CredentialStoreName | Credential "System" name
Username | User name in the credential store

#### Options

Parameter | Description
----------|------------
-h, --help | show this help message and exit
--version | show program's version number and exit

---

## **del_cred.py**

### Description

- Delete a password from the local credential store.

### Synopsis

```[bash]
> python del_cred.py -h
```

#### Usage

```[bash]
> del_cred.py [-h] [--version] CredentialStoreName Username
```

#### Positional Arguments

Argument | Description
---------|------------
CredentialStoreName | Credential "System" name
Username | User name in the credential store

#### Options

Parameter  | Description
-----------|------------
-h, --help | show this help message and exit
--version | show program's version number and exit
