# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401


class NullableClass(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        class properties:
            
            
            class integer_prop(
                schemas.SchemaTypeCheckerClsFactory(typing.Union[schemas.NoneClass, decimal.Decimal, ]),
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'integer_prop':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class number_prop(
                schemas.SchemaTypeCheckerClsFactory(typing.Union[schemas.NoneClass, decimal.Decimal, ]),
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'number_prop':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class boolean_prop(
                schemas.SchemaTypeCheckerClsFactory(typing.Union[schemas.NoneClass, schemas.BoolClass, ]),
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'boolean_prop':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class string_prop(
                schemas.SchemaTypeCheckerClsFactory(typing.Union[schemas.NoneClass, str, ]),
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'string_prop':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class date_prop(
                schemas.SchemaTypeCheckerClsFactory(typing.Union[schemas.NoneClass, str, ]),
                schemas.DateBase,
                schemas.NoneBase,
                schemas.Schema
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, date, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'date_prop':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class datetime_prop(
                schemas.SchemaTypeCheckerClsFactory(typing.Union[schemas.NoneClass, str, ]),
                schemas.DateTimeBase,
                schemas.NoneBase,
                schemas.Schema
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, datetime, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'datetime_prop':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class array_nullable_prop(
                schemas.SchemaTypeCheckerClsFactory(typing.Union[tuple, schemas.NoneClass, ]),
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema
            ):
            
            
                class MetaOapg:
                    items = schemas.DictSchema
            
            
                def __new__(
                    cls,
                    *args: typing.Union[tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'array_nullable_prop':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class array_and_items_nullable_prop(
                schemas.SchemaTypeCheckerClsFactory(typing.Union[tuple, schemas.NoneClass, ]),
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.SchemaTypeCheckerClsFactory(typing.Union[frozendict.frozendict, schemas.NoneClass, ]),
                        schemas.DictBase,
                        schemas.NoneBase,
                        schemas.Schema
                    ):
                    
                    
                        class MetaOapg:
                            additional_properties = schemas.AnyTypeSchema
                    
                        
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
                            *args: typing.Union[dict, frozendict.frozendict, None, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
            
                def __new__(
                    cls,
                    *args: typing.Union[tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'array_and_items_nullable_prop':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class array_items_nullable(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.SchemaTypeCheckerClsFactory(typing.Union[frozendict.frozendict, schemas.NoneClass, ]),
                        schemas.DictBase,
                        schemas.NoneBase,
                        schemas.Schema
                    ):
                    
                    
                        class MetaOapg:
                            additional_properties = schemas.AnyTypeSchema
                    
                        
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
                            *args: typing.Union[dict, frozendict.frozendict, None, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, None, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, None, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'array_items_nullable':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class object_nullable_prop(
                schemas.SchemaTypeCheckerClsFactory(typing.Union[frozendict.frozendict, schemas.NoneClass, ]),
                schemas.DictBase,
                schemas.NoneBase,
                schemas.Schema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.DictSchema
            
                
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
                    *args: typing.Union[dict, frozendict.frozendict, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, ],
                ) -> 'object_nullable_prop':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class object_and_items_nullable_prop(
                schemas.SchemaTypeCheckerClsFactory(typing.Union[frozendict.frozendict, schemas.NoneClass, ]),
                schemas.DictBase,
                schemas.NoneBase,
                schemas.Schema
            ):
            
            
                class MetaOapg:
                    
                    
                    class additional_properties(
                        schemas.SchemaTypeCheckerClsFactory(typing.Union[frozendict.frozendict, schemas.NoneClass, ]),
                        schemas.DictBase,
                        schemas.NoneBase,
                        schemas.Schema
                    ):
                    
                    
                        class MetaOapg:
                            additional_properties = schemas.AnyTypeSchema
                    
                        
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
                            *args: typing.Union[dict, frozendict.frozendict, None, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
                        ) -> 'additional_properties':
                            return super().__new__(
                                cls,
                                *args,
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
                    *args: typing.Union[dict, frozendict.frozendict, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, None, ],
                ) -> 'object_and_items_nullable_prop':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class object_items_nullable(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class additional_properties(
                        schemas.SchemaTypeCheckerClsFactory(typing.Union[frozendict.frozendict, schemas.NoneClass, ]),
                        schemas.DictBase,
                        schemas.NoneBase,
                        schemas.Schema
                    ):
                    
                    
                        class MetaOapg:
                            additional_properties = schemas.AnyTypeSchema
                    
                        
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
                            *args: typing.Union[dict, frozendict.frozendict, None, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
                        ) -> 'additional_properties':
                            return super().__new__(
                                cls,
                                *args,
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
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, None, ],
                ) -> 'object_items_nullable':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "integer_prop": integer_prop,
                "number_prop": number_prop,
                "boolean_prop": boolean_prop,
                "string_prop": string_prop,
                "date_prop": date_prop,
                "datetime_prop": datetime_prop,
                "array_nullable_prop": array_nullable_prop,
                "array_and_items_nullable_prop": array_and_items_nullable_prop,
                "array_items_nullable": array_items_nullable,
                "object_nullable_prop": object_nullable_prop,
                "object_and_items_nullable_prop": object_and_items_nullable_prop,
                "object_items_nullable": object_items_nullable,
            }
        
        
        class additional_properties(
            schemas.SchemaTypeCheckerClsFactory(typing.Union[frozendict.frozendict, schemas.NoneClass, ]),
            schemas.DictBase,
            schemas.NoneBase,
            schemas.Schema
        ):
        
        
            class MetaOapg:
                additional_properties = schemas.AnyTypeSchema
        
            
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
                *args: typing.Union[dict, frozendict.frozendict, None, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
            ) -> 'additional_properties':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
    
    integer_prop: typing.Union[MetaOapg.properties.integer_prop, schemas.Unset]
    number_prop: typing.Union[MetaOapg.properties.number_prop, schemas.Unset]
    boolean_prop: typing.Union[MetaOapg.properties.boolean_prop, schemas.Unset]
    string_prop: typing.Union[MetaOapg.properties.string_prop, schemas.Unset]
    date_prop: typing.Union[MetaOapg.properties.date_prop, schemas.Unset]
    datetime_prop: typing.Union[MetaOapg.properties.datetime_prop, schemas.Unset]
    array_nullable_prop: typing.Union[MetaOapg.properties.array_nullable_prop, schemas.Unset]
    array_and_items_nullable_prop: typing.Union[MetaOapg.properties.array_and_items_nullable_prop, schemas.Unset]
    array_items_nullable: typing.Union[MetaOapg.properties.array_items_nullable, schemas.Unset]
    object_nullable_prop: typing.Union[MetaOapg.properties.object_nullable_prop, schemas.Unset]
    object_and_items_nullable_prop: typing.Union[MetaOapg.properties.object_and_items_nullable_prop, schemas.Unset]
    object_items_nullable: typing.Union[MetaOapg.properties.object_items_nullable, schemas.Unset]
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["integer_prop"]) -> typing.Union[MetaOapg.properties.integer_prop, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["number_prop"]) -> typing.Union[MetaOapg.properties.number_prop, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["boolean_prop"]) -> typing.Union[MetaOapg.properties.boolean_prop, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["string_prop"]) -> typing.Union[MetaOapg.properties.string_prop, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["date_prop"]) -> typing.Union[MetaOapg.properties.date_prop, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["datetime_prop"]) -> typing.Union[MetaOapg.properties.datetime_prop, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["array_nullable_prop"]) -> typing.Union[MetaOapg.properties.array_nullable_prop, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["array_and_items_nullable_prop"]) -> typing.Union[MetaOapg.properties.array_and_items_nullable_prop, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["array_items_nullable"]) -> typing.Union[MetaOapg.properties.array_items_nullable, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["object_nullable_prop"]) -> typing.Union[MetaOapg.properties.object_nullable_prop, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["object_and_items_nullable_prop"]) -> typing.Union[MetaOapg.properties.object_and_items_nullable_prop, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["object_items_nullable"]) -> typing.Union[MetaOapg.properties.object_items_nullable, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[str, typing.Literal["integer_prop"], typing.Literal["number_prop"], typing.Literal["boolean_prop"], typing.Literal["string_prop"], typing.Literal["date_prop"], typing.Literal["datetime_prop"], typing.Literal["array_nullable_prop"], typing.Literal["array_and_items_nullable_prop"], typing.Literal["array_items_nullable"], typing.Literal["object_nullable_prop"], typing.Literal["object_and_items_nullable_prop"], typing.Literal["object_items_nullable"], ]):
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
        integer_prop: typing.Union[MetaOapg.properties.integer_prop, None, int, schemas.Unset] = schemas.unset,
        number_prop: typing.Union[MetaOapg.properties.number_prop, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        boolean_prop: typing.Union[MetaOapg.properties.boolean_prop, None, bool, schemas.Unset] = schemas.unset,
        string_prop: typing.Union[MetaOapg.properties.string_prop, None, str, schemas.Unset] = schemas.unset,
        date_prop: typing.Union[MetaOapg.properties.date_prop, None, date, str, schemas.Unset] = schemas.unset,
        datetime_prop: typing.Union[MetaOapg.properties.datetime_prop, None, datetime, str, schemas.Unset] = schemas.unset,
        array_nullable_prop: typing.Union[MetaOapg.properties.array_nullable_prop, tuple, None, schemas.Unset] = schemas.unset,
        array_and_items_nullable_prop: typing.Union[MetaOapg.properties.array_and_items_nullable_prop, tuple, None, schemas.Unset] = schemas.unset,
        array_items_nullable: typing.Union[MetaOapg.properties.array_items_nullable, tuple, schemas.Unset] = schemas.unset,
        object_nullable_prop: typing.Union[MetaOapg.properties.object_nullable_prop, dict, frozendict.frozendict, None, schemas.Unset] = schemas.unset,
        object_and_items_nullable_prop: typing.Union[MetaOapg.properties.object_and_items_nullable_prop, dict, frozendict.frozendict, None, schemas.Unset] = schemas.unset,
        object_items_nullable: typing.Union[MetaOapg.properties.object_items_nullable, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, None, ],
    ) -> 'NullableClass':
        return super().__new__(
            cls,
            *args,
            integer_prop=integer_prop,
            number_prop=number_prop,
            boolean_prop=boolean_prop,
            string_prop=string_prop,
            date_prop=date_prop,
            datetime_prop=datetime_prop,
            array_nullable_prop=array_nullable_prop,
            array_and_items_nullable_prop=array_and_items_nullable_prop,
            array_items_nullable=array_items_nullable,
            object_nullable_prop=object_nullable_prop,
            object_and_items_nullable_prop=object_and_items_nullable_prop,
            object_items_nullable=object_items_nullable,
            _configuration=_configuration,
            **kwargs,
        )
