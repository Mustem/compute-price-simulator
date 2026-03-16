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
- supports CLI-based scenario input
- supports preset market scenarios
- includes mean-reversion inspired pricing logic

## Structure

- src/ -> Python source files
- docs/ -> usage notes
- examples/ -> sample output
- data/ -> optional future sample inputs

## Main Script

### simulator.py
Runs a simple compute market pricing simulation.

## Usage

Run with default values:
python3 src/simulator.py

Run with a preset:
python3 src/simulator.py tight
python3 src/simulator.py balanced
python3 src/simulator.py loose

Run with custom inputs:
python3 src/simulator.py 1000 1450 1.15 1.08

Input order:
- supply
- demand
- hardware shock factor
- energy cost factor

## Roadmap

- add CSV input support
- add simple futures-oriented scenarios
- add contract unit assumptions
- add oracle-inspired external input structure
