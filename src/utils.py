def format_stage_name(name: str) -> str:
    return name.strip().lower().replace(" ", "_")


def success_message(stage: str) -> str:
    return f"Stage '{stage}' executed successfully!"