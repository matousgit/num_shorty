matousgit/num_shorty
====================

.. image:: https://img.shields.io/pypi/v/num-shorty.svg
    :target: https://pypi.org/project/num-shorty/
    :alt: Latest Version

``num_shorty`` converts an integer to a hexdigest like string - except not 16 length but provided alphabet length

**Example**:

.. code-block:: pycon

    >>> from import num_shorty
    >>> num_shorty.short(123456789)
    '8m0Kx'
    >>> num_shorty.expand('8m0Kx')
    123456789

**You can implement your own alphabet set**

.. code-block:: pycon

    >>> from import num_shorty
    >>> num_shorty.short(123456789, alphabet='abcdefgABCDEFG-*!:_')
    'cE!geD-'
    >>> num_shorty.expand('cE!geD-', alphabet='abcdefgABCDEFG-*!:_')
    123456789

