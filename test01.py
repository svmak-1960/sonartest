class A:
    @property
    def foo(self):
        return self._foo

    @foo.setter
    def foo(self, value):
        self._foo = value

    @foo.deleter
    def foo(self):
        del self._foo

class B:
    def get_foo(self):
        return self._foo

    def set_foo(self, value):
        self._foo = value

    def del_foo(self):
        del self._foo

    foo = property(get_foo, set_foo, del_foo, "'foo' property.")
