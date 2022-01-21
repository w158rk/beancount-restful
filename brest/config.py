from typing import NamedTuple
import hipack

_Config = NamedTuple('_Config', [
    ('beanfile', str)
])

class Config(_Config):

    @classmethod
    def load(cls, file):
        obj = hipack.load(file)
        return cls.load_obj(obj)

    @classmethod
    def load_obj(cls, obj):
        return cls(**obj)
