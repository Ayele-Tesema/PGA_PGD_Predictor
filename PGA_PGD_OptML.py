import PySimpleGUI as sg
import numpy as np
import pickle
with open("PGA_model.pkl", "rb") as pga_file:
    pga_data = pickle.load(pga_file)
    pga_model = pga_data['model']
    pga_scaler_X = pga_data['scaler_X']
    pga_scaler_y = pga_data['scaler_y']

with open("PGD_model.pkl", "rb") as pgd_file:
    pgd_data = pickle.load(pgd_file)
    pgd_model = pgd_data['model']
    pgd_scaler_X = pgd_data['scaler_X']
    pgd_scaler_y = pgd_data['scaler_y']

# Define ranges for features
feature_ranges = {
    "PI (%)": [0, 60],
    "H (m)": [10, 100],
    "γ (kN/m³)": [12, 24],
    "Vs (m/s)": [100, 650],
    "αgR (g)": [0.05, 1],
}

# Define font
font = ('Lucida Console', 13)

# GUI layout definition
layout = [
    [sg.Text("Define the input parameters", font=font)],
    [
        sg.Column(layout=[
            [sg.Frame(layout=[
                [sg.Text("PI (%)", font=font, size=(20, 1)), sg.InputText(key="-PI-", size=(15, 1), font=font, text_color='red')],
                [sg.Text("H (m)", font=font, size=(20, 1)), sg.InputText(key="-H-", size=(15, 1), font=font, text_color='red')],
                [sg.Text("γ (kN/m³)", font=font, size=(20, 1)), sg.InputText(key="-gamma-", size=(15, 1), font=font, text_color='red')],
                [sg.Text("Vs (m/s)", font=font, size=(20, 1)), sg.InputText(key="-Vs-", size=(15, 1), font=font, text_color='red')],
                [sg.Text("αgR (g)", font=font, size=(20, 1)), sg.InputText(key="-agR-", size=(15, 1), font=font, text_color='red')],
            ], title="Input parameters", font=font)],
        ], justification='left'),

        sg.Column(layout=[
            [sg.Frame(layout=[
                [sg.Text(f"PI (%): {feature_ranges['PI (%)'][0]} ≤ PI ≤ {feature_ranges['PI (%)'][1]}", font=font)],
                [sg.Text(f"H (m): {feature_ranges['H (m)'][0]} ≤ H ≤ {feature_ranges['H (m)'][1]}", font=font)],
                [sg.Text(f"γ (kN/m³): {feature_ranges['γ (kN/m³)'][0]} ≤ γ ≤ {feature_ranges['γ (kN/m³)'][1]}", font=font)],
                [sg.Text(f"Vs (m/s): {feature_ranges['Vs (m/s)'][0]} ≤ Vs ≤ {feature_ranges['Vs (m/s)'][1]}", font=font)],
                [sg.Text(f"αgR (g): {feature_ranges['αgR (g)'][0]} ≤ αgR ≤ {feature_ranges['αgR (g)'][1]}", font=font)],
            ], title="Application scope of the model", font=font)],
        ], justification='center'),
    ],
    [sg.Button("Predict", font=font), sg.Button("Cancel", font=font)],
    [sg.Text("Predicted peak ground acceleration (PGA) and displacement (PGD)", font=font)],

    [
        sg.Column(layout=[
            [sg.Frame(layout=[
                [sg.Text("Predicted PGA (g): ", font=font), sg.InputText(key="-PGA-", font=font, text_color='blue', size=(15, 1))],
                [sg.Text("Predicted PGD (cm): ", font=font), sg.InputText(key="-PGD-", font=font, text_color='blue', size=(15, 1))],
            ], title="Output", font=font)],
        ], justification="left"),
    ],      
            [sg.Text('Author: Ayele T. Chala, Szechenyi Istvan University, Hungary'+ '\n'
             '             Email: chala.ayele.tesema@hallgato.sze.hu')],
]

# Create window with specified size
window = sg.Window("Optimized Machine Learning Tool for Efficient PGA and PGD Predictions",layout, size=(650, 350), resizable=True)

# Main event loop
while True:
    event, values = window.read()
    if event in (None, "Cancel"):
        break
    elif event == "Predict":
        try:
            # Retrieve and validate input values
            PI = float(values["-PI-"])
            H = float(values["-H-"])
            gamma = float(values["-gamma-"])
            Vs = float(values["-Vs-"])
            agR = float(values["-agR-"])

            # Check if inputs are within the defined ranges
            if not (
                feature_ranges["PI (%)"][0] <= PI <= feature_ranges["PI (%)"][1] and
                feature_ranges["H (m)"][0] <= H <= feature_ranges["H (m)"][1] and
                feature_ranges["γ (kN/m³)"][0] <= gamma <= feature_ranges["γ (kN/m³)"][1] and
                feature_ranges["Vs (m/s)"][0] <= Vs <= feature_ranges["Vs (m/s)"][1] and
                feature_ranges["αgR (g)"][0] <= agR <= feature_ranges["αgR (g)"][1]
            ):
                sg.popup("Error: One or more input values are out of the allowed range.")
                continue

            # Prepare and scale the input for model prediction
            input_features = np.array([[PI, H, gamma, Vs, agR]])
            input_features_scaled_pga = pga_scaler_X.transform(input_features)
            input_features_scaled_pgd = pgd_scaler_X.transform(input_features)

            # Make predictions
            pga_pred_scaled = pga_model.predict(input_features_scaled_pga)[0]
            pgd_pred_scaled = pgd_model.predict(input_features_scaled_pgd)[0]

            # Inverse transform predictions
            pga_pred_original = pga_scaler_y.inverse_transform([[pga_pred_scaled]])[0, 0]
            pgd_pred_original = pgd_scaler_y.inverse_transform([[pgd_pred_scaled]])[0, 0]

            # Display the predictions
            window["-PGA-"].update(np.round(pga_pred_original, 3))
            window["-PGD-"].update(np.round(pgd_pred_original, 3))

        except Exception as e:
            sg.popup(f"Error: {e}\n\nInvalid input. Please make sure to enter numeric values.")
            continue

# Close the window
window.close()
