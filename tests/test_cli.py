from studious.cli import build_parser


def test_default_name() -> None:
    args = build_parser().parse_args([])
    assert args.name == "world"
