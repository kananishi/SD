# SD
Código dos trabalhos de Sistemas Distribuidos

## Linda
This model is implemented as a "coordination language" in which several primitives operating on ordered sequence of typed data objects, "tuples," are added to a sequential language, such as C, and a logically global associative memory, called a tuplespace, in which processes store and retrieve tuples.

The original Linda model requires four operations that individual workers perform on the tuples and the tuplespace:

    *in atomically reads and removes—consumes—a tuple from tuplespace
    *rd non-destructively reads a tuplespace
    *out produces a tuple, writing it into tuplespace (tuple may be duplicated in tuplespace)
    *eval creates new processes to evaluate tuples, writing the result into tuplespace
