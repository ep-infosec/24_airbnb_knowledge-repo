from abc import ABCMeta
import logging

logger = logging.getLogger(__name__)


class SubclassRegisteringABCMeta(ABCMeta):

    def __init__(cls, name, bases, dct):
        super(SubclassRegisteringABCMeta, cls).__init__(name, bases, dct)

        if not hasattr(cls, '_registry'):
            cls._registry = {}

        registry_keys = getattr(cls, '_registry_keys', [])
        if registry_keys:
            for key in registry_keys:
                if key in cls._registry and cls.__name__ != cls._registry[key].__name__:
                    logger.info(f"Ignoring attempt by class `{cls.__name__}` to register key '{key}', "
                                f"which is already registered for class `{cls._registry[key].__name__}`.")
                else:
                    cls._registry[key] = cls

    def _get_subclass_for(cls, key):
        return cls._registry[key]
