import logging
logger = logging.getLogger(__name__)


MEDIA_LIB_PATH_NAME = 'CHANNEL_SURFER_MEDIA'

# initialization
channel_03_content = dict()
channel_09_content = dict()
channel_18_content = dict()
channel_36_content = dict()
channel_46_content = dict()
channel_55_content = dict()

# initialized as a tuple for type reasons and immutability during runtime
# when building the channel we could nuke these and populate new ones
channel_mapping = {
    'Channel 03': ('ABC',   channel_03_content, ),
    'Channel 09': ('WSOC',  channel_09_content, ),
    'Channel 18': ('FOX',   channel_18_content, ),
    'Channel 36': ('CBS',   channel_36_content, ),
    'Channel 46': ('UPN',   channel_46_content, ),
    'Channel 55': ('WB',    channel_55_content, ),
}
