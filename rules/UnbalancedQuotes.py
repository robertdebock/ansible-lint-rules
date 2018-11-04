from ansiblelint import AnsibleLintRule

class UnbalancedQuotes(AnsibleLintRule):
    id = 'ROBERT4'
    shortdesc = 'Unbalanced quote'
    description = 'Quotes should be balanced, always two on a line'
    tags = ['formatting']

    def match(self, file, line):
        return line.count("(") != line.count(")") or line.count('"') % 2 != 0
