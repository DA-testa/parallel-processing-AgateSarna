# python3

def parallel_processing(n, m, data):
    output = []
    threads = [(i, 0) for i in range(n)]
    for i in range(m):
        threads.sort(key=lambda x: x[1])
        time = data[i]
        index, time_finished = threads[0]
        output.append((index, time_finished))
        threads[0] = (index, time_finished + time)


    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    # n = 0
    # m = 0
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    #data = []

    # TODO: create the function
    result = parallel_processing(n, m, data)
    
    # TODO: print out the results, each pair in it's own line
    for index, start_time in result:
        print(index, start_time)


if __name__ == "__main__":
    main()