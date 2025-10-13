from __future__ import annotations

from typing import ClassVar, Protocol, Type, runtime_checkable

import attrs
from PalmSens import Method as PSMethod
from PalmSens.Techniques import MixedMode as PSMixedMode

from pypalmsens._shared import single_to_double

from . import mixins
from ._shared import (
    CURRENT_RANGE,
)
from .base import BaseTechnique


@runtime_checkable
class StageProtocol(Protocol):
    """Protocol to provide base methods for stage classes."""

    __attrs_attrs__: ClassVar[list[attrs.Attribute]] = []

    def _update_attributes(self, psstage, /):
        for field in self.__attrs_attrs__:
            attribute = getattr(self, field.name)
            try:
                # Update parameters if attribute has the `update_params` method
                attribute._update_psmethod(psstage)
            except AttributeError:
                pass

    def _update_stage_params(self, psstage, /):
        for field in self.__attrs_attrs__:
            attribute = getattr(self, field.name)
            try:
                # Update parameters if attribute has the `update_params` method
                attribute._update_params(psstage)
            except AttributeError:
                pass


@attrs.define(slots=False)
class ConstantE(StageProtocol, mixins.CurrentLimitsMixin):
    """Amperometric detection stage."""

    _type = PSMixedMode.EnumMixedModeStageType.ConstantE

    potential: float = 0.0
    """Potential in V."""

    run_time: float = 1.0
    """Run time in s."""

    def _update_psstage(self, psstage, /):
        psstage.Potential = self.potential
        psstage.RunTime = self.run_time

        self._update_attributes(psstage)

    def _update_stage(self, psstage, /):
        self.potential = single_to_double(psstage.Potential)
        self.run_time = single_to_double(psstage.RunTime)

        self._update_stage_params(psstage)


@attrs.define(slots=False)
class ConstantI(StageProtocol, mixins.PotentialLimitsMixin):
    """Potentiometry stage."""

    _type = PSMixedMode.EnumMixedModeStageType.ConstantI

    current: float = 0.0
    """The current to apply in the given current range.

    Note that this value acts as a multiplier in the applied current range.

    So if 10 uA is the applied current range and 1.5 is given as current value,
    the applied current will be 15 uA."""

    applied_current_range: CURRENT_RANGE = CURRENT_RANGE.cr_100_uA
    """Applied current range.

    Use `CURRENT_RANGE` to define the range."""

    run_time: float = 1.0
    """Run time in s."""

    def _update_psstage(self, psstage, /):
        psstage.AppliedCurrentRange = self.applied_current_range._to_psobj()
        psstage.Current = self.current
        psstage.RunTime = self.run_time

        self._update_attributes(psstage)

    def _update_stage(self, psstage, /):
        self.applied_current_range = CURRENT_RANGE._from_psobj(psstage.AppliedCurrentRange)
        self.current = single_to_double(psstage.Current)
        self.run_time = single_to_double(psstage.RunTime)

        self._update_stage_params(psstage)


@attrs.define(slots=False)
class SweepE(StageProtocol, mixins.CurrentLimitsMixin):
    """Linear sweep detection stage."""

    _type = PSMixedMode.EnumMixedModeStageType.SweepE

    begin_potential: float = -0.5
    """Begin potential in V."""

    end_potential: float = 0.5
    """End potential in V."""

    step_potential: float = 0.1
    """Step potential in V."""

    scanrate: float = 1.0
    """Scan rate in V/s."""

    def _update_psstage(self, psstage, /):
        psstage.BeginPotential = self.begin_potential
        psstage.EndPotential = self.end_potential
        psstage.StepPotential = self.step_potential
        psstage.Scanrate = self.scanrate

        self._update_attributes(psstage)

    def _update_stage(self, psstage, /):
        self.begin_potential = single_to_double(psstage.BeginPotential)
        self.end_potential = single_to_double(psstage.EndPotential)
        self.step_potential = single_to_double(psstage.StepPotential)
        self.scanrate = single_to_double(psstage.Scanrate)

        self._update_stage_params(psstage)


