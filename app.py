from flask import Flask, jsonify, request

from scheduling_sim import (
    FirstComeFirstServeScheduler,
    PriorityCooperativeScheduler,
    PriorityPreemptiveScheduler,
    Process,
    RoundRobinScheduler,
    SchedulingAlgorithm,
    ShortestJobFirstScheduler,
    ShortestRemainingTimeFirstScheduler,
)

app = Flask(__name__)


@app.route("/", methods=["POST"])
def execute_process_scheduling():
    try:
        data = request.json

        processes = []
        for i in range(data["n_of_processes"]):
            process = Process(
                name=data["name"][i],
                execution_time=data["execution_time"][i],
                priority_level=data["priority_level"][i],
                arrival_time=data["arrival_time"][i],
            )
            processes.append(process)

        match data["algorithm"]:
            case "FCFS":
                scheduler = FirstComeFirstServeScheduler(processes)
            case "SJF":
                scheduler = ShortestJobFirstScheduler(processes)
            case "RR":
                scheduler = RoundRobinScheduler(
                    processes, data.get("quantum_length", 2)
                )
            case "PRIOc":
                scheduler = PriorityCooperativeScheduler(
                    processes, data.get("reversed", True)
                )
            case "PRIOp":
                scheduler = PriorityPreemptiveScheduler(
                    processes, data.get("reversed", True)
                )
            case "SRTF":
                scheduler = ShortestRemainingTimeFirstScheduler(processes)
            case _:
                valid_algorithms = ["FCFS", "SJF", "PRIOc", "RR", "SRTF", "PRIOp"]
                return jsonify(
                    {
                        "message": f"Invalid algorithm '{data['algorithm']}'. Must be one of the following: {', '.join(valid_algorithms)}."
                    }
                )

        scheduler.run()

        response = {
            "n_of_processes": scheduler.number_of_processes,
            "average_wait_time": scheduler.average_wait_time,
            "average_turnaround_time": scheduler.average_turnaround_time,
            "total_execution_time": scheduler.total_execution_time,
        }

        return jsonify(response), 200

    except KeyError as e:
        return jsonify({"message": f"Missing field {e}."}), 422
    except IndexError:
        return jsonify({"message": "Incorrect number of processes."}), 422


if __name__ == "__main__":
    app.run()
