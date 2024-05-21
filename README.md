
# FastAPI Service
## Installation

### Prerequisites

- Python 3.6+
- pip (Python package installer)

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/fastapi_project.git
    cd fastapi_project
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    uvicorn app.main:app --reload
    ```

The API will be available at `http://127.0.0.1:8000`.

## Usage

### Endpoint

- **POST** `/addition`

#### Request Format

```json
{
    "batchid": "id0101",
    "payload": [[1, 2], [3, 4]]
}
