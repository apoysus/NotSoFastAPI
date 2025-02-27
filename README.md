# notsofastapi

A lightweight rate-limiting library for FastAPI, no external dependencies like Redis required.

## Installation

```bash
pip install notsofastapi
```

## Usage

```python
from fastapi import FastAPI
from notsofastapi import ratelimit

app = FastAPI()

@app.get("/")
@ratelimit(limit=5, period=60)
async def root():
    return {"message": "Hello World"}
```

## Tests

```bash
pytest
```

## License

MIT License. See [LICENSE](LICENSE).

## Contributions

PRs are welcome!