# methodical
A simple tool that scans markdown pages for headlines and assembles them in a table of contents

## How to install locally

```bash
python -m pip install build
python -m build
pip install -e .
```

## Run

```bash
methodical PATH/TO/FILE
```


## Contributing

### Development setup
Install pre-commit hooks:

```bash
pip install pre-commit
pre-commit install
pre-commit install --hook-type pre-push
