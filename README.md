# Sortify
---
Sortify is an open-source sorting tool for Windows users. Define your own rules, make it work as you want.

## How to make it sort other files?

Sortify comes with a ready-made json file that can handle the usual range of tasks for an average user. 
It is easy to make sortify recognize and sort other types of data.  Simply add a new folder type to the schema of the json file, following the usual partitioning rules. Suppose to add support for sorting Blender files, add the following lines to the json schema:

```json
"Blender":['blend']
```
