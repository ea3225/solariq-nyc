# SolarIQ NYC

## Overview

SolarIQ NYC is an AI-powered decision-support platform that helps New York City property owners identify, evaluate, and finance rooftop solar installations. By combining building data, rooftop estimation, energy generation modeling, incentive optimization, and geospatial visualization, the platform transforms underutilized rooftops into actionable renewable energy investment opportunities.

---

## Motivation

Recent changes in energy markets and distributed energy participation have created new opportunities for residential and commercial property owners to benefit from solar generation.

However, evaluating solar feasibility at scale remains challenging due to the large number of buildings, varying roof characteristics, regulatory constraints, and economic considerations.

This project addresses that challenge by automatically screening thousands of properties and identifying those with the strongest investment potential.

---

## Methodology

### Building Screening

For each building, the system:

1. Estimates usable rooftop area from publicly available building characteristics.
2. Estimates potential solar system capacity (kW).
3. Estimates annual energy generation (kWh).
4. Calculates installation costs after incentives.
5. Estimates annual electricity cost savings.
6. Computes expected payback period.
7. Produces a recommendation score.

Buildings located within landmark or historic districts are excluded from recommendation due to potential installation restrictions.

---

## Financial Model

The analysis estimates:

* Solar system size (kW)
* Annual energy generation
* Installation cost
* Net cost after incentives
* Annual savings
* Payback period

Buildings are classified as:

| Category           | Criteria                                     |
| ------------------ | -------------------------------------------- |
| Highly Recommended | Payback < 8 years                            |
| Recommended        | Payback < 15 years                           |
| Not Suggested      | Payback ≥ 15 years or regulatory constraints |

---

## Geospatial Visualization

The project generates an interactive map highlighting high-potential solar opportunities throughout New York City.

Each location includes:

* Building address
* Estimated system size
* Annual savings
* Payback period

The map enables users to explore solar investment opportunities spatially and identify areas with strong renewable energy potential.

---

## Data Sources

The analysis uses publicly available New York City property and geospatial information.

Raw datasets are not redistributed in this repository due to size limitations and external ownership.

---

## Repository Structure

```text
nyc-solar-investment-screening/
│
├── README.md
├── requirements.txt
├── src/
│   ├── nyc_solar_scoring.py
│   └── generate_map.py
└── examples/
    └── solar_potential_map.html
└── presentation/
    └── solarIQ_presentation.pdf
```

---

## Team Project

This project was developed as part of a hackathon by a multidisciplinary team.

My contributions focused on the analytical backbone of the platform, including:

- Building-level solar potential estimation
- Rooftop area and system sizing methodology
- Financial feasibility modeling
- Payback period analysis
- Economic impact estimation
- Geospatial opportunity mapping
- Data processing and screening of NYC building datasets

Additional team members contributed to the model development, idea generation, user interface, demo development, and project presentation.

---

## Future Improvements

Potential extensions include:

* Satellite-image-based rooftop detection
* Building-level energy demand forecasting
* Shadow and shading analysis
* Dynamic electricity pricing integration
* Community solar and energy market participation modeling
* Optimization of installation portfolios under budget constraints

---

## Technologies

* Python
* Pandas
* Folium
* Geospatial Analysis
* Financial Modeling
* Renewable Energy Analytics
