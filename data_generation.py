import re


def data_generate(file):
	data = []
	with open(file) as f:
		for line in f:
			m = re.match(r'(?P<YR>\d+)\s+(?P<MO>\d+)\s+(?P<PREDICTED>[\.\d]+)\s+(?P<HIGH>[\.\d]+)\s+(?P<LOW>[\.\d]+)', line)
			if m: data.append((int(m.group('YR')), int(m.group('MO')), float(m.group('PREDICTED')), float(m.group('HIGH')), float(m.group('LOW'))))
	return data
