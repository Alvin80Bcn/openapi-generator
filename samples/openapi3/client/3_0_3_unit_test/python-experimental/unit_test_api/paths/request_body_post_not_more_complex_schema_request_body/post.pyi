# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import re  # noqa: F401
import sys  # noqa: F401
import typing
import urllib3
import functools  # noqa: F401
from urllib3._collections import HTTPHeaderDict

from unit_test_api import api_client, exceptions
import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from unit_test_api import schemas  # noqa: F401

# body param


class SchemaForRequestBodyApplicationJson(
    schemas.ComposedSchema,
):


    class MetaOapg:
        additional_properties = schemas.AnyTypeSchema
        
        
        class not_schema(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                class properties:
                    foo = schemas.StrSchema
                    __annotations__ = {
                        "foo": foo,
                    }
                additional_properties = schemas.AnyTypeSchema
            
            foo: typing.Union[MetaOapg.properties.foo, schemas.Unset]
            
            @typing.overload
            def __getitem__(self, name: typing.Literal["foo"]) -> typing.Union[MetaOapg.properties.foo, schemas.Unset]: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
            
            def __getitem__(self, name: typing.Union[str, typing.Literal["foo"], ]):
                # dict_instance[name] accessor
                if not hasattr(self.MetaOapg, 'properties') or name not in self.MetaOapg.properties.__annotations__:
                    return super().__getitem__(name)
                try:
                    return super().__getitem__(name)
                except KeyError:
                    return schemas.unset
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                foo: typing.Union[MetaOapg.properties.foo, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
            ) -> 'not_schema':
                return super().__new__(
                    cls,
                    *args,
                    foo=foo,
                    _configuration=_configuration,
                    **kwargs,
                )

    
    def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
        # dict_instance[name] accessor
        if not hasattr(self.MetaOapg, 'properties') or name not in self.MetaOapg.properties.__annotations__:
            return super().__getitem__(name)
        try:
            return super().__getitem__(name)
        except KeyError:
            return schemas.unset

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
    ) -> 'SchemaForRequestBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
