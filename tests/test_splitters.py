import pandas as pd
import numpy as np
import pytest
from evidense_x.splitters.group_split import DuplicateAwareGroupSplitter
from evidense_x.splitters.leakage_split import ControlledLeakageInjector

def test_group_splitter_class():
    df = pd.DataFrame({
        'f1': [1, 1, 2, 3, 4, 5, 6, 7],
        'target': [1, 1, 0, 0, 1, 0, 1, 0]
    })
    tr_idx, te_idx = DuplicateAwareGroupSplitter.split(df, ['f1'], 'target', test_size=0.25)
    assert len(set(tr_idx).intersection(set(te_idx))) == 0

def test_leakage_injector():
    train = pd.DataFrame({'f1': [1, 2, 3], 'target': [0, 1, 0]})
    test = pd.DataFrame({'f1': [4, 5, 6, 7], 'target': [1, 0, 1, 0]})
    leaked = ControlledLeakageInjector.inject(train, test, overlap_rate=0.5)
    assert len(leaked) == len(train) + 2
