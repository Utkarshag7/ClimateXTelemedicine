import os

# === BASE PATHS ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# === DATA FOLDERS ===
DATA_DIR            = os.path.join(BASE_DIR, 'Data')
RAW_DIR             = os.path.join(DATA_DIR, 'Raw')
PROCESSED_DIR       = os.path.join(DATA_DIR, 'Processed')
OUTPUTS_DIR         = os.path.join(DATA_DIR, 'Outputs')

# === RAW DATA FILES ===
GADM_L3_DBF = os.path.join(RAW_DIR, 'GADM Data', 'gadm41_IND_3.dbf')
GADM_L2_DBF = os.path.join(RAW_DIR, 'GADM Data', 'gadm41_IND_2.dbf')
GADM_L1_DBF = os.path.join(RAW_DIR, 'GADM Data', 'gadm41_IND_1.dbf')
GEOCODE_HEALTH_CENTRE_CSV = os.path.join(RAW_DIR, 'geocode_health_centre.csv')
HMIS_FACILITY_MASTER_CSV  = os.path.join(RAW_DIR, 'HMIS_Facility_Detail_AUG24.xlsx - Facility Master Report  for All.csv')
ODISHA_OSRM_PBF = os.path.join(RAW_DIR, 'odisha.osm.pbf')

# === PROCESSED DATA FILES & FOLDERS ===
SNAPPED_FACILITIES_DIR = os.path.join(PROCESSED_DIR, 'snapped_facilities_by_district')
SNAPPED_VILLAGES_DIR   = os.path.join(PROCESSED_DIR, 'snapped_villages_by_district')
MASTER_FACILITY_CSV    = os.path.join(PROCESSED_DIR, 'master_dataset_final.csv')

def snapped_facility_file(district, facility_type):
    return os.path.join(SNAPPED_FACILITIES_DIR, f"{district}_{facility_type}_snapped.geojson")
def snapped_village_file(district):
    return os.path.join(SNAPPED_VILLAGES_DIR, f"{district}_villages_snapped.geojson")

# === OUTPUTS FOLDERS & FILES ===
FINAL_OUTPUTS_ALLPROFILES_DIR = os.path.join(OUTPUTS_DIR, 'Final_outputs_allprofiles')
CHC_OUTPUTS_DIR   = os.path.join(FINAL_OUTPUTS_ALLPROFILES_DIR, 'chc')
DH_OUTPUTS_DIR    = os.path.join(FINAL_OUTPUTS_ALLPROFILES_DIR, 'dh')
FOOT_OUTPUTS_DIR  = os.path.join(FINAL_OUTPUTS_ALLPROFILES_DIR, 'foot_profile')
HSC_OUTPUTS_DIR   = os.path.join(FINAL_OUTPUTS_ALLPROFILES_DIR, 'hsc')
PHC_OUTPUTS_DIR   = os.path.join(FINAL_OUTPUTS_ALLPROFILES_DIR, 'phc')
CAR_OUTPUTS_DIR   = os.path.join(OUTPUTS_DIR, 'Ouptuts_Car')
CAR_ROUTING_DH    = os.path.join(CAR_OUTPUTS_DIR, 'routing_dh')
CAR_ROUTING_PHC   = os.path.join(CAR_OUTPUTS_DIR, 'phc')
CAR_ROUTING_HSC   = os.path.join(CAR_OUTPUTS_DIR, 'hsc')
CAR_ROUTING_CHC   = os.path.join(CAR_OUTPUTS_DIR, 'chc')

def routing_output_file(profile, facility_type, district):
    dir_map = {
        'allprofiles': FINAL_OUTPUTS_ALLPROFILES_DIR,
        'car': CAR_OUTPUTS_DIR,
    }
    folder = dir_map.get(profile, FINAL_OUTPUTS_ALLPROFILES_DIR)
    return os.path.join(folder, facility_type, f"{district}_village_to_{facility_type}.csv")

# === MODEL CONSTANTS (India-specific, literature-backed) ===

# --- Emissions (kg CO₂/km) ---
CAR_EMISSION_PER_KM   = 0.22  # Sedan/Hatchback, petrol, latest India studies
BIKE_EMISSION_PER_KM  = 0.05  # Motorcycle (<150cc)
AUTO_EMISSION_PER_KM  = 0.07  # Rural auto-rickshaw
BUS_EMISSION_PER_KM   = 0.055 # For reference only (not primary mode)
BICYCLE_EMISSION_PER_KM = 0.0
FOOT_EMISSION_PER_KM  = 0.0

# --- Transport Costs (INR/km) ---
CAR_COST_PER_KM   = 12.0    # Rural taxi/ambulance
BIKE_COST_PER_KM  = 2.5     # Average, India
AUTO_COST_PER_KM  = 15.0    # Rural auto hire
BUS_COST_PER_KM   = 1.5     # For reference only

# --- Wait & Consult Durations (minutes) ---
CONSULT_DURATION_MIN            = 10    # Typical OPD/teleconsultation
IN_PERSON_WAIT_TIME_MIN         = 15    # In-person, rural OPD average
TELEMEDICINE_WAIT_TIME_MIN_MIN  = 0     # Min
TELEMEDICINE_WAIT_TIME_MIN_MAX  = 5     # Max

# --- Routing & Modeling ---
K_NEAREST                       = 3     # k-NN for PHC/CHC (India/your study)
HSC_COVERAGE_THRESHOLD_KM       = 3     # WHO/India
PHC_COVERAGE_THRESHOLD_KM       = 5
DEFAULT_SPEED_CAR_KMPH          = 35    # Average rural (India MoRTH studies)
DEFAULT_SPEED_BIKE_KMPH         = 35
DEFAULT_SPEED_AUTO_KMPH         = 25

# --- Unit Conversions ---
M_PER_KM = 1000

# --- Any others as needed ---

# === PRINT SUMMARY (Optional debug) ===
if __name__ == "__main__":
    print("BASE_DIR:", BASE_DIR)
    print("RAW_DIR:", RAW_DIR)
    print("PROCESSED_DIR:", PROCESSED_DIR)
    print("OUTPUTS_DIR:", OUTPUTS_DIR)
    print("CAR_EMISSION_PER_KM (kg):", CAR_EMISSION_PER_KM)
    print("BIKE_COST_PER_KM (INR):", BIKE_COST_PER_KM)
    print("Sample snapped facility file:", snapped_facility_file("anugul", "hsc"))
    print("Sample routing output file:", routing_output_file("allprofiles", "phc", "anugul"))