from astropy.cloud.tests.pytest_utils import aws_s3_url


def test__load_headers__aws(aws_s3_url):
    from astropy.cloud.fits.index.aws import load_headers

    fits_headers = load_headers(aws_s3_url)
    import pdb; pdb.set_trace()
    import sys; sys.exit(1)

