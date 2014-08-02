
class BaseColor:
    attr = 0      # attribute code. default 0 resets attributes
    fgrd = 256    # foreground (text) color. default 256 for white
    bgrd = 0      # background color. default 0 for black

    def __init__(self, body=''):
        self.body = body

    def __repr__(self):
        return '\033[{attr};{bgrd};{fgrd}m{body}\033[0m'.format(
                attr=self.attr, bgrd=self.bgrd, fgrd=self.fgrd, body=self.body
            )

    def __str__(self):
        return '\033[{attr};{bgrd};{fgrd}m{body}\033[0m'.format(
                attr=self.attr, bgrd=self.bgrd, fgrd=self.fgrd, body=self.body
            )
