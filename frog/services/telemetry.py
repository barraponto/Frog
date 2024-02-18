class MockTelemetry:
    def __init__(self, *args, **kwargs):
        ...

    def capture(self, *args, **kwargs):
        ...

    def set_is_active(self, *args, **kwargs):
        ...

    def set_installation_id(self, *args, **kwargs):
        ...


telemetry = MockTelemetry()