import time
import requests
import json
from datetime import datetime, timedelta
import sys

# Attempt to import RPi.GPIO, mock if unavailable 
try:
    import RPi.GPIO as GPIO
except ImportError:
    from unittest.mock import Mock
    GPIO = Mock()
    GPIO.BCM = 'BCM'
    GPIO.OUT = 'OUT'
    GPIO.LOW = 'LOW'
    GPIO.HIGH = 'HIGH'

    # Mock GPIO functions
    def mock_gpio_output(pin, state):
        print(f"[MOCK GPIO] Pin {pin}: {'HIGH' if state == GPIO.HIGH else 'LOW'}")

    GPIO.output = mock_gpio_output

# GPIO Pins for LEDs 
RED_LED = 17
YELLOW_LED = 27
GREEN_LED = 22


def setup():
    """Setup the GPIO pins."""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RED_LED, GPIO.OUT)
    GPIO.setup(YELLOW_LED, GPIO.OUT)
    GPIO.setup(GREEN_LED, GPIO.OUT)

def all_leds_off():
    """Turn off all LEDs."""
    GPIO.output(RED_LED, GPIO.LOW)
    GPIO.output(YELLOW_LED, GPIO.LOW)
    GPIO.output(GREEN_LED, GPIO.LOW)



def indicate_red():
    """Turn on the Red LED."""
    all_leds_off()
    GPIO.output(RED_LED, GPIO.HIGH)
    print("[LED] Red ON: Low renewable energy")

def indicate_yellow():
    """Turn on the Yellow LED."""
    all_leds_off()
    GPIO.output(YELLOW_LED, GPIO.HIGH)
    print("[LED] Yellow ON: Moderate renewable energy")

def indicate_green():
    """Turn on the Green LED."""
    all_leds_off()
    GPIO.output(GREEN_LED, GPIO.HIGH)
    print("[LED] Green ON: High renewable energy")

def fetch_energy_json():
    """Fetch the renewable energy signal for the current time."""
    url = f"https://api.energy-charts.info/signal?country=de"

    try:
        print(f"Fetching data from: {url}")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Print the fetched data for debugging purposes
        print("Fetched JSON Data:")
        print(json.dumps(data, indent=2))
        
        return data
    except Exception as e:
        print(f"Error fetching JSON data: {e}")
        return None


    
def determine_status_based_on_json(data):
    """Determine the renewable energy status based on the signal."""
    try:
        if "signal" in data and data["signal"]:
            signal = data["signal"][-1]  # Get the latest signal value
            if signal == -1:
                return "red"  # Grid congestion
            elif signal == 0:
                return "red"  # Low renewable share
            elif signal == 1:
                return "yellow"  # Average renewable share
            elif signal == 2:
                return "green"  # High renewable share
            else:
                print("Unknown signal value.")
                return "error"
        else:
            print("Signal data not found.")
            return "error"
    except Exception as e:
        print(f"Error parsing JSON data: {e}")
        return "error"



def main():
    setup()
    try:
        while True:
            data = fetch_energy_json()
            if data:
                status = determine_status_based_on_json(data)
                if status == "red":
                    indicate_red()
                elif status == "yellow":
                    indicate_yellow()
                elif status == "green":
                    indicate_green()
                else:
                    print("Unknown status. Turning off all LEDs.")
                    all_leds_off()
            else:
                print("Failed to fetch data. Turning off all LEDs.")
                all_leds_off()

            
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting program")
    finally:
        all_leds_off()
        GPIO.cleanup()

if __name__ == "__main__":
    main()
