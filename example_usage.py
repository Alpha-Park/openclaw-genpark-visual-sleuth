# -*- coding: utf-8 -*-
from client import OpenClawGenParkVisualSleuth

def main():
    sleuth = OpenClawGenParkVisualSleuth()
    print("=== OpenClaw GenPark Visual Evidence Sleuth ===")

    # Scenario 1: Spatial 3D bounding box audit
    objects = [
        {"id": "laptop", "center": [0.0, 0.0, 0.8], "size": [0.35, 0.25, 0.02]},
        {"id": "coffee_mug", "center": [0.3, 0.1, 0.85], "size": [0.08, 0.08, 0.10]}
    ]
    spatial_res = sleuth.audit_spatial_consistency(objects)
    print(f"Spatial Consistency: {spatial_res['verdict']} (Collisions={spatial_res['collision_count']})")

    # Scenario 2: Lighting & shadow vector audit
    shadows = [
        [0.707, 0.0, 0.707],
        [0.68, 0.05, 0.72]
    ]
    light_res = sleuth.audit_light_sources(shadows)
    print(f"Lighting Consistency: {light_res['verdict']} (MaxDeviation={light_res['max_angle_deviation_deg']} deg)")

if __name__ == "__main__":
    main()
