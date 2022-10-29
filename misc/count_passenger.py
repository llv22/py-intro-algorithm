from typing import Dict

def countPassageOptimal(passengers: [str]) -> Dict[str, int]:
    cntOfPassenger = {}
    for p in passengers:
        cntOfPassenger[p] = cntOfPassenger.setdefault(p, 0) + 1
    return cntOfPassenger 
    
def countPassageWorse(passengers: [str])  -> Dict[str, int]:
    passengers = sorted(passengers)
    cntOfPassenger = {}
    cntOfPassenger[passengers[0]] = 1; c = passengers[0]
    for p in passengers[1:]:
        if p == c:
            cntOfPassenger[c] += 1
        else:
            c = p
            cntOfPassenger[c] = 1
    return cntOfPassenger

if __name__ == "__main__":
    passengers = ["US", "CN", "US", "GE"]
    print(f"countPassageOptimal = {countPassageOptimal(passengers)}") 
    print(f"countPassageWorse = {countPassageWorse(passengers)}") 
