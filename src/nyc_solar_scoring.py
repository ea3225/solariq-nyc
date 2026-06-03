import pandas as pd
import os

# Dynamically get the exact folder where this Python script lives
script_dir = os.path.dirname(os.path.abspath(__file__))
in_df_path = os.path.join(script_dir, "pluto_full.csv")
out_df_path = os.path.join(script_dir, "solar_results.csv")

# Assumptions
KWH_PER_KW_PER_YEAR = 1200
COST_PER_WATT = 3.0
ELECTRICITY_RATE = 0.24
INCENTIVE_DISCOUNT = 0.30

# Load your dataset 
df = pd.read_csv(in_df_path, low_memory=False)

df['bldgarea'] = pd.to_numeric(df['bldgarea'], errors='coerce').fillna(0)
df['numfloors'] = pd.to_numeric(df['numfloors'], errors='coerce').fillna(1)
# Ensure floor count is at least 1 to avoid DivisionByZero
df.loc[df['numfloors'] <= 0, 'numfloors'] = 1

def classify_building(row):
    bldg_area = row.get('bldgarea', 0)
    num_floors = row.get('numfloors', 1)
    
    if pd.isna(bldg_area) or bldg_area <= 0:
        return pd.Series(["❌ Not Suggested", 0, 0, 0, 0, 0, 0])

    # 1. Roof estimate using footprint!
    footprint_sqft = bldg_area / num_floors
    roof_sqft = footprint_sqft * 0.6  

    if roof_sqft < 500:
        return pd.Series(["❌ Not Suggested (Too Small)", roof_sqft, 0, 0, 0, 0, 0])

    # 2. System size
    system_kw = (roof_sqft * WATTS_PER_SQFT) / 1000
    if system_kw < 5:
        return pd.Series(["❌ Not Suggested (Under 5kW)", roof_sqft, system_kw, 0, 0, 0, 0])

    # 3. Energy production
    annual_kwh = system_kw * KWH_PER_KW_PER_YEAR

    # 4. Cost
    install_cost = system_kw * 1000 * COST_PER_WATT
    net_cost = install_cost * (1 - INCENTIVE_DISCOUNT)

    # 5. Savings
    annual_savings = annual_kwh * ELECTRICITY_RATE
    if annual_savings == 0:
        return pd.Series(["❌ Not Suggested", roof_sqft, system_kw, annual_kwh, net_cost, 0, 0])

    payback = net_cost / annual_savings

    # 6. Hard constraints
    is_landmark = pd.notna(row.get('landmark'))
    in_histdist = pd.notna(row.get('histdist'))

    if is_landmark or in_histdist:
        return pd.Series(["❌ Not Suggested (Landmark)", roof_sqft, system_kw, annual_kwh, net_cost, annual_savings, payback])

    # 7. Classification
    if payback < 8:
        rec = "✅ Highly Recommended"
    elif payback < 15:
        rec = "⚠️ Recommended"
    else:
        rec = "❌ Not Suggested"

    return pd.Series([rec, roof_sqft, system_kw, annual_kwh, net_cost, annual_savings, payback])

# Apply to all buildings 
out_cols = ['Recommendation', 'Usable_Roof_Sqft', 'System_kW', 'Annual_kWh', 'Net_Cost_$', 'Annual_Savings_$', 'Payback_Years']
df[out_cols] = df.apply(classify_building, axis=1)

# Save results
df.to_csv(out_df_path, index=False)

# Presentation Aggregate Metrics
recommended_all = df[df['Recommendation'] == '✅ Highly Recommended']
if not recommended_all.empty:
    total_buildings = len(recommended_all)
    # Convert kWh to GWh
    total_gwh = recommended_all['Annual_kWh'].sum() / 1_000_000
    # Convert Savings to Millions
    total_savings_millions = recommended_all['Annual_Savings_$'].sum() / 1_000_000
    # CO2 offset: ~0.0004 metric tons per kWh (EPA national grid offset average for presentations)
    total_co2_tons = recommended_all['Annual_kWh'].sum() * 0.0004

    print("\n" + "="*50)
    print("🌍 NYC CITY-WIDE IMPACT AGGREGATES")
    print("="*50)
    print(f"🏢 Total Identified Targets: {total_buildings:,.0f} buildings")
    print(f"⚡ Potential Clean Energy:   {total_gwh:,.2f} GWh/year")
    print(f"💵 Total Economic Savings:   ${total_savings_millions:,.2f} million/year")
    print(f"🌱 Carbon Offset:            {total_co2_tons:,.0f} tons CO2/year")
    print("="*50)

# example
# Filter for recommended buildings that actually have an address listed
recommended = df[(df['Recommendation'] == '✅ Highly Recommended') & (df['address'].notna())]

if not recommended.empty:
    # Sort by System Size to find a really impressive/large building for the presentation
    best = recommended.sort_values(by='System_kW', ascending=False).iloc[0]
    
    # We use encode/decode to safely print to terminal without emoji encoding crash issues 
    print("\n" + "="*50)
    print("🏢 PRESENTATION EXAMPLE BUILDING")
    print("="*50)
    print(f"📍 Address:           {best['address']}")
    print(f"📐 Usable Roof Area:  {best['Usable_Roof_Sqft']:,.0f} sq ft")
    print(f"⚡ System Size:       {best['System_kW']:,.1f} kW")
    print(f"☀️  Annual Energy:    {best['Annual_kWh']:,.0f} kWh/year")
    print(f"💵 Install Cost:      ${best['Net_Cost_$']:,.2f} (after incentives)")
    print(f"💰 Annual Savings:    ${best['Annual_Savings_$']:,.2f}/year")
    print(f"📉 Payback Period:    {best['Payback_Years']:.1f} years")
    print("="*50 + "\n")
else:
    print("No highly recommended buildings found.")
