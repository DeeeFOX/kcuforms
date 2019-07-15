
__all__ = ("BaseForm", "Form")

class BaseForm(object):
    """
    Base Form Class.  Provides core behaviour like field construction,
    validation, and data and error proxying.
    """
    pass

class FormMeta(type):
    """
    The metaclass for `Form` and any subclasses of `Form`.
    `FormMeta`'s responsibility is to create the `_unbound_fields` list, which
    is a list of `UnboundField` instances sorted by their order of
    instantiation.  The list is created at the first instantiation of the form.
    If any fields are added/removed from the form, the list is cleared to be
    re-generated on the next instantiation.
    Any properties which begin with an underscore or are not `UnboundField`
    instances are ignored by the metaclass.
    """
    pass

class Form(BaseForm, metaclass=FormMeta):
    pass


