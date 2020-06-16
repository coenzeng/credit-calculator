import argparse
from math import ceil

parser = argparse.ArgumentParser()
parser.add_argument('--type', required=True)
parser.add_argument('--principal', required=True)
parser.add_argument('--periods', required=True)
parser.add_argument('--interest', required=True)
args = parser.parse_args()

type1 = args.type
p = int(args.principal) 
n = int(args.periods)
i = float(args.interest)
i = i/1200

if type1 == "diff":
    m = 1
    total_d = 0
    while (m <= n):
        d = ceil(p/n + i*(p - (p*(m-1))/n))
        print("Month " + str(m) + ": paid out $" + str(d))
        total_d += d
        m += 1

    overpayment = total_d - p
    print(f"overpayment = {overpayment}")

