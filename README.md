# Caterpillars Movement


Have you ever noticed the movement pattern of caterpillars? Usually, they moves their mass from back to forth.

One day, I noticed that the way they move is similar to what we wrote in coding algorithms.

Let's experiment with the turtle graphic lib in Python.


<img src="https://github.com/Elstargo00/caterpillars-movement/blob/main/gif/caterpillar_movement.gif?raw=true">

```python

FRONT_POSITION = (-130,150)
MIDDLE_POSITION = (-180,150)
BACK_POSITION = (-230,150)
# segments: keeping current position of a caterpillar
# we move the last element (at BACK_POSITION) to its previous position (MIDDLE_POSITION)
# then move the second (MIDDLE_POSITION) to the first (FRONT_POSITION)
# then move the first position forward
segments = [FRONT_POSITION, MIDDLE_POSITION, BACK_POSITION]
for seg_num in range(len(segments)-1, 0, -1:
    segments[seg_num].goto(segments[seg_num - 1].xcor(), segments[seg_num -1].ycor())
segments[0].forward(45)
```

Let's see can we do it other way around? How about moving the FRONT_POSITION first.

```python
FRONT_POSITION = (-130,150)
MIDDLE_POSITION = (-180,150)
BACK_POSITION = (-230,150)
old_front_position = segments[0] # we need to define new variable to keep the value of front position before changing
segments[0].forward(45)
old_middle_position = segment[1] # again, we need to define new variable to keep the value of middle position before changing
segments[1].goto(old_front_position.xcor(), old_front_position.ycor())
segments[2].goto(old_middle_position.xcor(), old_middle_position.ycor())
# consider its inconsistency in variables (eg. old_front_position, old_middle_position). This make it hard to write for loop to scale
```

Could it be that nature is optimized?

By resisting it, things become much more complicated.
