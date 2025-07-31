from __future__ import annotations

import pytest


@pytest.fixture
def eis_simple(data_eis_5freq):
    return data_eis_5freq[0].eis_data[0]


@pytest.fixture
def eis_mux_subscan(data_eis_3ch_4scan_5freq):
    return data_eis_3ch_4scan_5freq[0].eis_data


def test_eis_data(eis_simple):
    eis = eis_simple

    assert str(eis)

    assert not eis.has_subscans
    assert eis.n_subscans == 0

    assert eis.scan_type == 'Fixed'
    assert eis.frequency_type == 'Scan'
    assert eis.n_points == 5
    assert eis.n_frequencies == 5

    assert eis.x_quantity == 'Time'
    assert eis.x_unit == 's'

    assert eis.current_range() == ['10 mA', '1 mA', '100 uA', '10 uA', '1 uA']

    dct = eis.array_dict()
    assert len(dct) == 18
    lst = eis.array_list()
    assert len(lst) == 18


def test_eis_dataset(eis_simple):
    dataset = eis_simple.dataset

    assert dataset.current_range() == ['10 mA', '1 mA', '100 uA', '10 uA', '1 uA']
    assert dataset.reading_status() == ['Underload'] * 4 + ['OK']

    assert len(dataset) == 18


def test_eis_data_mux_subscans(eis_mux_subscan):
    eis = eis_mux_subscan

    assert str(eis)

    assert not eis.has_subscans
    assert eis.n_subscans == 0

    assert eis.scan_type == 'Fixed'
    assert eis.frequency_type == 'Scan'
    assert eis.n_points == 5
    assert eis.n_frequencies == 5

    assert eis.x_quantity == 'Time'
    assert eis.x_unit == 's'

    assert eis.current_range() == ['10 mA', '1 mA', '100 uA', '10 uA', '1 uA']

    dct = eis.array_dict()
    assert len(dct) == 18
    lst = eis.array_list()
    assert len(lst) == 18


def test_test_eis_data_mux_subscans_dataset(eis_mux_subscan):
    dataset = eis_mux_subscan.dataset

    assert dataset.current_range() == ['10 mA', '1 mA', '100 uA', '10 uA', '1 uA']
    assert dataset.reading_status() == ['Underload'] * 4 + ['OK']

    assert len(dataset) == 18
