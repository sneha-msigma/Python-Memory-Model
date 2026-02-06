## Python Memory Model ##


Overview
`memcourt` is a lightweight diagnostic tool designed to prove how Python handles object references in memory. 
## Key Features
* **Heap Snapshotting:** Capture the state of variables and their unique memory IDs.
* **CLI Interface:** Run memory experiments directly from the terminal.
* **JSON Support:** Export memory data for machine-readable analysis or external visualization.
* **Educational Examples:** Built-in demonstrations of common Python memory pitfalls.



This project implements a minimal Heap Snapshot Engine and CLI in Python to
demonstrate and prove two core Python memory model concepts:

1. Aliasing
2. Nested Mutability

By capturing "snapshots" of variable memory addresses (`id()`), it provides visual and data-driven proof of how multiple variables can point to the same object (aliasing) and how shallow copies affect nested structures (nested mutability).


The system captures before-and-after heap snapshots, compares them, and reports
evidence using object identity (id()) and value changes.

The implementation is intentionally simple and beginner-friendly while remaining
technically correct and aligned with the task PDF.

--------------------------------------------------

## PROBLEM STATEMENT
In Python, variables do not store values directly. They store references to
objects in memory. This leads to behaviors such as:

- Multiple variable names referring to the same object (aliasing)
- Mutations inside nested mutable objects affecting outer immutable containers

The objective of this project is to:
- Capture heap state at specific moments
- Compare states across time
- Provide clear evidence of aliasing and nested mutability

--------------------------------------------------

## CONCEPTS DEMONSTRATED

# ALIASING
Aliasing occurs when multiple variables refer to the same object in memory.

Example:
a = [1, 2]
b = a

Both a and b point to the same list object. A mutation through one name affects
the other.

Evidence:
- Same object id()
- Mutation visible through all aliases

# NESTED MUTABILITY
Nested mutability occurs when a mutable object exists inside an immutable one.

Example:
t = ([1, 2], [3, 4])
inner = t[0]
inner.append(99)

- The tuple t is immutable
- The list inside it is mutable
- Mutating the inner list changes the observable state of t

Evidence:
- Outer object identity unchanged
- Inner object value changed

--------------------------------------------------

## PROJECT STRUCTURE

Python-Memory-Model/
|
|-- main.py
|-- examples.py
|
|-- memcourt/
    |-- __init__.py
    |-- snapshot.py
    |-- diff.py
    |-- cli.py

--------------------------------------------------


Control Flow:
main.py loads examples.py
main.py takes Snapshot A (before mutation)
main.py triggers mutation
main.py takes Snapshot B (after mutation)
diff.py compares snapshots
cli.py displays evidence

--------------------------------------------------

## MODULE RESPONSIBILITIES

snapshot.py
- Defines the Snapshot class
- Captures heap state at a specific moment
- Records variable name, object id, and value

diff.py
- Compares two snapshots
- Detects aliasing and mutations

cli.py
- Displays snapshots and diff results
- Supports human-readable and JSON output

examples.py
- Creates controlled test cases
- Demonstrates aliasing and nested mutability
- Provides mutation functions to enforce correct snapshot timing

main.py
- CLI entry point
- Controls snapshot timeline:
  1. Snapshot before mutation
  2. Perform mutation
  3. Snapshot after mutation
  4. Diff and report results

--------------------------------------------------

## SNAPSHOT DESIGN

A snapshot is a passive representation of heap state at a moment in time.
It does not perform analysis.

Each snapshot entry contains:
- Variable name
- Object identity (id)
- String representation of value

--------------------------------------------------

## DIFF DESIGN

Diffing is a separate analytical step that compares two snapshots to detect:

- Aliasing (same object id across variables)
- Mutations (value change between snapshots)

This separation follows the single-responsibility principle and mirrors the
conceptual pipeline described in the task PDF.

--------------------------------------------------

## CLI USAGE

Activate the Conda environment:
conda activate memory

Run analysis:
python main.py analyze examples.py

JSON output:
python main.py analyze examples.py --json

--------------------------------------------------

## OUTPUT INTERPRETATION

- Aliasing detected: multiple variable names share the same object id
- Mutation detected: value differs between snapshots
- Nested mutability: inner object mutated while outer identity remains stable

--------------------------------------------------

DESIGN RATIONALE

- Snapshot creation, diffing, and presentation are separated for clarity
- Mutation is enforced strictly between snapshots
- Script loading is file-based to support arbitrary input scripts

This design aligns with the intent and conceptual model of the task PDF.

--------------------------------------------------

KEY TAKEAWAYS

- Python variables store references, not values
- Object identity and value are distinct concepts
- Timing matters when observing memory behavior
- Clear separation of concerns simplifies reasoning

--------------------------------------------------


CONCLUSION

This project provides a minimal yet accurate demonstration of Python’s memory
model using heap snapshots and diffs. It serves as both a learning tool and a
foundation for more advanced memory analysis features.


