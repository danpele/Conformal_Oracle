"""Conformal recalibration audit for tail quantile forecasters."""

from conformal_oracle._protocols import Forecaster
from conformal_oracle._types import (
    ParametricDistribution,
    PredictiveDistribution,
    QuantileGridDistribution,
    SampleDistribution,
)
from conformal_oracle.audit import (
    audit,
    audit_rolling,
    audit_static,
    audit_with_benchmarks,
)
from conformal_oracle.classify import RegimeVerdict, classify_regime
from conformal_oracle.compare import ComparisonResult, compare_forecasters
from conformal_oracle.panel import audit_panel
from conformal_oracle.recalibration import (
    AdaptiveConformalInference,
    ConformalShift,
    ExtremeValueTheoryPOT,
    FilteredHistoricalSimulation,
    GBMQuantileRegression,
    HistoricalQuantileRecalibration,
    IsotonicQuantileRegression,
    LinearQuantileRegression,
    RecalibrationMethod,
    ScaleCorrectionRecalibration,
)

__version__ = "0.3.0"

__all__ = [
    # Core types
    "SampleDistribution",
    "QuantileGridDistribution",
    "ParametricDistribution",
    "PredictiveDistribution",
    "Forecaster",
    # Main entry points
    "audit",
    "classify_regime",
    "compare_forecasters",
    # Result types
    "RegimeVerdict",
    "ComparisonResult",
    # Deprecated (still importable, emit warnings on call)
    "audit_static",
    "audit_rolling",
    "audit_with_benchmarks",
    "audit_panel",
    # Recalibration
    "RecalibrationMethod",
    "ConformalShift",
    "HistoricalQuantileRecalibration",
    "ScaleCorrectionRecalibration",
    "LinearQuantileRegression",
    "IsotonicQuantileRegression",
    "AdaptiveConformalInference",
    "GBMQuantileRegression",
    "ExtremeValueTheoryPOT",
    "FilteredHistoricalSimulation",
]
