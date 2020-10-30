import functools
from .data_set import DataSet

@functools.lru_cache(maxsize=None)
def data_sets() -> [DataSet]:
    """Returns all available data_sets."""
    from .example import example_data_sets
    return example_data_sets()

@functools.lru_cache(maxsize=None)
def aggregate_tables() -> [DataSet]:
    """Returns all data_sets which needs aggregate tables."""
    from .example import example_data_sets
    return example_data_sets()