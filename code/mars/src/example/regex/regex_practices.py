import re

class RegexPractice:
  def match(self, pattern, string):
    return re.match(pattern, string)

  def search(self, pattern, string):
    return re.search(pattern, string)

  def find_all(self, pattern, string):
    return re.findall(pattern, string)

  def split(self, pattern, string):
    return re.split(pattern, string)  # matches one or more digits
