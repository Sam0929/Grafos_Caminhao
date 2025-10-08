# Random Graph Analysis G(n,p)

![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

This project models a logistics problem using **graph theory** to determine the **maximum load capacity** that a truck can transport between two islands connected by bridges, each with specific weight restrictions.

---

## 📖 About the Project

This project uses `networkx` and `matplotlib` to explore the properties of random graphs.  
It is divided into two main functionalities:

1. **Path Capacity Analysis:**  
   For a given graph (either fixed or randomly generated), the algorithm constructs the **Maximum Spanning Tree (MST)** and, for a set of node pairs (source and target), determines the maximum flow capacity between them.  
   This capacity is defined by the “bottleneck” — the **edge with the smallest weight** along the unique path between the two nodes in the tree.

2. **Theoretical Analysis of the G(n,p) Model:**  
   Computes and plots the evolution of fundamental metrics as the number of vertices (N) increases, such as the **fraction of the giant component**, **average degree**, and the **expected number of edges**.  
   This is achieved using the theoretical formulas of the model, avoiding costly simulations.

---

## ✨ Features

* Path capacity analysis based on the Maximum Spanning Tree.  
* Modular and organized project structure separating configuration, logic, and visualization.  
* Generation of random graphs with weighted edges.  
* Calculation and plotting of the **Giant Component Fraction (S)** as a function of N.  
* Calculation and plotting of the **Expected Average Degree** as a function of N.  
* Calculation and plotting of the **Expected Number of Edges** (quadratic growth).

---

## 🚀 Getting Started

Follow the steps below to set up the development environment locally.

### Pre-requisites

* Python 3.13 or higher  
* Git

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Sam0929/Grafos_Caminhao.git
    cd Projeto_Caminhao
    ```

2. **Create and activate a virtual environment:**  
   It is strongly recommended to use a virtual environment to isolate project dependencies.

    * On macOS/Linux:
        ```bash
        python3 -m venv .venv
        source .\venv/bin/activate
        ```
    * On Windows:
        ```bash
        python -m venv .venv
        .\venv\Scripts\activate
        ```

3. **Install the dependencies:**  
   The `requirements.txt` file contains all necessary Python libraries.
    ```bash
    pip install -r requirements.txt
    ```
    Main dependencies:
    * `networkx`
    * `matplotlib`
    * `numpy`

---

## 💻 Usage

The main script can be configured to run in two modes:  
`fixed` (using a small predefined graph) or `random` (generating a large random graph).

1. **Set the execution mode:**  
   Open the file `Projeto_Caminhao/main.py` and modify the `mode` variable at the beginning of the `main()` function:
    ```python
    def main():
        """Main function responsible for running analysis and visualization."""
        mode = 'random'  # Change to 'fixed' to use the test graph
        # ...
    ```

2. **Run the project:**  
   From the **root folder** of the project (`Projeto_Caminhao/`), execute the following command:
    ```bash
    python main.py
    ```

The script will print the path analysis results to the console and then display the theoretical analysis plots.

---

## 📂 Project Structure

The project follows a standard Python package structure to ensure organization and scalability.

