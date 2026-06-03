import pandas as pd
import folium
import os

# Dynamically get the exact folder where this Python script lives
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "solar_results.csv")

print(f"Loading {csv_path}...")
# We load the results that you already generated!
df = pd.read_csv(csv_path, low_memory=False)

# Filter for Highly Recommended buildings that actually have GPS coordinates
recommended = df[(df['Recommendation'] == '✅ Highly Recommended') & 
                 (df['latitude'].notna()) & 
                 (df['longitude'].notna())]

print(f"Found {len(recommended)} mappable highly recommended buildings.")
print("To prevent browser lag, plotting the top 500 largest systems...")

# Sorting by System Size and taking the top 500
top_buildings = recommended.sort_values(by='System_kW', ascending=False).head(500)

# Calculate map center (average of coordinates)
center_lat = top_buildings['latitude'].mean()
center_lon = top_buildings['longitude'].mean()

# Create a slick dark mode map
m = folium.Map(location=[center_lat, center_lon], zoom_start=11, tiles='CartoDB dark_matter')

# Add all 500 buildings to the map
for idx, row in top_buildings.iterrows():
    address = row.get('address', 'Unknown Address')
    kw = row.get('System_kW', 0)
    savings = row.get('Annual_Savings_$', 0)
    payback = row.get('Payback_Years', 0)
    
    # HTML formatted popup for when you click the blip
    popup_text = f"""
    <div style='font-family: Arial; font-size: 14px;'>
        <b style='color: #4CAF50;'>{address}</b><hr style='margin: 5px 0px;'>
        <b>System Size:</b> {kw:,.1f} kW<br>
        <b>Annual Savings:</b> ${savings:,.2f}<br>
        <b>Payback:</b> {payback:.1f} Years
    </div>
    """
    
    # Dynamic radius: bigger systems get slightly bigger circles
    radius_size = max(3, min(10, kw / 100))
    
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=radius_size, 
        color='#00FF00', # Neon green for clean energy!
        weight=1,
        fill=True,
        fill_color='#00FF00',
        fill_opacity=0.7,
        tooltip=f"{address} (Click for Details)", # Text when hovering
        popup=folium.Popup(popup_text, max_width=300)
    ).add_to(m)

# Export to an interactive HTML file precisely into the hackathon folder
output_file = os.path.join(script_dir, "solar_potential_map.html")
m.save(output_file)
print(f"Success! Open \n{output_file}\nin your web browser to view your interactive map!")
