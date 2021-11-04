from Src.Setup.WebdriverSetup import WebbriverSetup

class CyberAttackStatistics(WebbriverSetup):
    # Testcase to verify that table can be fitered
    def test_filter_statistics_by_name(self):
        search_key = 'ss'
        self.statisticsPage.filter_statistics(search_key)
        self.statisticsPage.verify_filtered_result_for_name(search_key)
        self.statisticsPage.clear_filter()
    
    # Testcase to sort table by name
    def test_sort_statistics_by_name(self):
        self.statisticsPage.sort_statistics_by("name")
        self.statisticsPage.verify_sort_statistics("name")

    # Testcase to sort table by number of cases
    def test_sort_statistics_by_number_of_cases(self):
        self.statisticsPage.sort_statistics_by("number of cases")
        self.statisticsPage.verify_sort_statistics("number of cases")

    # Testcase to sort table by impact score
    def test_sort_statistics_by_impact_score(self):
        self.statisticsPage.sort_statistics_by("impact score")
        self.statisticsPage.verify_sort_statistics("impact score")

    # Testcase to sort table by complexity
    def test_sort_statistics_by_complexity(self):
        self.statisticsPage.sort_statistics_by("complexity")
        self.statisticsPage.verify_sort_statistics("complexity")
    
    # Testcase to sort filtered table by name
    def test_sort_statistics_by_name_for_filtered_result(self):
        search_key = 'ss'
        self.statisticsPage.filter_statistics(search_key)
        self.statisticsPage.verify_filtered_result_for_name(search_key)
        self.statisticsPage.sort_statistics_by("name")
        self.statisticsPage.verify_sort_statistics("name")
        self.statisticsPage.clear_filter()