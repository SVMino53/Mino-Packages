from typing import Any, Literal


def __type_error_msg(scope_name : str,
                     var_name : str,
                     var_type : type,
                     expected_type : type):
    if not isinstance(scope_name, str):
        __type_error_msg(self.__name__, "scope_name", type(scope_name), str)

    if not isinstance(var_name, str):
        __type_error_msg(self.__name__, "var_name", type(var_name), str)

    if not isinstance(var_type, str):
        __type_error_msg(self.__name__, "var_type", type(var_type), str)

    if not isinstance(expected_type, str):
        __type_error_msg(self.__name__, "var_type", type(var_type), str)

    raise TypeError(f"in '{scope_name}': '{var_name}' is of type '{var_type.__name__}'; must be {expected_type.__name__}")

def __key_error_msg(scope_name : str,
                    var_name : str,
                    key_name : Any):
    raise KeyError(f"in '{scope_name}': '{key_name}' is not a key in '{var_name}'")

def __value_error_msg(scope_name : str,
                      var_name : str,
                      var_val : Any,
                      **kwargs):
    """
    Raises a ValueError message with a description on what values are allowed.

    Args:
        scope_name(str): Name of the scope, i.e. function, method or similar, where this function is called.
        var_name(str): Name of the variable assigned with the disallowed value.
        var_val(Any): Value assigned to the variable.
        **kwargs: See more bellow.
        
        in(list): List of allowed values.
        ni(list): List of disallowed values. **Compatible with:** *'lt', 'le', 'gt', 'ge'*
        eq(Any): Singular allowed value.
        ne(Any): Singular disallowed value. **Compatible with:** *'lt', 'le', 'gt', 'ge'*
        lt(float | int): Upper exclusive limit for allowed values. **Compatible with:** *'ni', 'ne', 'gt', 'ge'*
        le(float | int): Upper inclusive limit for allowed values. **Compatible with:** *'ni', 'ne', 'gt', 'ge'*
        gt(float | int): Lower inclusive limit for allowed values. **Compatible with:** *'ni', 'ne', 'lt', 'le'*
        ge(float | int): Lower inclusive limit for allowed values. **Compatible with:** *'ni', 'ne', 'lt', 'le'*
    """

    keys = kwargs.keys()
    for key in keys:
        if key not in ["in", "ni", "eq", "ne", "lt", "le", "gt", "ge"]:
            raise KeyError(f"'{key}' is an invalid key for '**kwargs'")
        
    msg = f"in '{scope_name}': '{var_name}' contains the value '{var_val}'; "
    
    if "in" in keys:
        if len(keys) != 1:
            raise 

        raise ValueError(msg + f"value must be in {kwargs["in"]}")
    
    if "eq" in keys:
        raise ValueError(msg + f"value must be '{kwargs["eq"]}'")
    
    if "ne" in keys:
        raise
    
    if "lt" in keys:
        if "gt" in keys:
            pass

        elif "ge" in keys:
            pass