from __future__ import annotations

from typing import ClassVar, Protocol, Sequence, runtime_checkable

import attrs
from PalmSens.Techniques import MixedMode as PSMixedMode

from .techniques import (
    CurrentLimitsMixin,
    CurrentRangeMixin,
    DataProcessingMixin,
    GeneralMixin,
    MethodSettings,
    PostMeasurementMixin,
    PretreatmentMixin,
)


@runtime_checkable
class StageProtocol(Protocol):
    """Protocol to provide base methods for stage classes."""

    __attrs_attrs__: ClassVar[list[attrs.Attribute]] = []


@attrs.define(slots=False)
class StageConstantE(StageProtocol, CurrentLimitsMixin):
    """Amperometric detection stage."""

    _type = PSMixedMode.EnumMixedModeStageType.ConstantE

    potential: float = 0.0
    """Potential in V."""

    run_time: float = 1.0
    """Run time in s."""

    def _update_psobj(self, *, obj):
        obj.Potential = self.potential
        obj.RunTime = self.run_time

        for field in self.__attrs_attrs__:
            attribute = getattr(self, field.name)
            try:
                # Update parameters if attribute has the `update_params` method
                attribute._update_psmethod(obj=obj)
            except AttributeError:
                pass

    def _update_params(self, *, obj):
        self.potential = obj.Potential
        self.run_time = obj.RunTime

        for field in self.__attrs_attrs__:
            attribute = getattr(self, field.name)
            try:
                # Update parameters if attribute has the `update_params` method
                attribute._update_params(obj=obj)
            except AttributeError:
                pass


class StageConstantI:
    """Potentiometry stage."""

    _type = PSMixedMode.EnumMixedModeStageType.ConstantI


class StageSweepE:
    """Linear sweep detection stage."""

    _type = PSMixedMode.EnumMixedModeStageType.SweepE


class StageOpenCircuit:
    """Ocp stage."""

    _type = PSMixedMode.EnumMixedModeStageType.OpenCircuit


class StageImpedance:
    """Electostatic impedance stage."""

    _type = PSMixedMode.EnumMixedModeStageType.Impedance


TStage = StageConstantE
# | StageConstantI | StageSweepE | StageOcp | StageEIS


@attrs.define
class MixedMode(
    MethodSettings,
    CurrentRangeMixin,
    PretreatmentMixin,
    PostMeasurementMixin,
    DataProcessingMixin,
    GeneralMixin,
):
    """Create mixed mode method parameters."""

    _id = 'mm'

    interval_time: float = 0.1
    """Interval time in s."""

    cycles: int = 1
    """Number of times to go through all stages."""

    stages: Sequence[TStage] = attrs.field(factory=list)
    """List of stages to run through."""

    def _update_psmethod(self, *, obj):
        """Update method with mixed mode settings."""
        obj.nCycles = self.cycles
        obj.IntervalTime = self.interval_time

        for stage in self.stages:
            psstage = obj.AddStage(stage._type)

            stage._update_psobj(obj=psstage)

    def _update_params(self, *, obj):
        self.cycles = obj.nCycles
        self.interval_time = obj.IntervalTime

        for psstage in obj.Stages:
            match psstage.StageType:
                case StageConstantE._type:
                    Stage = StageConstantE
                # case StageConstantI._type:
                #     Stage = StageConstantI
                # case StageSweepE._type:
                #     Stage = StageSweepE
                # case StageOpenCircuit._type:
                #     Stage = StageOpenCircuit
                # case StageImpedance._type:
                #     Stage = StageImpedance
                case _:
                    raise ValueError(f'No such stage {psstage.StageType}')

            stage = Stage()
            stage._update_params(obj=obj)
