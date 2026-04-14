import requests
import random
import time

BLYNK_TOKEN = "YOUR_BLYNK_AUTH_TOKEN"

energy = 0  # kWh

while True:
    # Simulated values
    voltage = round(random.uniform(210, 240), 2)
    current = round(random.uniform(0.5, 5.0), 2)
    
    power = round(voltage * current, 2)  # Watts
    energy += power / 3600000  # Convert W to kWh over time
    
    # Send to Blynk
    base_url = "https://blynk.cloud/external/api/update"
    
    requests.get(f"{base_url}?token={BLYNK_TOKEN}&V0={voltage}")
    requests.get(f"{base_url}?token={BLYNK_TOKEN}&V1={current}")
    requests.get(f"{base_url}?token={BLYNK_TOKEN}&V2={power}")
    requests.get(f"{base_url}?token={BLYNK_TOKEN}&V3={round(energy, 5)}")
    
    print(f"Voltage: {voltage}V | Current: {current}A | Power: {power}W | Energy: {energy:.5f} kWh")
    
    time.sleep(2)