tpl = '<rect x="{x}" y="{y}" width="{s}" height="{s}" style="fill:{color}"/>'
colors = ['red', 'black']
s = 50

with open('images/chessboard.svg', 'w') as f:
    print >>f, '<?xml version="1.0"?>\n<svg width="{s}" height="{s}" viewBox="0 0 {s} {s}" xmlns="http://www.w3.org/2000/svg">'.format(s=s*8)
    for i in range(8):
        for j in range(8):
            print >>f, tpl.format(x=i*s,y=j*s,s=s,color=colors[(i+j)%2])
    print >>f, '</svg>'

with open('images/chessboard-missing.svg', 'w') as f:
    print >>f, '<?xml version="1.0"?>\n<svg width="{s}" height="{s}" viewBox="0 0 {s} {s}" xmlns="http://www.w3.org/2000/svg">'.format(s=s*8)
    for i in range(8):
        for j in range(8):
            if i == 7 and j == 0 or i == 0 and j == 7: continue
            print >>f, tpl.format(x=i*s,y=j*s,s=s,color=colors[(i+j)%2])
    print >>f, '</svg>'

with open('images/chessboard-domino.svg', 'w') as f:
    print >>f, '<?xml version="1.0"?>\n<svg width="{s}" height="{s}" viewBox="0 0 {s} {s}" xmlns="http://www.w3.org/2000/svg">'.format(s=s*8)
    for i in range(8):
        for j in range(8):
            print >>f, tpl.format(x=i*s,y=j*s,s=s,color=colors[(i+j)%2])

    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                print >>f, '<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" ry="5" style="fill:white"/>'.format(
                        x = i * s + s / 3.,
                        y = j * s + s / 6.,
                        w = 4./3 * s,
                        h = 2./3 * s)
    print >>f, '</svg>'
