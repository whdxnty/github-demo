
# Print iterations progress
def print_progress(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_len = int(length * iteration // total)
    bar = fill * filled_len + '-' * (length - filled_len)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total: print()


# from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor, as_completed

class MultiThreadingClass:
    
    def __init__(self, func, list_args, num_threads=4):
        
        self.num_completed = 0
        self.job = func
        self.num_threads = num_threads
        self.total = len(list_args)
        self.list_args = list_args
    
    def run(self):
        with ProcessPoolExecutor(max_workers=self.num_threads) as pool:
            futures = [pool.submit(self.job, self.list_args[i]) for i in range(self.total)]
            for f in as_completed(futures):
                f.result()
                self.num_completed += 1
                print_progress(self.num_completed, self.total)
