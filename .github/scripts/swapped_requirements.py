"""Print the published requirements ``[tool.uv.sources]`` swaps for another source, space-separated (none: nothing).

A source applies to a checkout's ``uv sync`` alone, and the wheel keeps the requirement it swaps: a published wheel would
install a distribution the checkout never ran. ``release.yml`` refuses to publish while this prints anything. A source of
a development group alone (``[dependency-groups]``) never reaches the wheel and is not printed.
"""

import tomllib
from pathlib import Path

from packaging.requirements import Requirement
from packaging.utils import canonicalize_name


def swapped_requirements(pyproject: dict) -> list[str]:
    project = pyproject["project"]
    published = [
        *project.get("dependencies", ()),
        *(r for reqs in project.get("optional-dependencies", {}).values() for r in reqs),
    ]
    names = {canonicalize_name(Requirement(req).name) for req in published}
    sources = pyproject.get("tool", {}).get("uv", {}).get("sources", {})
    return sorted(name for name in sources if canonicalize_name(name) in names)


if __name__ == "__main__":
    print(" ".join(swapped_requirements(tomllib.loads(Path("pyproject.toml").read_text()))))
