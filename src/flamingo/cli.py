import click

from flamingo.jobs import FinetuningJobConfig, LMHarnessJobConfig, SimpleJobConfig


@click.group()
def main():
    pass


@main.group(name="run")
def run():
    pass


@run.command("simple")
@click.option("--config", type=str)
def run_simple(config: str) -> None:
    from flamingo.jobs.drivers import run_simple

    config = SimpleJobConfig.from_yaml_file(config)
    run_simple(config)


@run.command("finetuning")
@click.option("--config", type=str)
def run_finetuning(config: str) -> None:
    from flamingo.jobs.drivers import run_finetuning

    config = FinetuningJobConfig.from_yaml_file(config)
    run_finetuning(config)


@run.command("ludwig")
@click.option("--config", type=str)
@click.option("--dataset", type=str)
def run_ludwig(config: str, dataset: str) -> None:
    from flamingo.jobs.drivers import run_ludwig

    run_ludwig(config, dataset)


@run.command("lm-harness")
@click.option("--config", type=str)
def run_lm_harness(config: str) -> None:
    from flamingo.jobs.drivers import run_lm_harness

    config = LMHarnessJobConfig.from_yaml_file(config)
    run_lm_harness(config)


if __name__ == "__main__":
    main()
