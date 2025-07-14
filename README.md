# Network Slice Traffic Demand Prediction for Slice Mobility Management

This repository contains the codebase and resources for the paper:

**Title:** *Network Slice Traffic Demand Prediction for Slice Mobility Management*  
**Authors:** Muhammad Ashar Tariq, Malik Muhammad Saad, Mahnoor Ajmal, Ayesha Siddiqa, Dongkyun Kim  
**Affiliation:** School of Computer Science and Engineering, Kyungpook National University, South Korea  
**Published at:** ICAIIC 2024 (International Conference on Artificial Intelligence in Information and Communication)

📄 If you use this code or dataset, please cite our paper (see citation section below).

---

## 📌 Overview

5G introduces Network Slicing to support diverse services with tailored performance requirements on a shared physical infrastructure. However, the **non-uniform deployment of network slices across Tracking Areas (TAs)** within a Registration Area (RA) leads to service unavailability and mobility management challenges.

This project proposes a **Long Short-Term Memory (LSTM)-based traffic demand prediction model** to address these issues. The model forecasts the number of service requests each network slice is expected to receive in a TA, enabling **proactive resource configuration and seamless service continuity** for mobile users, even in areas where specific slices are not pre-deployed.

---

## 🎯 Key Contributions

- ⚙️ Predicts slice-wise hourly traffic demand using LSTM networks.
- 📡 Enables proactive slice handover and resource reallocation.
- 🚗 Supports seamless service delivery across non-uniform slice deployments in 5G RAs.
- 🧠 Injects intelligence into network operations using deep learning for predictive traffic management.

---

## 📁 Project Structure

```bash
.
├── data/           # Input dataset files (e.g., raw traffic logs, time series data)
├── model/          # Saved model checkpoints and parameters
├── results/        # Output predictions and logs
├── func/           # Helper modules and custom utility functions
├── main            # Main script to train or run the model
├── train           # May include training-related utilities or entry script
├── traffic.xlsx    # Dataset file: Contains slice-specific traffic request counts
├── time.xlsx       # Timestamps or time-aligned data for traffic.xlsx
├── README.md       # You're here! Project documentation

```

---

### ⚙️ Setup & Execution

1. **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/network-slice-demand-prediction.git
    cd network-slice-demand-prediction
    ```

2. **Install required packages**  
   Make sure you have Python 3.7 or higher installed. Then run:

    ```bash
    pip install -r requirements.txt
    ```

3. **Prepare the dataset**  
   Ensure the following files are placed in the root directory:
   - `traffic.xlsx`: Contains time-series request counts for each network slice.
   - `time.xlsx`: Contains corresponding timestamps.

4. **Run the model**

    ```bash
    python main
    ```

> 🧠 Depending on your setup, the model can be operated in two modes:
>
> - **Multivariate Mode**: All slices' traffic are treated as input features of a single model to learn inter-slice temporal relationships.
> - **Univariate Mode**: Each slice is predicted independently using a separate model.
>
> You can configure these modes and other hyperparameters directly in the `main` script or inside related files.

---

## 📊 Results & Evaluation

The detailed evaluation setup, prediction results, and performance analysis can be found in the published manuscript:

> **[Network Slice Traffic Demand Prediction for Slice Mobility Management — ICAIIC 2024](#)**  
> *https://ieeexplore.ieee.org/abstract/document/10463320 (DOI: 10.1109/ICAIIC60209.2024.10463320)*

The paper includes:
- Quantitative and visual comparison of true vs. predicted traffic demand for each network slice  
- Hourly average demand analysis across slices  
- LSTM model performance and training loss curve  
- Discussion on implications for proactive slice reconfiguration and mobility management

---

## 📚 Citation

If you use this code, dataset, or any part of this work in your research or publications, please cite the following paper:

```bibtex
@inproceedings{tariq2024network,
  title={Network slice traffic demand prediction for slice mobility management},
  author={Tariq, Muhammad Ashar and Saad, Malik Muhammad and Ajmal, Mahnoor and Siddiqa, Ayesha and Seo, Junho and Haishan, Yang and Kim, Dongkyun},
  booktitle={2024 International Conference on Artificial Intelligence in Information and Communication (ICAIIC)},
  pages={281--285},
  year={2024},
  organization={IEEE}
}
```