@attrs.define(slots=False)
class OpenCircuit(StageProtocol, mixins.PotentialLimitsMixin):
    """Ocp stage."""

    _type = PSMixedMode.EnumMixedModeStageType.OpenCircuit

    run_time: float = 1.0
    """Run time in s."""

    def _update_psstage(self, psstage, /):
        psstage.RunTime = self.run_time

        self._update_attributes(psstage)

    def _update_stage(self, psstage, /):
        self.run_time = single_to_double(psstage.RunTime)

        self._update_stage_params(psstage)


@attrs.define(slots=False)
class Impedance(StageProtocol):
    """Electostatic impedance stage."""

    _type = PSMixedMode.EnumMixedModeStageType.Impedance

    run_time: float = 10.0
    """Run time in s."""

    dc_potential: float = 0.0
    """DC potential in V."""

    ac_potential: float = 0.01
    """AC potential in V RMS."""

    frequency: float = 50000.0
    """Frequency in Hz."""

    min_sampling_time: float = 0.5
    """Minimum sampling time in s.

    The instrument will measure at leas 2 sine waves.
    The sampling time will be automatically adjusted when necessary."""

    max_equilibration_time: float = 5.0
    """Max equilibration time in s.

    Used as a guard when the frequency drops below 1/max. equilibration time."""

    def _update_psstage(self, psstage, /):
        psstage.Potential = self.dc_potential
        psstage.Eac = self.ac_potential

        psstage.RunTime = self.run_time
        psstage.FixedFrequency = self.frequency

        psstage.SamplingTime = self.min_sampling_time
        psstage.MaxEqTime = self.max_equilibration_time

        self._update_attributes(psstage)

    def _update_stage(self, psstage, /):
        self.dc_potential = single_to_double(psstage.Potential)
        self.ac_potential = single_to_double(psstage.Eac)

        self.run_time = single_to_double(psstage.RunTime)
        self.frequency = single_to_double(psstage.FixedFrequency)

        self.min_sampling_time = single_to_double(psstage.SamplingTime)
        self.max_equilibration_time = single_to_double(psstage.MaxEqTime)

        self._update_stage_params(psstage)


TStage = ConstantE | ConstantI | SweepE | OpenCircuit | Impedance


@attrs.define
class MixedMode(
    BaseTechnique,
    mixins.CurrentRangeMixin,
    mixins.PretreatmentMixin,
    mixins.PostMeasurementMixin,
    mixins.DataProcessingMixin,
    mixins.GeneralMixin,
):
    """Create mixed mode method parameters."""

    _id = 'mm'

    interval_time: float = 0.1
    """Interval time in s."""

    cycles: int = 1
    """Number of times to go through all stages."""

    stages: list[TStage] = attrs.field(factory=list)
    """List of stages to run through."""

    def _update_psmethod(self, psmethod: PSMethod, /):
        """Update method with mixed mode settings."""
        psmethod.nCycles = self.cycles
        psmethod.IntervalTime = self.interval_time

        for stage in self.stages:
            psstage = psmethod.AddStage(stage._type)

            stage._update_psstage(psstage)

    def _update_params(self, psmethod: PSMethod, /):
        self.cycles = psmethod.nCycles
        self.interval_time = single_to_double(psmethod.IntervalTime)

        Stage: Type[StageProtocol]

        for psstage in psmethod.Stages:
            match psstage.StageType:
                case ConstantE._type:
                    Stage = ConstantE
                case ConstantI._type:
                    Stage = ConstantI
                case SweepE._type:
                    Stage = SweepE
                case OpenCircuit._type:
                    Stage = OpenCircuit
                case Impedance._type:
                    Stage = Impedance
                case _:
                    raise ValueError(f'No such stage {psstage.StageType}')

            stage = Stage()
            stage._update_stage(psstage)

            self.stages.append(stage)
