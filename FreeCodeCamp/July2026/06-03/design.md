{
    "username": "",
    "posts": 0
}

{
    "verified": True
}

Return second object with the missing properties and don't overwrite a property if it exists

First thought is to compare the objects

1. Compare each property in the first object to each property in the second object. If it exists and matches, skip it.
2. If it doesn't exist insert it into the second object.

Questions:
When adding a new entry into dictionary it seems to append to end.

I wonder if I can insert at begining?
You can, it is a merge operator.
I'm wondering if this is better than just rebuilding the dictionary...

