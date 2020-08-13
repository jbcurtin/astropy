import pytest

@pytest.fixture
def aws_s3_url():
    return 'https://s3.us-east-1.amazonaws.com/stpubdata/tess/public/mast/tess-s0022-4-4-cube.fits'
