# -*- coding: utf-8 -*-
import sys, json
from client import OpenClawGenParkVisualSleuth

sleuth = OpenClawGenParkVisualSleuth()

def run_tool(name, args):
    if name == "audit_spatial_consistency":
        dets = args.get("object_detections", [])
        return sleuth.audit_spatial_consistency(dets)
    elif name == "audit_light_sources":
        vecs = args.get("shadow_vectors", [])
        return sleuth.audit_light_sources(vecs)
    else:
        raise ValueError(f"Unknown tool: {name}")

def main():
    if "--test" in sys.argv:
        print("[TEST] Running OpenClaw Visual Sleuth Self-Test...")
        d1 = [{"id": "car", "center": [0,0,0], "size": [2,2,2]},
              {"id": "bike", "center": [0,0,0], "size": [1,1,1]}]
        col = sleuth.audit_spatial_consistency(d1)
        assert col["spatial_consistent"] is False
        light = sleuth.audit_light_sources([[1, 0, 1], [0.98, 0.02, 1]])
        assert light["lighting_consistent"] is True
        print("[TEST] All tests passed successfully!")
        return

    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            res = run_tool(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"jsonrpc": "2.0", "id": req.get("id"), "result": res}))
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}}))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
