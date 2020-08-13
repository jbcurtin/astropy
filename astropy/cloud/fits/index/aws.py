import requests
import typing

from astropy.io import fits
from astropy.cloud.fits.auth.aws import AWSAuth
from astropy.cloud.fits.constants import END_CARD, BLOCK_SIZE, ENCODING
from astropy.cloud.fits.utils import FITSHeader, find_next_header_offset
from astropy.cloud.fits.datatypes import FITSHeader

def load_headers(url: str, request_payer: bool = False) -> typing.List[FITSHeader]:
    offset: int = 0
    headers: typing.List[FITSHeader] = []
    read_blocks: typing.List[str] = []
    header_data = []
    while True:
        response = requests.get(url, headers={
            'Range': f'bytes={offset}-{offset + BLOCK_SIZE - 1}',
        }, auth=AWSAuth(request_payer=True))
        if response.status_code in [206]:
            try:
                header_data.append(response.content.decode(ENCODING))
            except UnicodeDecodeError:
                raise Exception("If this happens, it means the FITS file is invalid or the calculation is off")

            else:
                if END_CARD in header_data[-1]:
                    fits_header = fits.Header.fromstring(''.join(header_data))
                    header = FITSHeader(offset, offset + BLOCK_SIZE, fits_header)
                    headers.append(header)
                    header_data = []
                    offset = find_next_header_offset(header)

                else:
                    offset = offset + BLOCK_SIZE
                    continue
        elif response.status_code in [416]:
            return headers

        else:
            raise NotImplementedError(f'Unable to handle HTTP Code: {response.status_code}')

