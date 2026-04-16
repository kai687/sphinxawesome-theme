---
file_format: mystnb
kernelspec:
    name: python3
---

# Jupyter notebooks

This theme should look ok with the `myst-nb` extension.

## Code with output

```{code-cell} ipython3
a = "This is "
b = "Python"
print(f"{a}{b}")
```

## Multiple outputs

```{code-cell} ipython3
for i in range(3):
    print(f"Line {i}")
```

## Expression result

```{code-cell} ipython3
import sys
sys.version
```

## Error output

```{code-cell} ipython3
:tags: [raises-exception]

1 / 0
```
