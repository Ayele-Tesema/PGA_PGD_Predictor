# Optimized Machine Learning Tool for Efficient PGA and PGD Predictions

Welcome to the Optimized Machine Learning Tool for Efficient PGA and PGD Predictions repository! This tool is designed to provide a rapid prediction of peak ground acceleration and displacement (PGA & PGD).The ML models in this repository were trained on *simulated* ground-motion datasets using **STRATA** (1-D equivalent-linear site-response program). 

**Core boundary / geometric assumptions used in the simulations.**  

The STRATA simulations assume:
- A **laterally-infinite (horizontally layered)** soil column — i.e., no 2-D/3-D lateral heterogeneity is modeled.  
- An **elastic half-space** (bedrock) underlying the soil column, consistent with STRATA’s 1-D formulation. 
- Input motions specified at the rock interface using STRATA’s **Outcrop** motion option (outcropping rock input).
  
 **Valid input ranges (model domain)**
  
The models are trained and valid within the parameter ranges sampled in our STRATA simulations. Use outside these ranges may be unreliable (results in error notifications):
-	Plasticity Index-PI (%): 0–60
- soil thickness-H (m): 10–100
-	unit weight of soil-γ (kN/m³): 12–24
-	Shear wave velocity-Vs (m/s): 100–650
- Reference peak ground acceleration-αgR (g): 0.05–1


## Getting Started!

### Installation

To get started with prediction tool, you need to have Python and required libraries installed on your system.


### Running the Application!

To successfully run the tool, please follow these steps:

1. **Install Python**
   - Ensure Python is installed on your system. You can download and install it from the [official Python website](https://www.python.org/).

2. **Install Required Libraries**
   - Install the necessary Python libraries by opening your terminal or command prompt and running the following command:
     ```bash
     pip install pandas numpy matplotlib scikit-learn PySimpleGUI 
     ```

3. **Download the Application Script**
   - Download the `PGA_PGD_OptML.py` script to your local machine.

4. **Open Your Python Environment**
   - Launch your preferred Python environment (for instance, Integrated Development Environment (IDE) like PyCharm or Visual Studio Code).

5. **Load the Script**
   - In your Python environment, open the `PGA_PGD_OptML.py`  script.

6. **Run the Application**
   - Execute the script to start the application. This is typically done by pressing a 'Run' button in IDEs or using a run command in the console.

Following these instructions will enable you to run the PGA_PGD_OptML.py application in any compatible Python environment.

## Contact

For inquiries or assistance, feel free to reach out through my email: chala.ayele.tesema@hallgato.sze.hu/sonoft@gmail.com

