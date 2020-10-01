import matplotlib.pyplot as plt
from io import StringIO

def latex2img(formula, fontsize=12, dpi=300, format_='svg'):
    """Renders LaTeX formula into image.
    """
    fig = plt.figure(figsize=(0.01, 0.01))
#     fig.text(0, 0, u'${}$'.format(formula), fontsize=fontsize)
    fig.text(0, 0, formula, fontsize=fontsize,style='italic')
    buffer_ = StringIO()
    fig.savefig(buffer_, dpi=dpi, transparent=False, format=format_, bbox_inches='tight', pad_inches=0.1)
    plt.close(fig)
    return buffer_.getvalue()