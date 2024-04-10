# Apache-Ignite-Storage

Apache Ignite Storage is an efficient storage solution for High-Performance Computing (HPC) with a pipelined workflow.

## Overview

This project utilizes Apache Ignite for storing and processing large datasets efficiently. It includes several components such as data loading, preprocessing, integration, and storing in Apache Ignite.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/Apache-Ignite-Storage.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Apache-Ignite-Storage
    ```

3. Install the required dependencies using pip and the provided `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Data Loading**: Run the following command to load data into the system:

    ```bash
    python Pipeline/DataLoading.py
    ```

2. **Data Preprocessing**: If data preprocessing is required, execute the following command:

    ```bash
    python Pipeline/DataPreprocessing.py
    ```

3. **Data Integration**: To integrate multiple datasets, run:

    ```bash
    python Pipeline/DataIntegration.py
    ```

4. **Storing in Apache Ignite**: Store the integrated data in Apache Ignite using:

    ```bash
    python Pipeline/StoreData.py
    ```

5. **Starting the Ignite Cluster**: If you haven't already started the Ignite cluster, run:

    ```bash
    ./run.sh
    ```

6. **Exploring the Results**: Explore the results in the output files or in the Apache Ignite cache, depending on your project's requirements.
7. In this **main.py** file, the main() function orchestrates the entire workflow by calling the respective functions from the **DataLoading, DataPreprocessing, DataIntegration, and StoreData modules.** This way, users can simply run python main.py to execute the entire pipeline.



## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or create a pull request.

