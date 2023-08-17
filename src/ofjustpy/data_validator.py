"""
Derived from wtforms
"""
import email_validator
from py_tailwind_utils.dpathutils import dget
from py_tailwind_utils.dpathutils import dsearch
from wtforms.validators import StopValidation
from wtforms.validators import ValidationError


def validate(validation_chain, data, stubStore):
    stop_validation = False
    errors = []
    # something about pre_validate

    if not stop_validation:
        for validator in validation_chain:
            try:
                validator(data, stubStore)
            except StopValidation as e:
                stop_validation = True
                if e.args and e.args[0]:
                    errors.append(e.args[0])
                break
            except ValidationError as e:
                errors.append(e.args[0])

    if errors:
        print("error occured ", errors)
    return len(errors) == 0


def InputRequired():
    def validator(raw_data, stubStore):
        """ """
        if raw_data and raw_data[0]:
            return
        raise StopValidation("Input field required")

    return validator


def EqualTo(other_spath):
    def validator(data, stubStore):
        if not dsearch(stubStore, other_spath):
            raise ValidationError(f"Invalid field name '{other_spath}'")
        other_value = dget(stubStore, other_spath).get_value()
        if other_value == data:
            return
        raise ValidationError(f"Field must be equal to %(other_spath)s.")

    return validator


def Email(
    granular_message=False,
    check_deliverability=True,
    allow_smtputf8=True,
    allow_empty_local=False,
):
    def validator(data, stubStore):
        try:
            if data is None:
                raise email_validator.EmailNotValidError()
            email_validator.validate_email(
                data,
                check_deliverability=check_deliverability,
                allow_smtputf8=allow_smtputf8,
                allow_empty_local=allow_empty_local,
            )
        except email_validator.EmailNotValidError as e:
            message = "Invalid email address"
            raise ValidationError(message) from e

    return validator


def Length(min=-1, max=-1):
    """
    Validates the length of a string.

    :param min:
        The minimum required length of the string. If not provided, minimum
        length will not be checked.
    :param max:
        The maximum length of the string. If not provided, maximum length
        will not be checked.
    :param message:
        Error message to raise in case of a validation error. Can be
        interpolated using `%(min)d` and `%(max)d` if desired. Useful defaults
        are provided depending on the existence of min and max.

    When supported, sets the `minlength` and `maxlength` attributes on widgets.
    """

    assert min != -1 or max != -1, "At least one of `min` or `max` must be specified."
    assert max == -1 or min <= max, "`min` cannot be more than `max`."
    # self.field_flags = {}
    # if self.min != -1:
    #     self.field_flags["minlength"] = self.min
    # if self.max != -1:
    #     self.field_flags["maxlength"] = self.max

    def validator(data, stubStore):
        length = data and len(data) or 0
        if length >= min and (max == -1 or length <= max):
            return

        raise ValidationError("input does not meet the length requirements")

    return validator
