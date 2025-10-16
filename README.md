# pyenvsubst

Substitutes the values of environment variables. Python version.


## Features

- Fully compatible with envsubst
- Requires only Python itself and stdlib
- Supports POSIX syntax for default values
- Offers multiple quality-of-life features


## Installation

Install the latest stable version via pip:
```bash
  pip install pyenvsubst
```

Install the latest development version via pip:
```bash
  pip install pip install pyenvsubst@git+https://github.com/Coacher/pyenvsubst.git
```


## Usage

Substitute environment variables from STDIN, output to STDOUT:
```bash
  cat template.txt | pyenvsubst
```

Exclude specified environment variables from substitution, output to STDOUT:
```bash
  cat template.txt | pyenvsubst --exclude "$API_TOKEN"
```

Substitute environment variables from FOO.txt, output to BAR.txt:
```bash
  pyenvsubst --input=FOO.txt --output=BAR.txt
```
