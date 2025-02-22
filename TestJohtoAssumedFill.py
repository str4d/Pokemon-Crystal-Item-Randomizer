import RunCustomRandomizationAssumedFill as RunCustomRandomization
import yaml
import json

romPath = 'crystal-speedchoice-v6.0.gbc'
yamlfile = open("Modes/JohtoMode.yml")
yamltext = yamlfile.read()
settings = yaml.load(yamltext)
yamlfile = open(settings['BasePatch'])
yamltext = yamlfile.read()
patches = json.loads(yamltext)
modFileList = settings['DefaultModifiers']
modList = []
for i in modFileList:
	yamlfile = open(i)
	yamltext = yamlfile.read()
	modList.append(yaml.load(yamltext))
res = RunCustomRandomization.randomizeRom(romPath,settings['Goal'], settings['FlagsSet'],patches, banList = settings['BannedLocations'], allowList = settings['AllowedLocations'], modifiers = modList, requiredItems = settings['ProgressItems'])
print(res[2])
print(res[1])