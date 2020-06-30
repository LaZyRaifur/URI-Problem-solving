sec = int(input())

min = int(sec / 60)
sec -= min * 60
hours = int(min / 60)
min -= hours * 60
print(repr(hours) + ":" + repr(min) + ":" + repr(sec))
