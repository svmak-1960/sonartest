class Android:
    @property
    def screen(self):
        return self._screen

    @screen.setter
    def foo(self, value):
        self._screen = value

    @foo.deleter
    def foo(self):
        del self._screen
