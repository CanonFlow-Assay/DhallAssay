"""Check closed Dhall expressions without invoking import resolution."""

PREFIX = ["--plain", "--censor"]


def inspect(target):
    # The immediate-dependency branch parses and enumerates the import nodes.
    # Unlike the transitive branch, it does not load the named dependencies.
    parsed = target.call("dhall", [*PREFIX, "resolve", "--immediate-dependencies"])
    if parsed is None:
        return
    if parsed.exit_code == 1:
        if b": Invalid input" in parsed.stderr:
            target.finding("DH001")
        else:
            target.failures.append("dhall: unexpected parser rejection")
        return
    if parsed.stdout.strip():
        target.finding("DH002")
        return

    # Dhall 1.42.2 "normalize" calls assertNoImports before typeOf. It
    # independently enforces the same boundary even after the parse step.
    typed = target.call("dhall", [*PREFIX, "normalize"])
    if typed is None:
        return
    if typed.exit_code == 1:
        if b'dhall --explain' in typed.stderr:
            target.finding("DH003")
        else:
            target.failures.append("dhall: unexpected normalization rejection")
        return
    for subcommand, rule_id in (("format", "DH004"), ("lint", "DH005")):
        checked = target.call("dhall", [*PREFIX, subcommand, "--check"])
        if checked and checked.exit_code == 1:
            marker = f"dhall {subcommand} --check".encode()
            if marker in checked.stderr:
                target.finding(rule_id)
            else:
                target.failures.append(f"dhall: unexpected {subcommand} rejection")
