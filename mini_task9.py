def flatten(a):
    ret_a = []
    for i in a:
        if isinstance(i, list):
            ret_a.extend(flatten(i))
        else:
            ret_a.append(i)
    return ret_a

def format_table(benchmarks, algos, result):
    help_bench = []
    help_bench.extend(benchmarks)
    help_bench.append('Benchmark')
    help = [str(i) for i in flatten(result)]
    help.extend(algos)
    print(help)
    first = "| " + "Benchmark".ljust(len(max(help_bench, key=lambda x: len(x))) + 1," ")
    for i in algos:
        first += "| " + i.ljust(len(max(help, key=lambda x: len(x)))," ") + " "
    first += "|"
    print(first)
    second = "|" + (len(first) - 2) * "-" + "|"
    print(second)
    for i in benchmarks:
        s = "| " + i.ljust(len(max(help_bench, key=lambda x: len(x))) + 1," ")
        for j in result[benchmarks.index(i)]:
            s += "| " + str(j).ljust(len(max(help, key=lambda x: len(x)))," ") + " "
        s += "|"
        print(s)
benchmarks = ["b", "w"]
algos = ["quick sort", "merge sort", "bubble sort"]
result = [[1.224823048023742349237492343, 1.56, 2.0], [3.3, 2.9, 3.9]]
format_table(benchmarks, algos, result)