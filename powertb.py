""" powertb: tracebacks with superpowers

Usage:

    import powertb
    powertb.enable()

This will register an exception handler for uncaught exceptions
and print a full color detailed traceback.

"""

import sys
import traceback
import inspect

import pygments
import pygments.lexers
import pygments.formatters


def enable():
    """ Register a callback for unhandled exceptions.
    """
    sys.excepthook = handle_exception


def handle_exception(exc_type, exc_value, exc_tb):
    """ Handle an exception. """
    formatter = pygments.formatters.Terminal256Formatter(style='monokai')

    # print traceback:
    tb_text = ''.join(traceback.format_exception(exc_type, exc_value, exc_tb))
    lexer = pygments.lexers.get_lexer_by_name('pytb')
    colored = pygments.highlight(tb_text, lexer, formatter)
    print(colored)

    # Print detailed frames:
    lexer = pygments.lexers.python.Python3Lexer(ensurenl=False)
    context_size = 5
    frames = inspect.getinnerframes(exc_tb, context=context_size)
    for frame in frames:
        # Some context:
        print('File:', frame.filename)
        num_line_chars = len(str((frame.lineno + context_size)))
        for index, line in enumerate(frame.code_context):
            line_nr = frame.lineno + index - frame.index
            line_nr = '{0:{1}}'.format(line_nr, num_line_chars)
            line = pygments.highlight(line, lexer, formatter)
            marker = '-> ' if index == frame.index else '   '
            print(marker, line_nr, ':', line)

        # Local variables:
        values = inspect.getargvalues(frame.frame)
        print('Variables:')
        for name, value in sorted(values.locals.items()):
            print('    ', name, '=', value, ' #', type(value))
        print()
