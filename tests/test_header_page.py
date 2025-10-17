class TestHeaderPage:
    def test_logo_scooter(self, header_page):
        assert header_page.check_header()