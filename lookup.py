#!/usr/bin/env python3
"""
Hellraiser: Revival — Safe Codes & Keypad Combinations CLI Lookup Tool
Verified against retail Patch 1.02 (Steam / PS5 / Xbox Series X|S).
Full interactive web solver: https://hellraisergamehub.com
"""

import json
import sys
from pathlib import Path

def main():
    json_path = Path(__file__).parent / "codes.json"
    if not json_path.exists():
        print("Error: codes.json not found.", file=sys.stderr)
        sys.exit(1)

    with open(json_path, "r", encoding="utf-8") as f:
        codes = json.load(f)

    query = " ".join(sys.argv[1:]).strip().lower()

    print("=" * 68)
    print(" Clive Barker's Hellraiser: Revival — Safe Codes & Keypad Lookup")
    print(" Web Interactive Map & Guides: https://hellraisergamehub.com")
    print("=" * 68)

    if not query:
        print("\nAll 10 Verified Safe Codes (Patch 1.02):\n")
        print(f"{'#':<3} {'Location':<32} {'Code':<8} {'Loot':<20}")
        print("-" * 68)
        for item in codes:
            code_str = item['code'] + (f" / {item['alternate_code']}" if item.get('alternate_code') else "")
            print(f"{item['id']:<3} {item['location']:<32} {code_str:<8} {item['loot']}")
        print("\nTip: Run `python lookup.py <keyword>` (e.g. `python lookup.py sewer` or `python lookup.py music`)")
        return

    matched = [
        c for c in codes
        if query in c['location'].lower() or query in c['chapter'].lower() or query in c['loot'].lower()
    ]

    if not matched:
        print(f"\nNo safe codes matched query: '{query}'")
        print("Visit https://hellraisergamehub.com/blog/all-safe-codes-keypad-combinations for complete walkthrough.")
        return

    print(f"\nFound {len(matched)} match(es) for '{query}':\n")
    for item in matched:
        print(f"[{item['id']}] {item['location']} ({item['chapter']})")
        print(f"    Code: {item['code']}" + (f" (Alternative: {item['alternate_code']})" if item.get('alternate_code') else ""))
        print(f"    Loot: {item['loot']}")
        print(f"    Hint: {item['hint']}\n")

if __name__ == "__main__":
    main()
