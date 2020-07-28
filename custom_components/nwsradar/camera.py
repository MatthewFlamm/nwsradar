"""Provide animated GIF loops of NWS radar imagery."""
from datetime import timedelta
import logging
import voluptuous as vol

from nws_radar import Nws_Radar, Nws_Radar_Lite, Nws_Radar_Mosaic
from nws_radar.nws_radar_mosaic import REGIONS

from homeassistant.components.camera import Camera, PLATFORM_SCHEMA
from homeassistant.helpers import config_validation as cv
from homeassistant.util import Throttle

from . import unique_id
from .const import CONF_STATION, CONF_TYPE, CONF_LOOP, CONF_STYLE, RADAR_TYPES

_LOGGER = logging.getLogger(__name__)

MIN_TIME_BETWEEN_UPDATES = timedelta(minutes=5)


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the nwsradar camera platform."""
    station = entry.data[CONF_STATION]
    style = entry.data[CONF_STYLE]
    frames = 6 if entry.data[CONF_LOOP] else 1
    if entry.data[CONF_TYPE]:
        radartype = RADAR_TYPES[entry.data[CONF_TYPE]]
    else:
        radartype = ""
    name = f"{unique_id(entry.data)}"
    async_add_entities([NWSRadarCam(name, radartype.upper(), station.upper(), frames, style)])


class NWSRadarCam(Camera):
    """A camera component producing animated NWS radar GIFs."""

    def __init__(self, name, radartype, station, frames, style):
        """Initialize the component."""
        super().__init__()
        self._name = name
        self._unique_id = name
        if style == 'Enhanced':
            self._cam = Nws_Radar(station, radartype, nframes=frames)
        elif style == 'Standard':
            if frames == 1:
                self._cam = Nws_Radar_Lite(station, radartype, loop=False)
            else:
                self._cam = Nws_Radar_Lite(station, radartype, loop=True)
        elif style == 'Mosaic':
            self._cam = Nws_Radar_Mosaic(station, nframes=frames)  
        self._image = None

    @property
    def should_poll(self):
        return True
    
    def camera_image(self):
        """Return the current NWS radar loop"""
        self.update()
        _LOGGER.debug("display image")
        return self._image

    @property
    def name(self):
        """Return the component name."""
        return self._name

    @property
    def unique_id(self):
        """Return unique_id."""
        return self._unique_id
    
    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update(self):
        _LOGGER.debug("update image")
        self._cam.update()
        self._image = self._cam.image()
