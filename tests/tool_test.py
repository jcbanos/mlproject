from mlproject.tools import haversine

def test_haversine():
  assert haversine(2.380009, 48.865070, -99.1827227, 19.3584709) == 9207.446970959321


