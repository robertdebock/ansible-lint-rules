from ansiblelint import AnsibleLintRule
import re


class DefaultHasSpace(AnsibleLintRule):
    id = 'ROBERT1'
    shortdesc = 'Value in default should not have spaces after ( and before )'
    description ='Value should be in the form default(something)'
    tags = ['formatting']

    bracket_regex = re.compile("default |default\( |default.* \)")

    def match(self, file, line):
      return self.bracket_regex.search(line)
