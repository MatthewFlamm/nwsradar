"""Fixtures for National Weather Service Radar tests."""
import pytest

from pytest_homeassistant_custom_component.async_mock import AsyncMock, patch

pytest_plugins = "pytest_homeassistant_custom_component"

@pytest.fixture()
def mock_nwsradar():
    """Mock nwsradar classes with default values."""
    with patch(
            "custom_components.nwsradar.camera.Nws_Radar", autospec=True
    ) as mock_nwsradar:
        yield mock_nwsradar


@pytest.fixture()
def mock_nwsradar_lite():
    """Mock nwsradar classes with default values."""
    with patch(
            "custom_components.nwsradar.camera.Nws_Radar_Lite", autospec=True
    ) as mock_nwsradar_lite:
        yield mock_nwsradar_lite


@pytest.fixture()
def mock_nwsradar_mosaic():
    """Mock nwsradar classes with default values."""
    with patch(
            "custom_components.nwsradar.camera.Nws_Radar_Mosaic", autospec=True
    ) as mock_nwsradar_mosaic:

        yield mock_nwsradar_mosaic
