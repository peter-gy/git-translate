from os import PathLike
from typing import Union, Optional

from git import Repo, RemoteProgress

from . import DiffService


class _CloneProgress(RemoteProgress):
    """
    Custom remote progress indicator to be used to display the cloning progress of a remote repo.
    """

    def update(self,
               op_code: int,
               cur_count: Union[str, float],
               max_count: Optional[Union[str, float]] = None,
               message: str = ''):
        if message:
            print(message)


class DiffServiceFactory:
    """Handles the instantiation of ``DiffService``s of different type"""

    @staticmethod
    def local_diff_service(*, local_repo_path: PathLike[str]) -> DiffService:
        """
        Args:
            local_repo_path: Path to the local git repository to be used for the diff-analysis

        Returns: A ``DiffService`` pointed to the git repository residing in the specified ``local_repo_path``.
        """
        return DiffService(repo=Repo(path=local_repo_path))

    @staticmethod
    def remote_diff_service(*,
                            remote_repo_url: str,
                            clone_dir_path: PathLike[str],
                            personal_access_token: Optional[str] = None,
                            show_clone_progress: bool = True, ) -> DiffService:
        """
        Args:
            remote_repo_url: URL to the remote git repository to be used for the diff-analysis
            clone_dir_path: Path to a local directory where the remote repo should be cloned
            personal_access_token: Personal access token issued by the Git Server that hosts the remote repository.
                                   Will be added to the ``remote_repo_url`` to handle authentication to private repos.
            show_clone_progress: Whether the cloning progress should be displayed

        Returns: A ``DiffService`` pointed to the git repository specified by ``remote_repo_url``.
        """
        url = remote_repo_url \
            if personal_access_token is None \
            else DiffServiceFactory.__construct_remote_repo_url(remote_repo_url, personal_access_token)
        return DiffService(repo=Repo.clone_from(
            url=url,
            to_path=clone_dir_path,
            progress=_CloneProgress() if show_clone_progress else None))

    @staticmethod
    def __construct_remote_repo_url(remote_repo_url: str, personal_access_token: str) -> str:
        return ''.join(['https://', personal_access_token, '@', remote_repo_url[len('https://'):]])
