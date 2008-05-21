# Tests pymanymouse using stdio
#
# Contributed by Connelly Barnes


import manymouse

def main():
  n = manymouse.init()
  event = manymouse.Event()
  while True:
    if manymouse.poll_event(event) == 0:
      continue
    if event.type == manymouse.EVENT_RELMOTION:
      print event.device, 'EVENT_RELMOTION', event.item, event.value, event.minval, event.maxval
    elif event.type == manymouse.EVENT_ABSMOTION:
      print event.device, 'EVENT_ABSMOTION', event.item, event.value, event.minval, event.maxval
    elif event.type == manymouse.EVENT_BUTTON: 
      print event.device, 'EVENT_BUTTON', event.item, event.value, event.minval, event.maxval
    elif event.type == manymouse.EVENT_SCROLL:
      print event.device, 'EVENT_SCROLL', event.item, event.value, event.minval, event.maxval
    elif event.type == manymouse.EVENT_DISCONNECT:
      print event.device, 'EVENT_DISCONNECT', event.item, event.value, event.minval, event.maxval

if __name__ == '__main__':
  main()
