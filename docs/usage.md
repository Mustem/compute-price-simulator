# Usage

Run the simulator with default built-in values:

python3 src/simulator.py

Run the simulator with a preset scenario:

python3 src/simulator.py tight
python3 src/simulator.py balanced
python3 src/simulator.py loose

Run the simulator with custom values:

python3 src/simulator.py <supply> <demand> <hardware_shock_factor> <energy_cost_factor>

Example:

python3 src/simulator.py 1000 1450 1.15 1.08
