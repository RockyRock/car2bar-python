# Cartesian to barycentric - Python

This python function converts cartesian coordinates to barycentric coordinates for any point belonging to an unit hypercube in dimension <a href="https://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="https://latex.codecogs.com/svg.latex?n" title="n" /></a>. The hypercube <a href="https://www.codecogs.com/eqnedit.php?latex=\mathcal{H}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\mathcal{H}" title="\mathcal{H}" /></a> is defined as follows,

<a href="https://www.codecogs.com/eqnedit.php?latex=\mathcal{H}&space;=&space;\left\{x&space;\in&space;\left\[&space;0,1&space;\right\]^{n}&space;\right\}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\mathcal{H}&space;=&space;\left\{x&space;\in&space;\left\[&space;0,1&space;\right\]^{n}&space;\right\}" title="\mathcal{H} = \left\{x \in \left\[ 0,1 \right\]^{n} \right\}" /></a>.

The function `car2bar()` takes the cartesian coordinates of any point within the hypercube <a href="https://www.codecogs.com/eqnedit.php?latex=\mathcal{H}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\mathcal{H}" title="\mathcal{H}" /></a> expressed as a column vector. This function returns the barycentric coordinates linked to the <a href="https://www.codecogs.com/eqnedit.php?latex=2^{n}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?2^{n}" title="2^{n}" /></a> vertices of <a href="https://www.codecogs.com/eqnedit.php?latex=\mathcal{H}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\mathcal{H}" title="\mathcal{H}" /></a>. The weights of the barycentric coordinates are ordered based on the binary encoding of the vertex index. For example, the following code converts the cartesian coordinates `car` to the barycentric coordinates `bar` in dimension <a href="https://www.codecogs.com/eqnedit.php?latex=2" target="_blank"><img src="https://latex.codecogs.com/svg.latex?2" title="2" /></a>,

```
>>> import numpy as np
>>> car = np.array([[0], [1]])
>>> bar = car2bar(car)
>>> print(bar)
[[0.]
 [1.]
 [0.]
 [0.]]
```

The vertices coordinated are obtained based on the binary decomposition of their respective indexes,

* <a href="https://www.codecogs.com/eqnedit.php?latex=Index&space;\:&space;0\Leftrightarrow&space;00" target="_blank"><img src="https://latex.codecogs.com/svg.latex?Index&space;\:&space;0\Leftrightarrow&space;00" title="Index \: 0\Leftrightarrow 00" /></a>,
* <a href="https://www.codecogs.com/eqnedit.php?latex=Index&space;\:&space;1\Leftrightarrow&space;01" target="_blank"><img src="https://latex.codecogs.com/svg.latex?Index&space;\:&space;1\Leftrightarrow&space;01" title="Index \: 1\Leftrightarrow 01" /></a>,
* <a href="https://www.codecogs.com/eqnedit.php?latex=Index&space;\:&space;2\Leftrightarrow&space;10" target="_blank"><img src="https://latex.codecogs.com/svg.latex?Index&space;\:&space;2\Leftrightarrow&space;10" title="Index \: 2\Leftrightarrow 10" /></a>,
* <a href="https://www.codecogs.com/eqnedit.php?latex=Index&space;\:&space;3\Leftrightarrow&space;11" target="_blank"><img src="https://latex.codecogs.com/svg.latex?Index&space;\:&space;3\Leftrightarrow&space;11" title="Index \: 3\Leftrightarrow 11" /></a>.

The function can be used for a non unit hypercube by normalizing the cartesian coordinates between <a href="https://www.codecogs.com/eqnedit.php?latex=0" target="_blank"><img src="https://latex.codecogs.com/svg.latex?0" title="0" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=1" target="_blank"><img src="https://latex.codecogs.com/svg.latex?1" title="1" /></a>.
