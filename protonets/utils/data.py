from ..data import omniglot

def load(opt, splits):
    if opt['data.dataset'] == 'omniglot':
        ds = omniglot.load(opt, splits)
    else:
        raise ValueError("Unknown dataset: {:s}".format(opt['data.dataset']))

    return ds
