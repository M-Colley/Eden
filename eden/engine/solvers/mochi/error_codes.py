"""Error flags the MochiSolver's kernels raise in the per-environment ``errno`` field of its kinematic tree."""

from enum import IntEnum


class MochiErrorCode(IntEnum):
    """Bits above every one of Genesis' ``BackwardErrorCode`` and ``RigidErrorCode``, so the two never collide.

    The MochiSolver flags its own ``errno``, apart from the RigidSolver's, but ``EnvBase`` sorts the flags of both with
    one mask (``eden.envs.base._RECOVERABLE_SOLVER_ERRORS``), and ``Solver.register_errors`` refuses a bit the base
    solver reserves (``BackwardErrorCode.INVALID_GRAD_NAN``). A Genesis bump that adds a code above these must move them
    above it; ``tests/engine/solvers/mochi/test_error_codes.py`` pins it.
    """

    OVERFLOW_MOCHI_CONTACT_PAIRS = 0b00000000000000000000010000000000
    OVERFLOW_MOCHI_CONTACTS = 0b00000000000000000000100000000000
    MOCHI_DIVERGED = 0b00000000000000000001000000000000
