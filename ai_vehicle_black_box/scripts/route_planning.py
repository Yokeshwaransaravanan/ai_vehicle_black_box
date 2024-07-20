import pandas as pd
from geopy.distance import geodesic

def load_route_data(file_path):
    return pd.read_csv(file_path)

def calculate_distance(lat1, lon1, lat2, lon2):
    return geodesic((lat1, lon1), (lat2, lon2)).km

def calculate_optimal_route(routes):
    routes['distance'] = routes.apply(lambda row: calculate_distance(row['latitude'], row['longitude'], row['latitude_dest'], row['longitude_dest']), axis=1)
    return routes.sort_values(by='distance')

def main():
    routes = load_route_data('data/route_data.csv')
    optimal_route = calculate_optimal_route(routes)
    optimal_route.to_csv('data/optimal_route.csv', index=False)

if __name__ == "__main__":
    main()

