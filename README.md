# Renewable Energy Signal Indicator - README

This project uses a Raspberry Pi to indicate the share of renewable energy in the grid using three LEDs (Red, Yellow, Green). The program fetches real-time energy signals from an external API and lights up the appropriate LED to reflect the renewable energy status.

---

## 📝 **Project Overview**

This project is designed to help users visualize the current share of renewable energy in the grid using a simple traffic light-style LED indicator:

- **Red LED**: Low renewable energy share or grid congestion
- **Yellow LED**: Moderate renewable energy share
- **Green LED**: High renewable energy share

The project is useful for people who want to optimize their energy consumption based on the availability of renewable energy sources.

---

## 📦 **Project Structure**

```plaintext
project/
│
├── energy_signal.py       # Main script for the project
├── README.md              # Documentation file
└── requirements.txt       # Dependencies (optional)
```

---

## ⚙️ **Hardware Requirements**

- **Raspberry Pi (any model with GPIO pins)**
- **3 LEDs (Red, Yellow, Green)**
- **3 Resistors (220Ω)**
- **Breadboard and connecting wires**

### **GPIO Pin Configuration**

| LED Color   | GPIO Pin   |
|-------------|------------|
| Red         | 17         |
| Yellow      | 27         |
| Green       | 22         |

---

## 🧰 **Software Requirements**

- Python 3.x
- RPi.GPIO library (for Raspberry Pi GPIO control)
- `requests` library (for fetching data from the API)
- `unittest.mock` (for mocking GPIO when running on non-Raspberry Pi systems)

Install the necessary dependencies using:

```bash
pip install requests
```

---

## 🚦 **How It Works**

1. **Setup GPIO Pins**  
   The `setup()` function initializes the GPIO pins for output.

2. **Fetch Renewable Energy Data**  
   The `fetch_energy_json()` function retrieves real-time energy data from the API:
   - **URL**: `https://api.energy-charts.info/signal?country=de`

3. **Determine Energy Status**  
   The `determine_status_based_on_json(data)` function interprets the signal from the API to determine the energy status:
   - **-1 or 0** → Red (Low renewable energy or grid congestion)
   - **1** → Yellow (Moderate renewable energy)
   - **2** → Green (High renewable energy)

4. **Light Up LEDs**  
   Based on the determined status, the appropriate LED is turned on.

5. **Continuous Monitoring**  
   The `main()` function continuously fetches and processes the energy signal every second.

---

## 🚀 **How to Run the Project**

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/amiralimohaddes/renewable-energy-led-indicator.git
   cd renewable-energy-led-indicator
   ```

2. **Run the Script**  
   ```bash
   python3 energy_signal.py
   ```

3. **Stop the Script**  
   Use `Ctrl + C` to stop the program safely.

---

## 🔧 **Mock GPIO for Testing**

The project includes a mock implementation of the GPIO library for testing purposes on non-Raspberry Pi systems. When running on a non-Raspberry Pi machine, the GPIO operations will print mock messages to the console instead of interacting with physical pins.

Example Output on a non-Raspberry Pi system:
```plaintext
[MOCK GPIO] Pin 17: HIGH
[LED] Red ON: Low renewable energy
```

---

## 🌐 **External API Used**

The project uses the following API to fetch real-time renewable energy data:

- **API URL**: `https://api.energy-charts.info/signal?country=de`

This API returns a signal indicating the renewable energy status at the current time:
- **-1** → Grid congestion
- **0** → Low renewable energy
- **1** → Moderate renewable energy
- **2** → High renewable energy

---

## 🖥️ **Development and Testing**

For development and testing purposes on a non-Raspberry Pi system, you can run the script without physical hardware. The mock implementation will print messages to the console indicating which LEDs would have been activated.

---

## 🧹 **Cleanup**

To ensure the GPIO pins are properly cleaned up after the program ends, the `GPIO.cleanup()` function is called in the `finally` block of the `main()` function.

---

## 💡 **Project Ideas for Expansion**

- **Add a GUI** to display energy status on a screen connected to the Raspberry Pi.
- **Control home appliances** based on the renewable energy signal.
- **Send notifications** via email or SMS when the energy status changes.

---

## 📄 **License**

This project is licensed under the MIT License. You are free to use, modify, and distribute this project as per the terms of the license.

---

## 🧑‍💻 **Contributors**

- **Yasaman Khoroushi** -
  **Mojtaba Goudarzi** -
  **Seyed Amir Ali Mohaddes**

---

## 🛠️ **Troubleshooting**

- **Error: `RPi.GPIO` module not found**  
  Ensure you are running the script on a Raspberry Pi device or use the mock implementation for testing.

- **LEDs not lighting up**  
  - Double-check your wiring.
  - Ensure the correct GPIO pins are configured.

---

## 📞 **Contact**

For any questions or issues, please raise an issue on the project's GitHub repository.

---

## 🎉 **Thank You for Using This Project!** 🎉
