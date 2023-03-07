"""
This Python module is written by Abdurakhmon Omonov.

Most developers know that refactoring code is important from a number of perspectives like the readibility of the code
or its performance.

Remember the line from the Zen of Python.
...
Simple is better than complex.
...
So the purpose of this module is to make your code as easy as possible.
I named this module METROPOLIS as I am going to refer to the classes and methods of it as occupation names.
It would be better of you to contribute to the code if you have some spare time. But, remember not to change the existing
code if it does not have any problems and follow the ethics of programming in general.
"""
from qrcode import QRCode
import qrcode

def qrcode_maker(data: str, 
                 version: int, 
                 box_size: int, 
                 border: int, 
                 fill_color: tuple,
                 back_color: tuple, 
                 fit=True) -> QRCode:
    """
    Creates a qrcode based on the given data, for more information visit https://pypi.org/project/qrcode
    """

    maker = qrcode.QRCode(
                        version=version,
                        error_correction=qrcode.ERROR_CORRECT_M,
                        box_size=box_size,
                        border=border,
                    )
    maker.add_data(data)
    maker.make(fit=fit)
    return maker.make_image(fill_color=fill_color, back_color=back_color)
