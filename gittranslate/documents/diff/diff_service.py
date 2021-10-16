from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Callable

import git


@dataclass(init=True, repr=True, kw_only=True, frozen=True)
class DiffService:
    """
    Service to handle the recognition of diffs between files throughout commits.
    Using this service ensures that only such files' content will be passed to the ``TranslationService``
    that have actually been modified since a specific commit.
    """
    repo: git.Repo

    def modified_files(self, *,
                       since_commit: Optional[str] = None,
                       file_filter: Callable[[Path], bool] = lambda file: True) -> frozenset[Path]:
        """
        Args:
            since_commit: Specifier of the commit to be used as a point of comparison for diffing.
                          All the ``Path``'s of the files in the ``repo`` will be returned, if
                          this parameter is set to ``None`` or is not specified.
                          Expressions such as *"HEAD~1"* are also supported.
            file_filter: Predicate function that takes a ``Path`` as its parameter and returns
                         a ``bool`` value. Only those files' ``Path``s will be returned
                         that match this predicate. No filtering takes place if this argument
                         is not specified.

        Returns: A ``frozenset`` of ``Path``s of the files that have been modified since the
                 supplied ``since_commit`` or those of all the files that are in the ``repo``
                 if ``since_commit`` is not specified.
        """
        working_dir_path: str = self.repo.working_dir
        if since_commit is None:
            files = Path(working_dir_path).glob('**/*')
            # returning all the file names in the repo that are not inside the '.git' dir
            # and match the ``file_filter`` predicate
            return frozenset(file for file in files if '.git' not in file.parts and file_filter(file))

        # otherwise look at the diffs between the HEAD and the specified ``since_commit``
        diffs: list[git.Diff] = self.repo.head.commit.diff(since_commit)
        return frozenset(Path(working_dir_path, diff.a_path) for diff in diffs)
