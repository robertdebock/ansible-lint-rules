lint-rules
==========

A few extra lint rules to keep coding style consistent.

DefaultHasSpace
---------------

ROBERT1: To keep code consistent and mostly readable.

Correct:
```
- name: do something
  package:
    name: "{{ variable | default(omit) }}"
```

Incorrect: (Spaces after and before both ( and ).
```
- name: do something
  package:
    name: "{{ variable | default ( omit ) }}"
```

TaskUsesLookup
--------------

ROBERT2: To make sure playbooks are simple to read.

Correct:
```
- name: do something:
  package:
    name: "{{ packages }}"
```

Incorrect:
```
- name: do something:
  package:
    name: "{{ packages[ansible_distribution }}"
```
