from __future__ import annotations

from string import Formatter

from pydantic import BaseModel

from .techniques import MethodScript


class MethodScriptTemplate(BaseModel):
    template: str

    def substitute(self, **kwargs) -> MethodScript:
        """Substitute variables in template."""
        if (keywords := set(kwargs)) != (variables := self.variables()):
            raise ValueError(
                (
                    'Keyword arguments do not match template variables.'
                    f'Difference: {keywords ^ variables}. '
                )
            )

        s = self.template.format(**kwargs)
        return MethodScript(script=s)

    def variables(self) -> set[str]:
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
