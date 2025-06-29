# Odisha Health Model: Time–Distance–Money & Climate Emissions Project

## Overview

This repository contains the full data science and spatial modeling workflow for analyzing healthcare access in Odisha, India, with a focus on **travel time, distance, economic cost, and climate emissions**.\
The project uses village and facility geospatial data, OSRM-based routing, and emissions/cost modeling to produce actionable insights for health system improvement.

---

## Project Highlights

- **Village- and facility-level access analysis** across all districts of Odisha
- **GIS data cleaning, snapping, and deduplication**
- **Multi-modal travel time/distance modeling** (car, motorcycle, auto, foot)
- **Comprehensive cost and climate emissions model** for each transport mode
- **Outputs include reproducible routing tables, coverage statistics, and emissions/cost estimates**
- **Jupyter notebook workflow**: each step modular and auditable

---

## Project Structure

```
notebooks/
  01_prepare_villages_v1.0.ipynb
  02_snap_facilities_v2.0.ipynb
  03_govdata_audit_v1.0.ipynb
  04_prepare_hmis_v1.0.ipynb
  05_routing_carprofile_v1.0.ipynb
  06_routing_footprofile_hsc_v1.0.ipynb
  07_routing_chc_to_dh_v1.0.ipynb
  08_cost_emissions_analysis_v1.0.ipynb
Data/
  Raw/
  Processed/
  Outputs/
config.py   # (optional, for future portability)
README.md   # (this file)
```

> **Note:**\
> All file/folder paths in the notebooks are currently hardcoded for a local Windows environment.\
> If running on a different system, you will need to update these paths accordingly.

---

## Data Sources

- **Village Boundaries:** ESRI/GADM/Census 2011/2024, Odisha administrative boundaries
- **Facility Master:** ESRI, HMIS (MoHFW), geocoded and manually cleaned
- **Road Network:** OSM (OpenStreetMap PBF/GeoJSON), subsetted for Odisha
- **Government Data:** PLFS, Census, health coverage and utilization datasets
- **Routing Engine:** OSRM (local Docker setup, multi-profile)

---

## Workflow & Methodology

### 1️⃣ **Prepare and Clean Villages**

**Notebook:** `01_prepare_villages_v1.0.ipynb`

- Load village boundaries and administrative districts
- Deduplicate, fix geometries, and assign standardized codes (LGD, etc.)
- Output: cleaned villages GeoJSON/CSV

---

### 2️⃣ **Snap and Clean Health Facilities**

**Notebook:** `02_snap_facilities_v2.0.ipynb`

- Load raw facility data (ESRI/HMIS/GoI)
- Snap facility points to nearest road/village using spatial joins and cKDTree
- Output: snapped facility GeoJSON for each district

---

### 3️⃣ **Audit and Match Government Data**

**Notebook:** `03_govdata_audit_v1.0.ipynb`

- Load processed government facility lists
- Audit for duplicates, missing locations, inconsistent NINs
- Output: cleaned government datasets, audit summary files

---

### 4️⃣ **Prepare and Clean HMIS Facility Data**

**Notebook:** `04_prepare_hmis_v1.0.ipynb`

- Load raw HMIS data (MoHFW, CSV/Excel)
- Clean and deduplicate, standardize key columns, join to snapped facilities
- Output: cleaned HMIS dataset, district summaries

---

### 5️⃣ **Routing: Car Profile (Village to Facility)**

**Notebook:** `05_routing_carprofile_v1.0.ipynb`

- For each district and facility type (HSC, PHC, CHC):
  - Load snapped villages and facilities
  - Run OSRM routing (car profile) to get travel time and distance from each village to the nearest facility (k-NN logic as required)
  - Output: routing result CSVs for all combinations

---

### 6️⃣ **Routing: Foot Profile (Village to HSC)**

**Notebook:** `06_routing_footprofile_hsc_v1.0.ipynb`

- For each district:
  - Load snapped villages and HSCs
  - Run OSRM routing (foot profile) to estimate walk-time access to HSCs
  - Output: routing CSVs per district

---

### 7️⃣ **Routing: CHC to DH (Referral Routing)**

**Notebook:** `07_routing_chc_to_dh_v1.0.ipynb`

- For each district:
  - Load snapped CHC and DH points
  - Run OSRM routing (car profile) to estimate referral time from each CHC to the nearest DH/SDH
  - Output: referral routing CSVs per district

---

### 8️⃣ **Cost & Emissions Modeling**

**Notebook:** `08_cost_emissions_analysis_v1.0.ipynb`

- Load all routing outputs (from car, foot, referral, etc.)
- Calculate travel cost (INR) and emissions (kg CO₂) for each trip
  - Uses India-specific emission factors:
    - Car: 0.22 kg/km
    - Motorcycle: 0.05 kg/km
    - Auto: 0.07 kg/km
    - Foot/Bicycle: 0
  - Cost per km (INR):
    - Car: ₹12
    - Motorcycle: ₹2.5
    - Auto: ₹15
- Outputs: summary tables for costs/emissions, district/facility breakdowns, and key stats for reporting

---

## Model Logic and Constants

- **Travel time & distance:** calculated for all routes using OSRM with real road network data.
- **Cost model:** multiplies route distance by official per-km costs for each vehicle type.
- **Emissions model:** multiplies route distance by literature-based kg CO₂ per km for each vehicle.
- **Waiting and consult durations:** from ABCE, IHME, BMC, NHA studies (India).
- **k-NN approach:** For PHC/CHC, up to 3 nearest facilities are checked; for HSC, 1-NN is used.

---

## Reproducibility Notes

- **Hardcoded file paths:** All data loading/saving uses full Windows paths.\
  If you wish to run the code elsewhere, update the paths in each notebook or create a `config.py` for future use.
- **OSRM routing:** Requires a local Docker-based OSRM instance with the Odisha PBF file and car/foot profiles.

---

## Outputs

- **Processed villages/facilities** (GeoJSON, CSV)
- **Routing result tables** (per district, facility type, and profile)
- **Cost/emissions summaries** (per route and aggregated)
- **Audit files** for quality checks

---

## Credits

- **Data sources:** ESRI, HMIS, GADM, OSM, GoI, PLFS, ABCE, NHA, BMC, IHME, CEEW, MoEFCC, etc.
- **Lead analyst:** Utkarsh Agarwal
- **Contact:** [utkarsh.agarwal@ifmr.ac.in](mailto\:utkarsh.agarwal@ifmr.ac.in)

---

## Acknowledgements
Methodology built on the latest global and India-specific best practices in health GIS, accessibility, and sustainability modeling.

---

## To Run This Project

1. **Install dependencies**:
   - geopandas, pandas, numpy, tqdm, requests, shapely, etc.
2. **Prepare your data folders** as in the structure above.
3. **Open each notebook in order** and update paths if necessary.
4. **Review outputs** in the Outputs folder.

---

> **Note:**\
For sharing, evaluation, and reproducibility, you can convert all file/folder references to variables using a config.py, or at least document path dependencies in each notebook.


