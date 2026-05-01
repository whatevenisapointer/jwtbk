# JWT Secret Brute Forcer

A simple Python tool to brute-force HS256 JWT secrets using a wordlist.


## Installation

```bash
git clone https://github.com/whatevenisapointer/jwt-cracker
cd jwt-cracker

pip install -r requirements.txt
```
## Usage

```bash
python3 exploit.py -t <token> -w <wordlist>
```
## Example
```bash
python3 exploit.py -t eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoidGVzdCJ9.4Dr0n9n3L9A22I3SmrnVXlrh-ahEmIBr4qFoiVOfq40 -w jwt.secrets.list
```
## Options

-t, --token      JWT token  
-w, --wordlist   Path to wordlist file  
-v,              Version number

## Example Output

```bash
=== RESULT ===
[+] Valid key found: secret1
[+] Time elapsed: 0.0109s
```bash
## Requirements

- Python 3.x
- PyJWT
- colorama

## Disclaimer

This tool is intended for educational purposes and authorized security testing only.