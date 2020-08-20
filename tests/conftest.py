"""Fixtures for National Weather Service Radar tests."""
import pytest

from pytest_homeassistant_custom_component.async_mock import AsyncMock, patch

pytest_plugins = "pytest_homeassistant_custom_component"

@pytest.fixture()
def mock_nwsradar():
    """Mock nwsradar classes with default values."""
    with patch(
            "custom_components.nwsradar.camera.Nws_Radar.update"
    ) as mock_nwsradar_update, patch(
            "custom_components.nwsradar.camera.Nws_Radar.image"
    ) as mock_nwsradar_image:
        yield mock_nwsradar_update, mock_nwsradar_image


@pytest.fixture()
def mock_nwsradar_lite():
    """Mock nwsradar classes with default values."""
    with patch(
        "custom_components.nwsradar.camera.Nws_Radar_Lite.update"
    ) as mock_nwsradar_lite_update, patch(
        "custom_components.nwsradar.camera.Nws_Radar_Lite.image"
    ) as mock_nwsradar_lite_image:
        yield mock_nwsradar_lite_update, mock_nwsradar_lite_image


@pytest.fixture()
def mock_nwsradar_mosaic():
    """Mock nwsradar classes with default values."""
    with patch(
        "custom_components.nwsradar.camera.Nws_Radar_Mosaic.update"
    ) as mock_nwsradar_mosaic_update, patch(
        "custom_components.nwsradar.camera.Nws_Radar_Mosaic.image"
    ) as mock_nwsradar_mosaic_image:

        yield mock_nwsradar_mosaic_update, mock_nwsradar_mosaic_image
