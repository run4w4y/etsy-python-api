import inspect
import typing
from enum import Enum


class AutoDeserialize:
    @classmethod
    def deserialize_with_enums(cls, json_object):
        init_sig = inspect.signature(cls.__init__)

        for parameter_name in init_sig.parameters:
            if parameter_name == 'self':
                continue
            
            type_annotation = init_sig.parameters[parameter_name].annotation
            
            if typing.get_origin(type_annotation) is not typing.Union:
                continue
            
            union_type = typing.get_args(type_annotation)[0]
            enum_type = None
            
            if inspect.isclass(union_type) and issubclass(union_type, Enum):
                enum_type = union_type
            elif typing.get_origin(union_type) is typing.Optional:
                inner_type = typing.get_args(union_type)[0]
                if issubclass(inner_type, Enum):
                    enum_type = inner_type
            
            if enum_type is not None and json_object.get(parameter_name) is not None:
                json_object[parameter_name] = enum_type(json_object[parameter_name]) 
        
        return cls(**json_object)
