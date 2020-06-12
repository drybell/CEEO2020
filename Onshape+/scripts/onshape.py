import requests as r 
import random

parser = argparse.ArgumentParser(description='Test script for Onshape API')

parser.add_argument('-d', dest="did", help="Specify a document id for your Onshape workspace")
parser.add_argument('-w', dest="wid", help="Specify a workspace id for your Onshape workspace")

base_url = 'https://rogers.onshape.com'

document_id = '2696c6465ac59aff8ca3dfc1'

workspace_id = '/w/be80594917e5b1877e38d94e'

part_studio_eid = 'bd2b08bfd9046a3e25896bf3'


# From onshape_public onshape_client rip 
def make_nonce():
    """
    Generate a unique ID for the request, 25 chars in length
    Returns:
        - str: Cryptographic nonce
    """

    chars = string.digits + string.ascii_letters
    nonce = "".join(random.choice(chars) for i in range(25))

    # if self._logging:
    #     utils.log('nonce created: %s' % nonce)

    return nonce