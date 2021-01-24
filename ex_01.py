from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--duration_of_work', type=int)
parser.add_argument('--rate', type=float)
parser.add_argument('--bonus', type=float, default=0)

args = parser.parse_args()
salary = args.duration_of_work * args.rate + args.bonus
print(
    f'За месяц отработано {args.duration_of_work} часов. При ставке {args.rate} и премии {args.bonus} к выплате выходит {salary}')
#