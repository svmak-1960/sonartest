class A:
    @property
    def foo(self, unexpected, unexpected2):  # Noncompliant. Too many parameters.
        return self._foo

    @foo.setter
    def foo(self, value, unexpected):  # Noncompliant. Too many parameters.
        self._foo = value

    @foo.deleter
    def foo(self, unexpected):  # Noncompliant. Too many parameters.
        del self._foo

class B:
    def get_foo(self, unexpected):  # Noncompliant. Too many parameters.
        return self._foo

    def set_foo(self, value, unexpected):  # Noncompliant. Too many parameters.
        self._foo = value

    def del_foo(self, unexpected):  # Noncompliant. Too many parameters.
        del self._foo

    foo = property(get_foo, set_foo, del_foo, "'foo' property.")
