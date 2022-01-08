## idea of how to solve it
"""
find the start-points - add each to 1 list
Go through the list(s). For the last item, find all matches.
    ->for each unique path, create a new list and add to backlog
    ->continue on the main path, check the next match...etc.
        ->continue until we either hit the end, or a dead end (as per rules).
    ->once main path done, continue on the backlog for the other paths, they should now be unique.

    ->once now paths left in backlog, end
"""