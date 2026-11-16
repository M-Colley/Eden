"""The MochiSolver's error flags against those Genesis' solvers reserve."""

from genesis.engine.solvers.base_solver import BackwardErrorCode
from genesis.engine.solvers.rigid.data import RigidErrorCode

from eden.engine.solvers.mochi.error_codes import MochiErrorCode


def test_each_mochi_error_owns_a_bit_above_every_genesis_error():
    # `Solver.register_errors` refuses a bit the base solver already holds, EnvBase sorts the rigid and the Mochi flags
    # with one mask, and a Genesis bump may add codes above the last one: a collision reads as an unrelated error
    # raised with the wrong message.
    for code in MochiErrorCode:
        assert code.bit_count() == 1, code
    assert len({int(code) for code in MochiErrorCode}) == len(MochiErrorCode)
    assert min(MochiErrorCode) > max(max(BackwardErrorCode), max(RigidErrorCode))
