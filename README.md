# NYC Solar Investment Screening

## Overview

This project was developed during a sustainability-focused hackathon to identify and prioritize rooftop solar investment opportunities across New York City.

The platform combines building-level property information, rooftop area estimation, solar energy production assumptions, and financial feasibility analysis to identify buildings where solar installations are likely to generate attractive economic returns.

The goal is to support data-driven decision making for property owners, communities, and policymakers seeking to accelerate renewable energy adoption in urban environments.

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
```

---

## Team Project

This project was developed as part of a hackathon by a multidisciplinary team.

My contributions focused on:

* Solar potential estimation
* Financial feasibility modeling
* Building screening methodology
* Data processing and analysis
* Geospatial opportunity identification

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

```
```

