# -*- coding: utf-8 -*-
"""
OpenClaw GenPark Visual Sleuth
Standard Library only: math, typing.
Visual evidence chain and spatial bounding consistency auditor.
Evaluates 3D IoU bounding collisions and directional lighting ray alignment.
"""

import math
from typing import Dict, List, Tuple, Any

class OpenClawGenParkVisualSleuth:
    def _dot(self, v1: Tuple[float, float, float], v2: Tuple[float, float, float]) -> float:
        return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

    def _norm(self, v: Tuple[float, float, float]) -> float:
        return math.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2])

    def audit_spatial_consistency(self, object_detections: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        object_detections: [{"id": "car", "center": [0,0,1], "size": [1.8, 4.2, 1.4]},
                             {"id": "pedestrian", "center": [0.2, 0.1, 1], "size": [0.5, 0.5, 1.7]}]
        Checks for physically impossible bounding box intersections (interpenetration).
        """
        interpenetrations = []
        n = len(object_detections)

        for i in range(n):
            for j in range(i + 1, n):
                obj_a = object_detections[i]
                obj_b = object_detections[j]

                c_a = obj_a.get("center", [0, 0, 0])
                c_b = obj_b.get("center", [0, 0, 0])
                s_a = obj_a.get("size", [1, 1, 1])
                s_b = obj_b.get("size", [1, 1, 1])

                # Axis-Aligned Bounding Box overlap along x, y, z
                overlap_x = max(0.0, min(c_a[0] + s_a[0]/2, c_b[0] + s_b[0]/2) - max(c_a[0] - s_a[0]/2, c_b[0] - s_b[0]/2))
                overlap_y = max(0.0, min(c_a[1] + s_a[1]/2, c_b[1] + s_b[1]/2) - max(c_a[1] - s_a[1]/2, c_b[1] - s_b[1]/2))
                overlap_z = max(0.0, min(c_a[2] + s_a[2]/2, c_b[2] + s_b[2]/2) - max(c_a[2] - s_a[2]/2, c_b[2] - s_b[2]/2))

                inter_vol = overlap_x * overlap_y * overlap_z
                if inter_vol > 0.05:
                    vol_a = s_a[0] * s_a[1] * s_a[2]
                    vol_b = s_b[0] * s_b[1] * s_b[2]
                    overlap_ratio = inter_vol / min(vol_a, vol_b)
                    interpenetrations.append({
                        "object_a": obj_a.get("id"),
                        "object_b": obj_b.get("id"),
                        "intersection_volume": round(inter_vol, 3),
                        "overlap_ratio": round(overlap_ratio, 3)
                    })

        is_consistent = len(interpenetrations) == 0
        return {
            "spatial_consistent": is_consistent,
            "collision_count": len(interpenetrations),
            "collisions": interpenetrations,
            "verdict": "PHYSICALLY_REALISTIC" if is_consistent else "IMPOSSIBLE_COLLISION_DETECTED"
        }

    def audit_light_sources(self, shadow_vectors: List[List[float]]) -> Dict[str, Any]:
        """
        shadow_vectors: list of 3D directional vectors pointing towards the apparent light source.
        Checks for multi-directional shadow hallucination (common in AI generated fakes).
        """
        if len(shadow_vectors) < 2:
            return {"lighting_consistent": True, "max_angle_deviation_deg": 0.0}

        angles = []
        for i in range(len(shadow_vectors)):
            for j in range(i + 1, len(shadow_vectors)):
                v1 = tuple(shadow_vectors[i])
                v2 = tuple(shadow_vectors[j])
                n1 = self._norm(v1)
                n2 = self._norm(v2)
                if n1 > 1e-4 and n2 > 1e-4:
                    cos_theta = max(-1.0, min(1.0, self._dot(v1, v2) / (n1 * n2)))
                    ang = math.degrees(math.acos(cos_theta))
                    angles.append(ang)

        max_dev = max(angles, default=0.0)
        is_consistent = max_dev <= 25.0

        return {
            "lighting_consistent": is_consistent,
            "max_angle_deviation_deg": round(max_dev, 2),
            "verdict": "UNIFIED_LIGHT_SOURCE" if is_consistent else "MULTIPLE_CONFLICTING_SHADOWS"
        }
