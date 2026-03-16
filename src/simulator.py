import sys

base_price = 1.00
mean_reversion_strength = 0.30

provider_prices = {
    "AWS": 1.32,
    "RunPod": 1.08,
    "Vast.ai": 0.94,
    "Akash": 0.89,
    "Republic": 1.02,
}

preset = sys.argv[1].lower() if len(sys.argv) >= 2 else None

if preset == "tight":
    supply = 1000
    demand = 1600
    hardware_shock_factor = 1.20
    energy_cost_factor = 1.10
elif preset == "balanced":
    supply = 1400
    demand = 1200
    hardware_shock_factor = 1.00
    energy_cost_factor = 1.00
elif preset == "loose":
    supply = 2000
    demand = 1000
    hardware_shock_factor = 0.95
    energy_cost_factor = 0.98
elif len(sys.argv) == 5:
    supply = float(sys.argv[1])
    demand = float(sys.argv[2])
    hardware_shock_factor = float(sys.argv[3])
    energy_cost_factor = float(sys.argv[4])
else:
    supply = 1000
    demand = 1450
    hardware_shock_factor = 1.15
    energy_cost_factor = 1.08

utilization = demand / supply
raw_price_multiplier = utilization * hardware_shock_factor * energy_cost_factor
raw_estimated_price = base_price * raw_price_multiplier

mean_reverted_price = raw_estimated_price - (
    (raw_estimated_price - base_price) * mean_reversion_strength
)

estimated_price = round(mean_reverted_price, 2)

provider_values = list(provider_prices.values())
reference_market_price = round(sum(provider_values) / len(provider_values), 2)
provider_price_spread = round(max(provider_values) - min(provider_values), 2)

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

if preset in ["tight", "balanced", "loose"]:
    print(f"Preset Scenario: {preset}")

print(f"Base Price: {base_price:.2f}")
print(f"Supply: {supply}")
print(f"Demand: {demand}")
print(f"Utilization: {utilization * 100:.1f}%")
print(f"Hardware Shock Factor: {hardware_shock_factor:.2f}")
print(f"Energy Cost Factor: {energy_cost_factor:.2f}")
print(f"Mean Reversion Strength: {mean_reversion_strength:.2f}")
print()

print("Provider Inputs:")
for provider, price in provider_prices.items():
    print(f"- {provider}: {price:.2f}")

print()
print(f"Reference Market Price: {reference_market_price:.2f}")
print(f"Provider Price Spread: {provider_price_spread:.2f}")
print()

print(f"Raw Estimated Price: {raw_estimated_price:.2f}")
print(f"Mean-Reverted Price: {estimated_price:.2f}")
print(f"Scarcity Level: {scarcity}")
print(f"Market State: {market_state}")
