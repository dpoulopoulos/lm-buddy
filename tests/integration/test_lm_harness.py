import wandb

from lm_buddy import LMBuddy
from lm_buddy.integrations.huggingface import AutoModelConfig
from lm_buddy.integrations.wandb import WandbRunConfig
from lm_buddy.jobs.configs import LMHarnessEvaluationConfig, LMHarnessJobConfig
from lm_buddy.paths import format_artifact_path
from tests.utils import FakeArtifactLoader


def get_job_config(model_artifact: wandb.Artifact) -> LMHarnessJobConfig:
    """Create a job config for evaluation.

    The artifact should already be logged and contain a fully qualified W&B name.
    """
    model_config = AutoModelConfig(path=format_artifact_path(model_artifact))
    tracking_config = WandbRunConfig(name="test-lm-harness-job")
    evaluation_config = LMHarnessEvaluationConfig(tasks=["hellaswag"], limit=5)
    return LMHarnessJobConfig(
        model=model_config,
        evaluation=evaluation_config,
        tracking=tracking_config,
    )


def test_lm_harness_job_with_tracking(llm_model_artifact):
    # Preload input artifact in loader
    artifact_loader = FakeArtifactLoader()
    logged_model_artifact = artifact_loader.log_artifact(llm_model_artifact)

    # Get a job config
    job_config = get_job_config(logged_model_artifact)

    # Run test job
    buddy = LMBuddy(artifact_loader)
    buddy.evaluate(job_config)

    # One input artifact, and one eval artifact produced
    assert artifact_loader.num_artifacts() == 2


def test_lm_harness_job_no_tracking(llm_model_artifact):
    # Preload input artifact in loader
    artifact_loader = FakeArtifactLoader()
    llm_model_artifact = artifact_loader.log_artifact(llm_model_artifact)

    # Get a job config
    job_config = get_job_config(llm_model_artifact)
    job_config.tracking = None  # Disable tracking on job config

    # Run test job
    buddy = LMBuddy(artifact_loader)
    buddy.evaluate(job_config)

    # One input artifact, no additional eval artifacts produced
    assert artifact_loader.num_artifacts() == 1
