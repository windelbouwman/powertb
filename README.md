
# powertb

Welcome to powertb, powertb gives your tracebacks superpowers!

powertb turns this:

![screenshot before](screenshot_from.png)

into this:

![screenshot before](screenshot_to.png)

# Features

Features include:

- Syntax colored context.
- List of local variables and their types.
- Api compatible with [cgitb](https://docs.python.org/3.7/library/cgitb.html)
- MIT licensed.
- Single file implementation. Drop this file into your project and use at will.

# Usage

In your script, include this:

```python
import powertb
powertb.enable()
```

# Installation

```shell
pip install powertb
```

# Alternatives

There is a long list of available traceback enhancers. This is the list, in alphabetical order:

- [backtrace](https://github.com/nir0s/backtrace) : Pretty versatile and offers options
- [colored-traceback](https://pypi.org/project/colored-traceback/) : colors tracebacks with pygments
- [ptb](https://github.com/chillaranand/ptb) : Add context variables to tracebacks

