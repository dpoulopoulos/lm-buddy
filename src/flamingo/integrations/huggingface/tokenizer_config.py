from pydantic import validator

from flamingo.integrations.huggingface.utils import repo_id_validator
from flamingo.integrations.wandb import WandbArtifactConfig
from flamingo.types import BaseFlamingoConfig


class AutoTokenizerConfig(BaseFlamingoConfig):
    """Settings passed to a HuggingFace AutoTokenizer instantiation."""

    path: str | WandbArtifactConfig
    trust_remote_code: bool | None = None
    use_fast: bool | None = None

    _path_validator = validator("path", allow_reuse=True, pre=True)(repo_id_validator)
