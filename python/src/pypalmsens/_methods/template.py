from __future__ import annotations

from string import Formatter
from typing import Any

from pydantic import BaseModel

from .techniques import MethodScript


class MethodScriptTemplate(BaseModel):
    template: str
    model: type[BaseModel] | None = None

    def substitute(self, **kwargs) -> MethodScript:
        """Substitute variables in template."""
        if self.model:
            variables = self.model(**kwargs).model_dump()
        else:
            self.validate_against_template(kwargs)
            variables = kwargs

        s = self.template.format(**variables)
        return MethodScript(script=s)

    def validate_against_template(self, mapping: dict[str, Any]):
        if (keywords := set(mapping)) != (variables := self.template_variables()):
            raise ValueError(
                (
                    'Keyword arguments do not match template variables.'
                    f'Difference: {keywords ^ variables}. '
                )
            )

    def template_variables(self) -> set[str]:
        """Get variables defined in template."""
        variables = []

        # Skip last field which is always empty
        fields = list(Formatter().parse(self.template))[:-1]

        for field in fields:
            name = field[1]
            if not name:
                raise ValueError('Template contains variable name.')
            variables.append(name)

        return set(variables)
