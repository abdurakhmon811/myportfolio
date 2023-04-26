from qrcode import QRCode
import csv
import qrcode
import re


class Translator:
    """
    The one who will take care of translations or any other stuff related to lingual topics.
    """

    def find_related_words(self, word: str, source_file_path: str) -> str:
        """
        Finds related words for the given word.

        NOTE: The first word in the file being passed should have -is_id or -is_link suffixes as this skill
        is ideally developed for a search engine for a website. For example, when a user types UNIVERSITY in the search box
        everything related to education should appear, which is what this skill for.
        :returns: A link or an id(of an HTML element) to redirect the request user to.
        """
        
        with open(source_file_path, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for row in reader:
                for phrase in row:
                    match_ = re.match(
                        word, 
                        phrase, 
                        flags=re.IGNORECASE,
                    )
                    if match_:
                        return str(row[0])


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
