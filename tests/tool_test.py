from mlproject.tools import haversine

def test_haversine():
  assert haversine(48.865070, 2.380009, 19.3584709, -99.1827227) == 11159.056396758873


