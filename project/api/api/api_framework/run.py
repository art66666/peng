import pytest
from Common.project_path import *
from Common.base_page import BasePage

pytest.main(['-vs', ('--alluredir={0}').format(test_result_path), '--clean-alluredir'])

BasePage.allure_report(test_result_path,allure_report)