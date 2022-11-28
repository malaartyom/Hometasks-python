def format_table(benchmarks, algos, result):
    first = "| " + "Benchmark".ljust(len(max(benchmarks, key=lambda x: len(x))) + 1," ")
    for i in algos:
        first += "| " + i.ljust(len(max(algos, key=lambda x: len(x)))," ") + " "
    first += "|"
    print(first)
    second = "|" + (len(first) - 2) * "-" + "|"
    print(second)
    for i in benchmarks:
        s = "| " + i.ljust(len(max(benchmarks, key=lambda x: len(x))) + 1," ")
        for j in result[benchmarks.index(i)]:
            s += "| " + str(j).ljust(len(max(algos, key=lambda x: len(x)))," ") + " "
        s += "|"
        print(s)
benchmarks = ["best case", "worst case"]
algos = ["quick sort", "merge sort", "bubble sort"]
result = [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]]
format_table(benchmarks, algos, result)