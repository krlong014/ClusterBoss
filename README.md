# ClusterBoss

ClusterBoss is an MPI-based distributed task queue manager. It is
designed for running a moderately large number of independent compute-intensive
jobs asynchronously on a small cluster. I'm sure there are better systems
for doing this, but it was faster for me to write my own than to search for one and figure out how to use it.

## Example

See the file example/Silly.py.

## Requirements
- MPI4Py
    - This in turn requires an MPI installation (_e.g._, MPICH, OpenMPI)
- numpy
    - Needed for test suite only
