from mpi4py import MPI
from ClusterBoss import Worker, Boss, Task
import time
from numpy.random import default_rng
import logging

class SillyFunction(Task.Function):
    def __init__(self, rank):
        super().__init__()
        self.rank = rank


    def run(self, arg):
        wait = default_rng().random()
        time.sleep(wait)
        print('p={} f={}'.format(self.rank, arg), flush=True)
        return arg

class SillyAnalyzer(Task.ResultAnalyzer):
    def __init__(self):
        self.results = []

    def acceptResult(self, result):
        self.results.append(result)

    def postprocess(self):
        s = sorted(self.results)
        print('Unsorted results: {}'.format(self.results))
        print('Sorted results: {}'.format(s))


if __name__=='__main__':

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    logLevel = logging.INFO

    if rank==0:
        args = ('Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot',
            'Golf', 'Hotel', 'India', 'Juliet', 'Kilo', 'Lima', 'Mike',
            'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra',
            'Tango', 'Uniform', 'Whiskey', 'X-Ray', 'Yankee', 'Zulu')
        analyzer = SillyAnalyzer()
        mgr = Boss(args, analyzer, comm=comm, logLevel=logLevel)
        mgr.loop()
        analyzer.postprocess()
    else:
        f = SillyFunction(rank)
        worker = Worker(f, comm=comm, logLevel=logLevel)
        worker.loop()
