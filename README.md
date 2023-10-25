# Process Scheduling API

This Flask web application provides an API for executing various process scheduling algorithms. You can use this API to simulate different scheduling strategies for a set of processes and analyze their performance. It was made using the [source code of another project of mine](https://github.com/c-sant/scheduling-sim).

## Implemented Algorithms

The simulator supports the following algorithms:

- [X] **FCFS**: First Come First Serve
- [X] **SJF**: Shortest Job First
- [X] **SRTF**: Shortest Remaining Time First
- [X] **RR**: Round Robin
- [X] **PRIOc**: Priority (Cooperative)
- [X] **PRIOp**: Priority (Preemptive)

## Instalation

1. Clone the repository to your local machine.

```shell
git clone https://github.com/c-sant/process-scheduler-api.git
```

2. Access the project directory.

```shell
cd process-scheduler-api
```

3. Create a virtual environment (optional, but recommended):

```shell
python -m venv venv
```

4. Activate your virtual environment:

* For Windows:

```shell
venv\Scripts\activate
```

* For macOS and Linux:

```shell
source venv/bin/activate
```

5. Install project dependencies:

```shell
pip install -r requirements.txt
```

## Usage

1. Start the application using Flask:

```shell
flask run
```

You can also start by using Python to read the main script file:

```shell
python app.py
```

2. Make a POST request to the root endpoint (`/`) with a JSON payload that specifies the scheduling algorithm and the details of the processes to be scheduled. Here's an example of a valid request:

```json
{
    "algorithm": "FCFS",
    "n_of_processes": 2,
    "name": ["p1", "p2"],
    "arrival_time": [0, 1],
    "execution_time": [5, 2],
    "priority_level": [2, 1],
    "quantum_length": 2,
    "reversed": true
}
```

- `algorithm`: the acronym of the algorithm you intend to use. Refer to [Implemented Algorithms](#implemented-algorithms).
- `n_of_processes`: any positive integer.
- `name`: name of each process. Should be a list with as many items as specified by `n_of_processes`.
- `arrival_time`: arrival time of each process. Should be a list with as many items as specified by `n_of_processes`.
- `execution_time`: execution/burst time of each process. Should be a list with as many items as specified by `n_of_processes`.
- `priority_level`: level of priority of each process. Should be a list with as many items as specified by `n_of_processes`.
- `quantum_length`: the quantum length used by the Round Robin algorithm.
- `reversed`: if true, priority levels will follow a descending order.

3. The response should have the following structure:

```json
{
    "average_turnaround_time": 5.5,
    "average_wait_time": 2.0,
    "n_of_processes": 2,
    "total_execution_time": 7
}
```
## Example

Here's an example of how to use the API with Python and the `requests` library:

```python
import requests

url = "http://localhost:5000"
data = {
    "algorithm": "FCFS",
    "n_of_processes": 3,
    "name": ["P1", "P2", "P3"],
    "execution_time": [8, 4, 6],
    "priority_level": [2, 1, 3],
    "arrival_time": [0, 0, 0],
}

response = requests.post(url, json=data)

if response.status_code == 200:
    results = response.json()
    # Process the scheduling results here
else:
    print(f"Error: {response.json()['message']}")
```

## Contributing

This is a college assignment, but if you would like to contribute and turn this into a real project, please open an issue or submit a pull request.
