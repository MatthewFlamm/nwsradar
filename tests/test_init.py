"""Tests for init module."""
from custom_components.nwsradar.const import DOMAIN, CONF_LOOP, CONF_STYLE, CONF_TYPE
from homeassistant.components.camera import DOMAIN as CAMERA_DOMAIN

from pytest_homeassistant_custom_component.common import MockConfigEntry
from tests.const import NWSRADAR_CONFIG


async def test_unload_entry(hass, mock_nwsradar_lite):
    """Test that nws setup with config yaml."""
    entry = MockConfigEntry(domain=DOMAIN, data=NWSRADAR_CONFIG,)
    entry.add_to_hass(hass)

    await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    assert len(hass.states.async_entity_ids(CAMERA_DOMAIN)) == 1
    entries = hass.config_entries.async_entries(DOMAIN)
    assert len(entries) == 1

    assert await hass.config_entries.async_unload(entries[0].entry_id)
    assert len(hass.states.async_entity_ids(CAMERA_DOMAIN)) == 0
    assert len(hass.states.async_entity_ids(DOMAIN)) == 0


async def test_no_loop(hass, mock_nwsradar_lite):
    """Test that nws setup with config yaml."""
    data = NWSRADAR_CONFIG.copy()
    data[CONF_LOOP] = False
    entry = MockConfigEntry(domain=DOMAIN, data=data,)
    entry.add_to_hass(hass)

    await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    assert len(hass.states.async_entity_ids(CAMERA_DOMAIN)) == 1
    assert (
        hass.states.async_entity_ids(CAMERA_DOMAIN)[0]
        == "camera.abc_standard_composite_reflectivity"
    )


async def test_enhanced(hass, mock_nwsradar):
    """Test that nws setup with config yaml."""
    data = NWSRADAR_CONFIG.copy()
    data[CONF_STYLE] = "Enhanced"
    entry = MockConfigEntry(domain=DOMAIN, data=data,)
    entry.add_to_hass(hass)

    await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    assert len(hass.states.async_entity_ids(CAMERA_DOMAIN)) == 1
    assert (
        hass.states.async_entity_ids(CAMERA_DOMAIN)[0]
        == "camera.abc_enhanced_composite_reflectivity_loop"
    )


async def test_mosaic(hass, mock_nwsradar_mosaic):
    """Test that nws setup with config yaml."""
    data = NWSRADAR_CONFIG.copy()
    data[CONF_STYLE] = "Mosaic"
    data[CONF_TYPE] = ""
    entry = MockConfigEntry(domain=DOMAIN, data=data,)
    entry.add_to_hass(hass)

    await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    assert len(hass.states.async_entity_ids(CAMERA_DOMAIN)) == 1
    assert hass.states.async_entity_ids(CAMERA_DOMAIN)[0] == "camera.abc_mosaic_loop"
