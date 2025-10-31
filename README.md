# offramp_simulation
Simulation of a highway off-ramp system using SimPy under different traffic conditions.

Overview

This project simulates vehicle traffic at the Kahathuduwa highway exit in Sri Lanka. The goal is to analyze congestion, waiting times, and throughput during different traffic scenarios and identify possible improvements for ramp efficiency and safety.

The simulation uses Python and the SimPy library to model vehicle arrivals, waiting, and departures based on real-world traffic data collected on-site.

Features

Models single-lane and dual-lane off-ramp traffic.

Considers variable vehicle arrival intervals and exit durations.

Simulates different scenarios: morning peak, evening peak, weekend traffic, accidents, and new ramp design.

Identifies bottlenecks and calculates waiting times, throughput, and ramp efficiency.

Requirements

Python 3.8+

SimPy library

Pandas library (for data handling)

Installation

Clone the repository:

git clone <repository_url>

Install required libraries:

pip install simpy pandas
Usage

Ensure that the data file (if any) is in the project directory.

Run the simulation script:

python off_ramp_simulation.py

The program outputs waiting times, throughput, and congestion analysis for the selected scenario.

Scenarios Simulated
Scenario	Description
Morning Peak	Traffic during morning rush hour
Evening Peak	Traffic during evening rush hour
Weekend Traffic	Traffic during weekend
Lane Blockage (Accident)	One lane blocked due to accident
New Ramp Layout	Two-lane ramp design for improved flow
Performance Objectives

Reduce vehicle waiting time.

Measure exit efficiency.

Maximize throughput.

Assess ramp capacity impact.

Identify congestion points.

Expected Outcomes

High traffic leads to long queues and slower throughput.

Adding lanes or optimizing ramp flow reduces delays.

Improved ramp design ensures smoother traffic movement during peak hours.

Author

Vishadi Ranasinghe

License

This project is licensed under the MIT License.
