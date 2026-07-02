letters = {
    'M': [
        [1,1,1,1,1],
        [1,2,1,2,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
    ],
    'O': [
        [1,1,1,1],
        [1,2,2,1],
        [1,2,2,1],
        [1,2,2,1],
        [1,1,1,1],
    ],
    'K': [
        [1,0,0,1],
        [1,0,1,0],
        [1,1,0,0],
        [1,0,1,0],
        [1,0,0,1],
    ],
    'S': [
        [1,1,1,1],
        [1,2,2,0],
        [1,1,1,1],
        [0,2,2,1],
        [1,1,1,1],
    ],
    'H': [
        [1,0,0,1],
        [1,0,0,1],
        [1,1,1,1],
        [1,0,0,1],
        [1,0,0,1],
    ],
    'A': [
        [1,1,1,1],
        [1,2,2,1],
        [1,1,1,1],
        [1,0,0,1],
        [1,0,0,1],
    ],
    'G': [
        [1,1,1,1],
        [1,2,2,0],
        [1,2,1,1],
        [1,2,2,1],
        [1,1,1,1],
    ],
    'N': [
        [1,1,0,1],
        [1,0,1,1],
        [1,0,0,1],
        [1,0,0,1],
        [1,0,0,1],
    ],
    'R': [
        [1,1,1,1],
        [1,2,2,1],
        [1,1,1,1],
        [1,0,1,0],
        [1,0,0,1],
    ],
    'E': [
        [1,1,1,1],
        [1,2,2,0],
        [1,1,1,0],
        [1,2,2,0],
        [1,1,1,1],
    ],
    'D': [
        [1,1,1,0],
        [1,2,2,1],
        [1,2,2,1],
        [1,2,2,1],
        [1,1,1,1],
    ],
    'Y': [
        [1,0,0,1],
        [1,0,0,1],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,0],
    ]
}

def render_word(word, color1, color2):
    html = '<div class="flex gap-2 sm:gap-3">'
    for char in word:
        matrix = letters[char.upper()]
        cols = len(matrix[0])
        html += f'<div class="grid gap-[1px] sm:gap-[2px]" style="grid-template-columns: repeat({cols}, minmax(0, 1fr));">'
        for row in matrix:
            for val in row:
                if val == 1:
                    bg = f'bg-[{color1}]'
                elif val == 2:
                    bg = f'bg-[{color2}]'
                else:
                    bg = 'bg-transparent'
                html += f'<div class="w-1.5 h-1.5 sm:w-2 sm:h-2 md:w-3 md:h-3 {bg}"></div>'
        html += '</div>'
    html += '</div>'
    return html

mokshagna = render_word('MOKSHAGNA', '#B7B1B1', '#4B4646')
reddy = render_word('REDDY', '#F1ECEC', '#4B4646')

logo_html = f'<div class="flex flex-col sm:flex-row gap-4 sm:gap-8 items-start sm:items-center">{mokshagna}{reddy}</div>'

with open('src/components/BlockLogo.astro', 'w') as f:
    f.write("---\n---\n" + logo_html)

