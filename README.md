# Kahathuduwa Highway Off-Ramp Simulation

**Author:** Vishadi Ranasinghe

---

## Overview

This project simulates vehicle traffic at the Kahathuduwa highway exit in Sri Lanka. The main goal is to analyze congestion, waiting times, and throughput during different traffic scenarios and identify ways to improve ramp efficiency and safety.

The simulation uses **Python** and the **SimPy** library to model vehicle arrivals, waiting, and departures based on actual traffic data collected on-site.



## Features

* Models **single-lane** and **dual-lane** off-ramp traffic
* Accounts for variable **vehicle arrival intervals** and **exit durations**
* Simulates different scenarios:

  * Morning peak
  * Evening peak
  * Weekend traffic
  * Lane blockage (accident)
  * New ramp design
* Identifies bottlenecks and calculates:

  * Waiting times
  * Throughput
  * Ramp efficiency



## Requirements

* Python 3.8+
* SimPy library
* Pandas library (for data handling)



## Installation

1. Clone the repository:

```bash
git clone <repository_url>
```

2. Install required libraries:

```bash
pip install simpy pandas
```




## Usage

1. Ensure that the data file (if any) is in the project directory.
2. Run the simulation script:

```bash
python off_ramp_simulation.py
```

3. The program outputs:

* Waiting times
* Throughput
* Congestion analysis for the selected scenario



## Scenarios Simulated

| Scenario                 | Description                            |
| ------------------------ | -------------------------------------- |
| Morning Peak             | Traffic during morning rush hour       |
| Evening Peak             | Traffic during evening rush hour       |
| Weekend Traffic          | Traffic during weekends                |
| Lane Blockage (Accident) | One lane blocked due to an accident    |
| New Ramp Layout          | Two-lane ramp design for improved flow |




## Performance Objectives

* Reduce vehicle waiting time
* Measure exit efficiency
* Maximize throughput
* Assess ramp capacity impact
* Identify congestion points
* Test scenario-based interventions (lane addition, ramp modifications)



## Expected Outcomes

* Peak traffic results in longer queues and slower throughput
* Adding lanes or optimizing ramp flow reduces delays
* Improved ramp design ensures smoother traffic movement during high-demand periods



## License

This project is licensed under the **MIT License**.
