class ApiPath:
    # 登录路径
    login_path = '/auth/oauth/token'
    # 菜单路径
    menu_path = '/admin/menu'
    # 上传路径
    upload_path = '/device/device/file/upload'

    """
    点位新增、查询、删除路径
    """
    # 点位查询路径
    search_point_path = '/device/point/info/page'
    # 点位新增路径
    insert_point_path = '/device/point/info/save'
    # 批量删除点位路径
    batch_delete_point_path = '/device/point/info/remove'

    """
    设备新增、查询、删除路径
    """


    # 设备新增路径
    insert_device_path = '/device/device/info/saveDevice'