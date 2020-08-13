from astropy.cloud.fits.datatypes import CloudService, FITSHeader
from astropy.cloud.fits.index import aws

def load_headers(url: str, service: CloudService=CloudService.AWS, request_payer: bool=False) -> FITSHeader:
    if cloud_service is CloudService.AWS:
        return aws.load_headers(url, request_payer)
    else:
        raise NotImplementedError(f'Cloud Service[{cloud_service}] not implemented')


