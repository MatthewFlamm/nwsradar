from homeassistant.components import camera
from pytest_homeassistant_custom_component.common import MockConfigEntry, async_fire_time_changed

from custom_components.nwsradar.const import DOMAIN

from tests.const import NWSRADAR_CONFIG

async def test_camera(hass, mock_nwsradar_lite):

    mock_nwsradar_lite[0].return_value = None
    mock_nwsradar_lite[1].return_value = b"Test"

    entry = MockConfigEntry(domain=DOMAIN, data=NWSRADAR_CONFIG,)
    entry.add_to_hass(hass)
    await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    state = hass.states.get("camera.abc_standard_composite_reflectivity_loop")


    await hass.async_block_till_done()
    assert state
    assert state.state == "idle"
    image = await camera.async_get_image(hass, "camera.abc_standard_composite_reflectivity_loop")
    assert image.content == b"Test"
    assert mock_nwsradar_lite[0].assert_called_once()
    assert mock_nwsradar_lite[1].assert_called_once()
