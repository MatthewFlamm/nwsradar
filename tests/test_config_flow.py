"""Test the National Weather Service Radar config flow."""
import aiohttp

from homeassistant import config_entries, setup
import pytest
from pytest_homeassistant_custom_component.async_mock import patch

from custom_components.nwsradar.const import DOMAIN


@pytest.mark.parametrize(
    "input_1,step_id_2,input_2,title,data",
    [
        (
            "Standard",
            "standard_enhanced",
            {"type": "Composite Reflectivity", "loop": True, "station": "ABC"},
            "ABC Standard Composite Reflectivity Loop",
            {
                "type": "Composite Reflectivity",
                "style": "Standard",
                "loop": True,
                "station": "ABC",
                "name": None,
            },
        ),
        (
            "Enhanced",
            "standard_enhanced",
            {"type": "Composite Reflectivity", "loop": True, "station": "ABC"},
            "ABC Enhanced Composite Reflectivity Loop",
            {
                "type": "Composite Reflectivity",
                "style": "Enhanced",
                "loop": True,
                "station": "ABC",
                "name": None,
            },
        ),
        (
            "Mosaic",
            "mosaic",
            {"loop": True, "station": "NAT"},
            "NAT Mosaic  Loop",  # extra space since no type isnt handled well
            {
                "type": "",
                "style": "Mosaic",
                "loop": True,
                "station": "NAT",
                "name": None,
            },
        ),
    ],
)
async def test_form(input_1, step_id_2, input_2, title, data, hass):
    """Test we get the form."""
    await setup.async_setup_component(hass, "persistent_notification", {})
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] == "form"
    assert result["errors"] == {}

    with patch(
        "custom_components.nwsradar.async_setup", return_value=True
    ) as mock_setup, patch(
        "custom_components.nwsradar.async_setup_entry",
        return_value=True,
    ) as mock_setup_entry:
        result2 = await hass.config_entries.flow.async_configure(
            result["flow_id"], {"style": input_1}
        )
        assert result2["type"] == "form"
        assert result2["step_id"] == step_id_2

        result3 = await hass.config_entries.flow.async_configure(
            result["flow_id"], input_2
        )

    assert result3["type"] == "create_entry"
    assert result3["title"] == title
    assert result3["data"] == data

    await hass.async_block_till_done()
    assert len(mock_setup.mock_calls) == 1
    assert len(mock_setup_entry.mock_calls) == 1


async def test_impory(hass):
    """Test we get the form."""
    await setup.async_setup_component(hass, "persistent_notification", {})

    with patch(
        "custom_components.nwsradar.async_setup", return_value=True
    ) as mock_setup, patch(
        "custom_components.nwsradar.async_setup_entry",
        return_value=True,
    ) as mock_setup_entry:
        result = await hass.config_entries.flow.async_init(
            DOMAIN,
            context={"source": config_entries.SOURCE_IMPORT},
            data={
                "type": "Composite Reflectivity",
                "style": "Standard",
                "loop": True,
                "station": "ABC",
                "name": None,
            },
        )
    assert result["type"] == "create_entry"
    assert result["title"] == "ABC Standard Composite Reflectivity Loop"
    assert result["data"] == {
        "type": "Composite Reflectivity",
        "style": "Standard",
        "loop": True,
        "station": "ABC",
        "name": None,
    }

    await hass.async_block_till_done()
    assert len(mock_setup.mock_calls) == 1
    assert len(mock_setup_entry.mock_calls) == 1
