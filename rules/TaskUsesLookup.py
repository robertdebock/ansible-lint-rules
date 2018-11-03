from ansiblelint import AnsibleLintRule
import re

class TaskUsesLookup(AnsibleLintRule):
    id = 'ROBERT2'
    shortdesc = 'Variable lookup should not happen tasks/main.yml'
    description = 'Values can not contain parameter: variable[identifier]'
    tags = ['formatting']

    bracket_regex = re.compile("{{.*\[.*\].*}}")

    def match(self, file, line):
      return self.bracket_regex.search(line)
