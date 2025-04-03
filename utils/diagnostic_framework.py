# utils/diagnostic_framework.py

def asmethod_flow(age, appearance, self_or_other, medication, extra_med, time_persisting, history, other_symptoms, danger_symptoms):
    # Process inputs using the ASMETHOD framework.
    # Customize decision logic as needed.
    results = {
        "Age/Appearance": age,
        "Self/Other": self_or_other,
        "Medication": medication,
        "Extra Medicines": extra_med,
        "Time Persisting": time_persisting,
        "History": history,
        "Other Symptoms": other_symptoms,
        "Danger Symptoms": danger_symptoms
    }
    # Example decision: if danger symptoms present, flag as critical
    if danger_symptoms:
        results["action"] = "Refer immediately"
    else:
        results["action"] = "Proceed with further questions"
    return results

def encore_flow(explore, no_med, care, observe, refer, explain):
    # Process inputs using the ENCORE framework.
    results = {
        "Explore": explore,
        "No Medication": no_med,
        "Care": care,
        "Observe": observe,
        "Refer": refer,
        "Explain": explain
    }
    # Simple logic to decide if referral is needed
    if refer:
        results["action"] = "Referral to doctor recommended"
    else:
        results["action"] = "Self-care guidance"
    return results

def sit_down_sir_flow(site, intensity, type_nature, duration, onset, with_other, annoyed_by, spread, frequency, relieved_by):
    # Process inputs using the SIT DOWN SIR framework.
    results = {
        "Site": site,
        "Intensity": intensity,
        "Type": type_nature,
        "Duration": duration,
        "Onset": onset,
        "With Other": with_other,
        "Annoyed By": annoyed_by,
        "Spread": spread,
        "Frequency": frequency,
        "Relieved By": relieved_by
    }
    # Decision logic example: high intensity and short onset may indicate emergency
    if intensity > 7 and onset < 2:
        results["action"] = "Emergency treatment required"
    else:
        results["action"] = "Schedule further evaluation"
    return results

# Additional helper functions can be added as needed.
