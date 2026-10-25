# Development Environment

## Hardware
- Computer: MacBook Pro
- Processor: Apple Silicon M3
- Architecture: arm64

## Software
- Operating system: macOS
- Python: 3.11.7
- Git: 2.39.3
- Editor: Visual Studio Code

## Python environment
The project uses a dedicated Python virtual environment (.venv).

Dependencies are recorded in requirements.txt.

To recreate the environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```