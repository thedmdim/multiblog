import markdown
import xml.etree.ElementTree as ET
import time

start_time = time.time()

#html = '<root>'+markdown.markdown(open("posts/faras/Transfer files via SSH.md").read())+'</root>'
#title = ET.fromstring(html).find('.//h1')

title = open("posts/faras/Transfer files via SSH.md").readline()

print(title)
print("--- %s seconds ---" % (time.time() - start_time))