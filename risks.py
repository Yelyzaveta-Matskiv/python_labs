import threading
import random
import time
from tqdm import tqdm

price_per_unit = 10 

class Warehouse:
    def __init__(self, name, meds):
        self.name = name
        self.meds = meds
        self.lock = threading.Lock()

    def steal(self, requested_amount):
        with self.lock:
            if self.meds <= 0:
                return 0, "empty"

            event = random.choice(["success", "partial", "caught"])

            if event == "caught":
                return 0, "caught"

            if event == "partial":
                max_possible = min(requested_amount, self.meds)
                stolen = random.randint(1, max_possible)
            else:  
                stolen = min(requested_amount, self.meds)

            self.meds -= stolen
            return stolen, event


class Runner(threading.Thread):
    def __init__(self, name, warehouse, progress_bar):
        super().__init__()
        self.name = name
        self.warehouse = warehouse
        self.progress_bar = progress_bar
        self.earned = 0
        self.log = []

    def run(self):
        for i in range(10):
            amount_to_steal = random.randint(10, 30)

            stolen, event = self.warehouse.steal(amount_to_steal)

            if stolen > 0:
                gain = stolen * price_per_unit
                self.earned += gain
                self.log.append(
                    f"[{self.name}] raid #{i+1}: event={event}, "
                    f"goal={amount_to_steal}, stolen={stolen}, gain={gain}"
                )
            else:
                if event == "empty":
                    self.log.append(
                        f"[{self.name}] raid #{i+1}: warehouse is empty, nothing was taken."
                    )
                elif event == "caught":
                    self.log.append(
                        f"[{self.name}] raid #{i+1}: caught, nothing taken"
                    )

            time.sleep(random.uniform(0.1, 0.5))
            self.progress_bar.update(1)


def run_simulation(sim_id=1, runners_count=5, warehouses_count=4):
    print(f"\n=== Simulation #{sim_id} ===")

    warehouses = [
        Warehouse(f"warehouse-{i+1}", random.randint(100, 300))
        for i in range(warehouses_count)
    ]

    bars = [
        tqdm(
            total=10,
            desc=f"Runner-{i+1}",
            position=i,
            leave=False
        )
        for i in range(runners_count)
    ]

    runners = [
        Runner(
            name=f"Runner-{i+1}",
            warehouse=random.choice(warehouses),
            progress_bar=bars[i],
        )
        for i in range(runners_count)
    ]

    for r in runners:
        r.start()

    for r in runners:
        r.join()

    for b in bars:
        b.close()

    total_earned = sum(r.earned for r in runners)

    print("\n--- REPORT ON WAREHOUSES ---")
    for w in warehouses:
        print(f"{w.name}: medicine left = {w.meds}")

    print("\n--- REPORT ON RUNNERS ---")
    for r in runners:
        print(f"{r.name}: total profit = {r.earned}")

    print(f"\nTOTAL PROFIT: {total_earned}")
    print("===============")

    return total_earned


if __name__ == "__main__":
    simulations = 3
    all_results = []
    for i in range(1, simulations + 1):
        earned = run_simulation(sim_id=i)
        all_results.append(earned)

    print("\n=== SUMMARY OF ALL SIMULATIONS ===")
    for i, res in enumerate(all_results, start=1):
        print(f"Simulation #{i}: total profit = {res}")
    print(f"Average profit: {sum(all_results) / len(all_results):.2f}")