#!/usr/bin/env python3

def parse_log_file(file_location):
    """
    Parse a log file and return the world name and a list of completed trace logs
    :param file_location: The location of the log file to parse
    :return: The world name and a list of completed trace logs
    """
    print("Reading log file: " + file_location)

    world_name = ""
    line_count = 0
    current_episode = 0
    current_sim_trace_logs = []
    completed_sim_trace_logs_by_episode = {}

    try:
        with open(file_location, 'r') as file:
            for line in file:
                line_count += 1
                if line_count % 100 == 0:
                    print(f"Parsed {line_count} lines.")

                if 'World name passed in YAML:' in line:
                    world_name = line.split(': ')[1].strip()
                elif line.startswith('SIM_TRACE_LOG:'):
                    parsed_line = parse_line(line)

                    episode_number = parsed_line['episode']

                    if parsed_line['state'] == 'lap_complete':
                        completed_sim_trace_logs_by_episode[episode_number] = current_sim_trace_logs

                    # A new episode has started
                    if current_episode != episode_number:
                        current_sim_trace_logs = []
                        current_episode = episode_number

                    current_sim_trace_logs.append(parsed_line)
    except Exception as e:
        print(f"An error occurred while parsing the file: {e}")
        return None, None

    # Convert the dictionary to a list of arrays
    grouped_sim_trace_logs = [logs for episode, logs in sorted(completed_sim_trace_logs_by_episode.items())]

    return world_name, grouped_sim_trace_logs


def parse_line(line):
    line = line.strip()  # remove leading/trailing whitespace
    if line.startswith('SIM_TRACE_LOG:'):
        # split the line into pieces by comma, and discard the 'SIM_TRACE_LOG:' part
        parts = line[14:].split(',')

        # create a dictionary mapping column names to values
        result = {
            'episode': int(parts[0]),
            'step': int(parts[1]),
            'x': float(parts[2]),
            'y': float(parts[3]),
            'heading': float(parts[4]),
            'steering_angle': float(parts[5]),
            'speed': float(parts[6]),
            'decision': int(parts[7]),
            'reward': float(parts[8]),
            'is_reversed': parts[9],
            'all_wheels_on_track': parts[10],
            'progress': float(parts[11]),
            'closest_waypoint': int(parts[12]),
            'track_length': float(parts[13]),
            'timestamp': float(parts[14]),
            'state': parts[15],
        }
        return result
    else:
        return None  # or some other default
