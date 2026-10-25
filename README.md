# multisensor-anomaly-detection
Independent research project exploring machine learning, anomaly detection, and sensor fusion using hyperspectral imaging (HSI), LiDAR, and radar-like measurements.

## Research Question
Under which conditions does combining spectral, geometric, and radar-like measurements improve land-cover classification or anomaly detection compared with using individual sensor modalities?

## Planned experiments

### Experiment A – Real-World Land-Cover Classification

Use the MUUFL Gulfport dataset containing co-registered hyperspectral imagery (HSI) and LiDAR-derived measurements.

Compare HSI-only, LiDAR-only, and combined HSI + LiDAR classification models to investigate the benefits and limitations of sensor fusion.

### Experiment B – Simulated Multisensor Anomaly Detection

Develop a shared simulated environment observed by three sensor modalities: HSI, LiDAR, and radar-like sensing.

Train anomaly-detection models to identify unusual observations and compare individual sensors against different fusion strategies.

Planned investigations include PCA reconstruction error, Isolation Forest, Kalman filtering where appropriate, temporal behavior, and robustness to measurement noise, sensor misalignment, and small-object detectability.

Simulated results will be evaluated separately from real-world measurements.

## Current Status

### Milestone M0 – Project Setup: Completed

The development environment is configured, and the first synthetic HSI visualizations have been implemented and verified.

Next milestone M1 – Real Dataset Inspection.