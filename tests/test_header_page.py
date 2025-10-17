class TestHeaderPage:
    def test_header(self, header_page):
        assert header_page.check_header()