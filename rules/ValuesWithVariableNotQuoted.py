from ansiblelint import AnsibleLintRule
import re


class ValuesWithVariableNotQuoted(AnsibleLintRule):
    id = 'ROBERT3'
    shortdesc = 'Quoting values make playbooks more consistent'
    description ='Value should be quoted using double quotes'
    tags = ['formatting']

    bracket_regex = re.compile("\w:( )((?!\").)*\{")

    def match(self, file, line):
      return self.bracket_regex.search(line)
