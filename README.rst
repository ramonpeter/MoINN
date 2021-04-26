======
MoINN
======

|CI| |Black|

.. |CI| image:: https://github.com/ramonpeter/MoINN/actions/workflows/ci.yml/badge.svg
   :alt: Build Status

.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

These are the **M**\ odules for **I**\ nvertible **N**\ eural **N**\ etworks (**MoINN**)

It is mainly a Tensorflow 2 implementation of the **FrEIA** framework: https://github.com/VLL-HD/FrEIA

Currently implemented coupling blocks are:

- NICE [1]_
- Real NVP [2]_
- GLOW [3]_
- GIN [4]_
- SPADE [5]_
- All in one Black (FrEIA)

Installation
-------------

Dependencies
~~~~~~~~~~~~

+---------------------------+-------------------------------+
| **Package**               | **Version**                   |
+---------------------------+-------------------------------+
| Python                    | 3.6 - 3.8                     |
+---------------------------+-------------------------------+
| Tensorflow                | >= 2.1.0                      |
+---------------------------+-------------------------------+
| Numpy                     | >= 1.15.0                     |
+---------------------------+-------------------------------+
| Scipy                     | >= 1.5                        |
+---------------------------+-------------------------------+

Download + Install
~~~~~~~~~~~~~~~~~~~~~~~~~~

To just install the modules for usage:

.. code:: sh

   pip install git+https://github.com/ramonpeter/MoINN.git
   
For development:

.. code:: sh

   # clone the repository
   git clone https://github.com/ramonpeter/MoINN.git
   # then install in dev mode
   cd EventGAN
   python setup.py develop


References
----------

.. [1] Dinh et al., "NICE: Non-linear Independent Components Estimation", `1410.8516 [cs.LG]`_
.. _`1410.8516 [cs.LG]` : https://arxiv.org/abs/1410.8516v6

.. [2] Dinh et al., “Density estimation using Real NVP,” `1605.08803 [cs.LG]`_
.. _`1605.08803 [cs.LG]` : https://arxiv.org/abs/1605.08803

.. [3] Kingma and Dhariwal, “Glow: Generative Flow with Invertible 1x1 Convolutions”, `1807.03039 [cs.LG]`_
.. _`1807.03039 [cs.LG]` : https://arxiv.org/abs/1807.03039

.. [4] Sorrenson et al., "Disentanglement by Nonlinear ICA with General Incompressible-flow Networks (GIN)", `2001.04872 [cs.LG]`_
.. _`2001.04872 [cs.LG]` : https://arxiv.org/abs/2001.04872

.. [5] Park et al., "Semantic Image Synthesis with Spatially-Adaptive Normalization", `1903.07291 [cs.LG]`_
.. _`1903.07291 [cs.LG]` : https://arxiv.org/abs/1903.07291).

