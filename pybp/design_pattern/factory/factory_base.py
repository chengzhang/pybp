class FactoryBase(object):
    """Factory mixin

    subclasses of :py:class:`FactoryMixin` are registered by default
    """
    _subclasses: dict = {}

    def __init_subclass__(cls, *args, **kwargs):
        super().__init_subclass__(*args, **kwargs)
        cls._subclasses[cls.__name__] = cls

    @classmethod
    def create(cls, _name, *args, **kwargs):
        return cls._subclasses[_name](*args, **kwargs)