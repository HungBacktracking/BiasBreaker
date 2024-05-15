from IPython.display import display
from IPython.display import Markdown
import textwrap
import pathlib

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))