# incident-severity-scorer

Turn impact and urgency scores (1-5 each) into a P1-P4 incident priority using a fixed matrix.

## How to run

```sh
python3 main.py --impact 4 --urgency 5
```

## Example output

```
Impact 4 + Urgency 5 = 9 -> P1
```

Standard library only. Run the tests with `python3 -m unittest discover`.
