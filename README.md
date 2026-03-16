# compute-price-simulator

A simple Python prototype for modeling compute price pressure using supply, demand, utilization, hardware shocks, and energy cost factors.

## Why this exists

If compute is becoming a core commodity of the AI economy, it needs better price discovery tools.

This project is a small starting point: a CLI-based simulator for thinking about how compute prices may respond to changing market conditions.

## Features

- models compute supply and demand
- estimates utilization
- applies hardware shock pressure
- applies energy cost pressure
- outputs an estimated compute price
- labels market scarcity

## Structure

- src/ -> Python source files
- docs/ -> usage notes
- examples/ -> sample output
- data/ -> optional future sample inputs

## Main Script

### simulator.py
Runs a simple compute market pricing simulation.

## Usage

Run:
python3 src/simulator.py

## Roadmap

- add CLI arguments
- add scenario presets
- add CSV input support
- add simple futures-oriented scenarios
