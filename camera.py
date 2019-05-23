"""Provide animated GIF loops of NWS radar imagery."""
from datetime import timedelta
import logging
import voluptuous as vol

from homeassistant.components.camera import PLATFORM_SCHEMA, Camera
from homeassistant.const import CONF_NAME
from homeassistant.helpers import config_validation as cv
from homeassistant.util import Throttle

_LOGGER = logging.getLogger(__name__)

CONF_FRAMES = 'frames'
CONF_STATION = 'station'

MIN_TIME_BETWEEN_UPDATES = timedelta(minutes=5)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_STATION): cv.string,
    vol.Optional(CONF_FRAMES): cv.positive_int,
    vol.Optional(CONF_NAME): cv.string,
})


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up NWS radar-loop camera component."""
    station = config[CONF_STATION]
    name = config.get(CONF_NAME) or config[CONF_STATION]
    frames = config.get(CONF_FRAMES) or 6
    add_entities([NWSRadarCam(name, station, frames)])
    
class NWSRadarCam(Camera):
    """A camera component producing animated NWS radar GIFs."""

    def __init__(self, name, station, frames):
        """Initialize the component."""
        from nws_radar import Nws_Radar
        super().__init__()
        self._name = name
        self._cam = Nws_Radar(station, 'NCR', nframes=frames)
        self._image = None

    def camera_image(self):
        """Return the current NWS radar loop"""
        self._update()
        _LOGGER.debug("display image")
        return self._image

    @property
    def name(self):
        """Return the component name."""
        return self._name

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def _update(self):
        _LOGGER.debug("update image")
        self._cam.update()
        self._image = self._cam.image()
