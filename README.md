pytest-talk
===========
Code samples used in my Talk at [The Developers Conference 2015][#tdc2015]

Slides can be found at [Slide Share][#slides]

[#tdc2015]: http://www.thedevelopersconference.com.br/tdc/2015/saopaulo/trilha-python
[#slides]: https://pt.slideshare.net/erickwilder/pytest-escreva-menos-teste-mais-50449095


Running the examples:
---------------------
Every test module was written to be self contained with little or no outside dependencies.
For pure `unittest`-based examples, you may need to set your `PYTHONPATH` before running
them:

```sh
PYTHONPATH=. python tests/test_dict_verbose.py
```

For `py.test` based tests, I've included the project path onto a `conftest.py` file, so
the step described above is not required.

References
----------
- py.test:  
  http://pytest.readthedocs.org/en/latest/

- Convert `unittest` assertions to `py.test`:  
  https://gist.github.com/canassa/4fd63d682d90f5e3f07e

- `2to3` library:  
  https://docs.python.org/2/library/2to3.html