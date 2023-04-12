from ApiPath.apipath import ApiPath as AP
from TestDatas import common_data as CP


class ApiUrl:
    # 登录地址
    login_url = ('{0}{1}').format(CP.url, AP.login_path)

    # 菜单地址
    menu_url = ('{0}{1}').format(CP.url, AP.menu_path)

    # 上传地址
    upload_url = ('{0}{1}').format(CP.url, AP.upload_path)

    """
    点位地址
    """
    # 查询点位地址
    search_point_url = ('{0}{1}').format(CP.url, AP.search_point_path)

    # 新增点位地址
    insert_point_url = ('{0}{1}').format(CP.url, AP.insert_point_path)

    # 批量删除点位地址
    batch_dalete_point_url = ('{0}{1}').format(CP.url, AP.batch_delete_point_path)

    """
    设备地址
    """

    # 新增设备地址
    insert_device_url = ('{0}{1}').format(CP.url, AP.insert_device_path)
