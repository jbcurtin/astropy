import enum
import typing

import numpy as np

from astropy.io import fits

class CloudService(enum.Enum):
    AWS = 'aws'
    DigitalOcean = 'digital-ocean'
    GoogleObjectStorage = 'google-object-storage'
    AzureBlobStorage = 'azure-blob-storage'
    Other = 'other'

class FITSHeader(typing.NamedTuple):
    offset: int
    length: int
    fits: fits.Header
