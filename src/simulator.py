base_price = 1.00
supply = 1000
demand = 1450
hardware_shock_factor = 1.15
energy_cost_factor = 1.08

utilization = demand / supply

price_multiplier = utilization * hardware_shock_factor * energy_cost_factor
estimated_price = round(base_price * price_multiplier, 2)

if utilization < 0.70:
    scarcity = "Low"
    market_state = "Loose Market"
elif utilization < 0.90:
    scarcity = "Medium"
    market_state = "Balanced Market"
else:
    scarcity = "High"
    market_state = "Tight Market"

print("=== Compute Price Simulator ===")
print()
print(f"Base Price: {base_price:.2f}")
print(f"Supply: {supply}")
print(f"Demand: {demand}")
print(f"Utilization: {utilization * 100:.1f}%")
print(f"Hardware Shock Factor: {hardware_shock_factor:.2f}")
print(f"Energy Cost Factor: {energy_cost_factor:.2f}")
print()
print(f"Estimated Compute Price: {estimated_price:.2f}")
print(f"Scarcity Level: {scarcity}")
print(f"Market State: {market_state}")
