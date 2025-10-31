# Highway Off-Ramp Simulation (Data-Driven, Kahathuduwa Exit, Seconds)
# Author: Vishadi Ranasinghe
# Description: Simulate vehicles leaving a highway off-ramp under different traffic scenarios in Sri Lanka

import simpy

# --------- Simulation functions ------------

def vehicle(env, name, ramp, wait_times, exit_times, exit_data, idx):
    """
    Simulate a vehicle arriving, waiting for ramp if needed, and exiting.
    """
    arrival_time = env.now
    with ramp.request() as request:  # try to use ramp
        yield request  # wait if ramp is busy
        wait_duration = env.now - arrival_time  # calculate waiting time
        wait_times.append(wait_duration)

        exit_duration = exit_data[idx % len(exit_data)]  # get exit duration from data
        yield env.timeout(exit_duration)  # simulate exiting
        exit_times.append(exit_duration)

def vehicle_generator(env, arrival_times, ramp, wait_times, exit_times, exit_data, sim_duration):
    """
    Generate vehicles continuously based on provided arrival times.
    """
    count = 0
    while env.now < sim_duration:  # run until simulation time is over
        inter_arrival = arrival_times[count % len(arrival_times)]
        yield env.timeout(inter_arrival)  # wait until next vehicle
        count += 1
        env.process(vehicle(env, f"Vehicle {count}", ramp, wait_times, exit_times, exit_data, count-1))

def run_simulation(arrival_times, exit_times_data, ramp_lanes, sim_duration):
    """
    Run one scenario of the simulation.
    """
    sim_env = simpy.Environment()
    ramp_resource = simpy.Resource(sim_env, capacity=ramp_lanes)
    wait_times_recorded = []
    exit_times_recorded = []

    sim_env.process(vehicle_generator(sim_env, arrival_times, ramp_resource, wait_times_recorded, exit_times_recorded, exit_times_data, sim_duration))
    sim_env.run()

    total_vehicles = len(wait_times_recorded)
    avg_wait = statistics.mean(wait_times_recorded) if wait_times_recorded else 0
    avg_exit = statistics.mean(exit_times_recorded) if exit_times_recorded else 0
    avg_total = avg_wait + avg_exit

    return total_vehicles, avg_wait, avg_exit, avg_total


# ------------------------- Main program -------------------------

def main():
    # Define traffic scenarios
    scenarios = [
        ("Morning Peak", [2, 3, 2.5, 3, 2.5], [3.5, 3.6, 3.5, 3.6, 3.5], 1),
        ("Evening Peak", [2.5, 3, 2.5, 3, 2.5], [3.5, 3.7, 3.6, 3.5, 3.7], 1),
        ("Weekend Traffic", [5, 6, 5.5, 6, 5.5], [3.5, 3.6, 3.5, 3.6, 3.5], 1),
        ("Accident Lane Blocked", [2, 3, 2.5, 3, 2.5], [3.5, 3.6, 3.5, 3.6, 3.5], 1),
        ("New Ramp Design", [2, 2.5, 2, 2.5, 2], [3.5, 3.5, 3.5, 3.5, 3.5], 2)
    ]

    # Simulation duration (30 minutes = 1800 seconds)
    sim_time = 1800

    print("Highway Off-Ramp Simulation (30 Minutes, Kahathuduwa Exit, Seconds)\n")

    # Print input data for clarity
    for name, arrivals, exits, lanes in scenarios:
        print(f"--- {name} ---")
        print("Arrival times (s):", arrivals)
        print("Exit times (s)   :", exits)
        print("Ramp lanes      :", lanes)
        print()

    # Header for results
    print(f"{'Scenario':30s} {'Vehicles':>10s} {'Avg Wait(s)':>12s} {'Avg Exit(s)':>12s} {'Total Avg(s)':>12s}")
    print("-"*80)

    # Run each scenario and display results
    for name, arrivals, exits, lanes in scenarios:
        total, avg_wait, avg_exit, avg_total = run_simulation(arrivals, exits, lanes, sim_time)
        print(f"{name:30s} {total:10d} {avg_wait:12.2f} {avg_exit:12.2f} {avg_total:12.2f}")

if _name_ == "_main_":
    main()