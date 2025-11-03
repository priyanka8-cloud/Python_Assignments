def read_expenses(file):
    data = []
    try:
        with open(file) as f:
            for line in f:
                if not line.strip(): 
                    continue
                parts = line.strip().split(',')
                if len(parts) == 3:
                    try:
                        data.append((parts[0], parts[1], float(parts[2])))
                    except:
                        print("Skipping bad line:", line.strip())
                else:
                    print("Skipping bad line:", line.strip())
    except FileNotFoundError:
        print("File not found!")
    return data

def calculate(records):
    total = sum(a for _, _, a in records)
    cat, day = {}, {}
    for d, c, a in records:
        cat[c] = cat.get(c, 0) + a
        day[d] = day.get(d, 0) + a
    high = max(day, key=day.get)
    return total, cat, high, day[high]

def write_summary(total, cat, high, high_amt, file):
    with open(file, "w", encoding="utf-8") as f:   # <-- added encoding
        f.write("================= Expense Summary (October 2025) =================\n")
        f.write(f"Total Monthly Expense: ₹{total:.0f}\n\nCategory-wise Breakdown:\n")
        for c, a in cat.items():
            f.write(f"{c:<14}: ₹{a:.0f}\n")
        f.write(f"\nHighest Spending Day: {high} (₹{high_amt:.0f})\n")
        f.write("=================================================================\n")


inp = input("Enter input filename: ")
out = input("Enter output summary filename: ")
rec = read_expenses(inp)
if not rec:
    print("No records found.")
else:
    t, c, h, ha = calculate(rec)
    write_summary(t, c, h, ha, out)
    print("Summary saved to", out)
