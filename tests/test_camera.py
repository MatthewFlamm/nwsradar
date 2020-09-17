from unittest.mock import Mock
from homeassistant import config_entries
from homeassistant.components import camera
from homeassistant.setup import async_setup_component
from pytest_homeassistant_custom_component.common import (
    MockConfigEntry,
    async_fire_time_changed,
)

from custom_components.nwsradar.const import DOMAIN

from tests.const import (
    NWSRADAR_CONFIG,
    NWSRADAR_CONFIG_ENHANCED,
    NWSRADAR_CONFIG_MOSAIC,
)


async def test_camera(hass, mock_nwsradar_lite):

    instance = mock_nwsradar_lite.return_value
    instance.update = Mock(return_value=None)
    instance.image = Mock(return_value=b"Test")

    entry = MockConfigEntry(
        domain=DOMAIN,
        data=NWSRADAR_CONFIG,
    )
    entry.add_to_hass(hass)
    await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    state = hass.states.get("camera.abc_standard_composite_reflectivity_loop")

    assert state
    assert state.state == "idle"
    image = await camera.async_get_image(
        hass, "camera.abc_standard_composite_reflectivity_loop"
    )
    assert image.content == b"Test"

    instance.image.assert_called_once()
    instance.update.assert_called_once()


async def test_camera_enhanced(hass, mock_nwsradar):

    instance = mock_nwsradar.return_value
    instance.update = Mock(return_value=None)
    instance.image = Mock(return_value=b"Test")

    entry = MockConfigEntry(
        domain=DOMAIN,
        data=NWSRADAR_CONFIG_ENHANCED,
    )
    entry.add_to_hass(hass)
    await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    state = hass.states.get("camera.abc_enhanced_composite_reflectivity_loop")

    assert state
    assert state.state == "idle"
    image = await camera.async_get_image(
        hass, "camera.abc_enhanced_composite_reflectivity_loop"
    )
    assert image.content == b"Test"

    instance.image.assert_called_once()
    instance.update.assert_called_once()


async def test_camera_mosaic(hass, mock_nwsradar_mosaic):

    instance = mock_nwsradar_mosaic.return_value
    instance.update = Mock(return_value=None)
    instance.image = Mock(return_value=b"Test")

    entry = MockConfigEntry(
        domain=DOMAIN,
        data=NWSRADAR_CONFIG_MOSAIC,
    )
    entry.add_to_hass(hass)
    await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    state = hass.states.get("camera.abc_mosaic_loop")

    assert state
    assert state.state == "idle"
    image = await camera.async_get_image(hass, "camera.abc_mosaic_loop")
    assert image.content == b"Test"

    instance.image.assert_called_once()
    instance.update.assert_called_once()


async def test_import(hass, mock_nwsradar):

    config = {"camera": {"platform": "nwsradar", "station": "ABC"}}

    await async_setup_component(hass, "camera", config)
    await hass.async_block_till_done()

    state = hass.states.get("camera.abc")

    assert state
    assert state.state == "idle"
