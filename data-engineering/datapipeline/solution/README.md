# Formula 1 Data Pipeline

This project contains a Python-based data pipeline that transforms raw Formula 1 race data from CSV files into structured JSON files, one for each year of competition.

***

## Core Features

* **Automated Data Transformation:** Loads race and results data, merges them, and cleans the data to ensure consistency.
* **Structured JSON Output:** Produces clean, well-structured JSON files with key race statistics.
* **Dynamic File Generation:** Automatically generates one `stats_{year}.json` file for each year present in the source data.
* **Error Handling:** Includes checks for missing files and required columns to prevent unexpected crashes.

***

## How to Run the Pipeline

### **1. Prerequisites**

* Python 3.8+

### **2. Setup**

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/gherghinoiu/F1DataPipeline.git
    ```

2.  **Project Structure:**
    Ensure your project follows this structure. The `main.py` script is designed to find the data files from this specific layout.
    ```
    your-project/
    ├── source-data/
    │   ├── races.csv
    │   └── results.csv
    ├── solution/
    │   ├── main.py
    │   ├── data_loader.py
    │   └── data_transformer.py
    ├── results/
    │   └── (This folder will be created automatically if it doesn't exist)
    ├── tests/
    │   ├── test_data_loader.py
    │   ├── test_data_transformer.py
    └──
    ```

3.  **Install Dependencies:**
    Install the required pandas and pytest library using pip.
    ```bash
    pip install -r requirements.txt
    ```

### **3. Execute the Pipeline**

Run the main script from the project's root directory. The script will handle creating the `results` folder and processing all the data.
```bash
python solution/main.py
```
Upon successful execution, you will see confirmation messages in your terminal, and the `results/` folder will be populated with the `stats_{year}.json` files.

## Stretch Requirements Undertaken
This solution successfully implements the stretch goals outlined in the assignment.

### **1. Unit Testing**
Unit tests have been created for the core data loading and transformation logic to ensure reliability and correctness.

* **Framework:** `pytest`
* **Location:** The `tests/` directory.

**How to Run Tests:**

1.  Navigate to the project's root directory in your terminal and run the following command:
    ```bash
    python -m pytest
    ```
    Pytest will automatically discover and run all the tests, giving you a report on their success.


### **4. Assumtions**
Data is valid if the fastestLapTime has NaN value in it and will just return 'No time available'





