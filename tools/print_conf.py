import yaml

years = [2015, 2016, 2017, 2018]

with open(r'defaults.yml') as file:
  CONF = yaml.load(file, Loader=yaml.FullLoader)

try:
  with open(r'user.yml') as file:
    _CONF = yaml.load(file, Loader=yaml.FullLoader)
  CONF.update(_CONF)
except:
  pass

borderchars = [ '─', '│', '─', '│', '┌', '┐', '┘', '└']


def _topbottom_line(width=80, title=None, pos='top'):
  _ltitle = 0
  _title = ""
  if title:
    _title = f" {title} "
    _ltitle = len(_title)
  _hwidth = (width - _ltitle) // 2
  _ewidth = (width - _ltitle) % 2
  _lwidth = _hwidth-1 + _ewidth 
  _rwidth = _hwidth-1
  if pos == 'top':
    _l = borderchars[4] + _lwidth * borderchars[0]
    _r = _rwidth * borderchars[0] + borderchars[5]
  else:
    _l = borderchars[7] + _lwidth * borderchars[0]
    _r = _rwidth * borderchars[0] + borderchars[6]
  return f"{_l}{_title}{_r}"


def fill_line(text, width=80, pos='top'):
  _text = f" {str(text)} "
  _ltext = min(len(_text), width)
  _text = _text[:_ltext]
  _twidth = int(width - _ltext - 2)
  _text += _twidth * ' '
  return f"{borderchars[1]}{_text}{borderchars[3]}"

def top_line(width=80, title=None):
  ans = _topbottom_line(width, title, 'top')
  return ans

def bottom_line(width=80, title=None):
  ans = _topbottom_line(width, title, 'bottom')
  return ans


print(top_line(80))
print(fill_line('MC private production', 80))
print(bottom_line(80))

for c in ['general']:
  print(4*" ", top_line(70, f"{c.upper()}"))
  for k,v in CONF[c].items():
    print(4*" ", fill_line(f"{k:>20} : {v}", 70))
  print(4*" ",bottom_line(70))

for y in years:
  print(4*" ", top_line(70, f"{y}"))
  for k,v in CONF[y].items():
    print(4*" ", fill_line(f"{k:>20} : {v}", 70))
  print(4*" ", bottom_line(70))

print(4*" ", top_line(70, f"Statistics"))
for y in ['number_of_events', 'number_of_bunchs']:
    print(4*" ", fill_line(f"{y:>20} : {CONF[y]}", 70))
print(4*" ", bottom_line(70))

print(bottom_line(80, 'developed in Sardinia'))
