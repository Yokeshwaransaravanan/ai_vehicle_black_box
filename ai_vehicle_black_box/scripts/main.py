import tensorflow as tf
import pandas as pd
from predictive_maintenance import load_data as load_maintenance_data
from energy_optimization import load_data as load_energy_data
from route_planning import load_route_data, calculate_optimal_route

def load_models():
    maintenance_model = tf.keras.models.load_model('models/predictive_maintenance_model.h5')
    energy_model = tf.keras.models.load_model('models/energy_optimization_model.h5')
    return maintenance_model, energy_model

def main():
    maintenance_model, energy_model = load_models()

    maintenance_data = pd.read_csv('data/maintenance_data.csv')
    energy_data = pd.read_csv('data/energy_data.csv')
    route_data = pd.read_csv('data/route_data.csv')

    maintenance_features = maintenance_data.drop('fault', axis=1)
    maintenance_predictions = maintenance_model.predict(maintenance_features)
    maintenance_data['predicted_fault'] = maintenance_predictions

    energy_features = energy_data.drop('energy_usage', axis=1)
    energy_predictions = energy_model.predict(energy_features)
    energy_data['predicted_energy_usage'] = energy_predictions

    optimal_route = calculate_optimal_route(route_data)

    maintenance_data.to_csv('data/maintenance_predictions.csv', index=False)
    energy_data.to_csv('data/energy_predictions.csv', index=False)
    optimal_route.to_csv('data/optimal_route.csv', index=False)

    print("Maintenance Predictions:\n", maintenance_data[['fault', 'predicted_fault']].head())
    print("\nEnergy Predictions:\n", energy_data[['energy_usage', 'predicted_energy_usage']].head())
    print("\nOptimal Route:\n", optimal_route.head())

if __name__ == "__main__":
    main()

