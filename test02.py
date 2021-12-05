class Android:
    @property
    def screen(self, size):
        return self._screen

    @screen.setter
    def foo(self, value, size):
        self._screen = value

    @foo.deleter
    def foo(self, size):
        del self._screen
