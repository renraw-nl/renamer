# renamer

A CLI renamer similar to what IrfanView can do, written in python.

## References

- [Total Commander's multi-rename tool](https://www.ghisler.ch/wiki/index.php/Multi-rename_tool)
- [Entangled.py](https://github.com/entangled/entangled.py/) -- packages and basic setup
- Too simple MacOS [rename finder option](https://allthings.how/how-to-batch-rename-multiple-files-on-mac/)
- ...

## Tools

- [argh](https://argh.readthedocs.io/en/latest/)
- [rich](https://rich.readthedocs.io/en/stable/index.html)
- [pyparsing](https://github.com/pyparsing/pyparsing)
    - [diagram](https://github.com/tabatkins/railroad-diagrams/blob/gh-pages/README-py.md)
- [filelock](https://py-filelock.readthedocs.io/en/latest/index.html)
- ...

## (Planned) Use

```bash
> rename -d {N0-35}{C:01}{N40-$} *.*
> rename -d {} *.*
```

1. Clash check for new names
2. ...

### Marcos

N
:   Original name, or part of it \d+\-\d+.

C
:   Counter, with defined increments, starting number and format.
