from canvas_sdk import client, utils

def list_available_tabs_for_course_or_group_courses(request_ctx, course_id, include, **request_kwargs):
    """
    Returns a list of navigation tabs available in the current context.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param include: (required) Optionally include external tool tabs in the returned list of tabs (Only has effect for courses, not groups)
        :type include: string
        :return: List available tabs for a course or group
        :rtype: requests.Response (with void data)

    """

    include_types = ('external')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/tabs'
    payload = {
        'include' : include,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_available_tabs_for_course_or_group_groups(request_ctx, group_id, include, **request_kwargs):
    """
    Returns a list of navigation tabs available in the current context.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param include: (required) Optionally include external tool tabs in the returned list of tabs (Only has effect for courses, not groups)
        :type include: string
        :return: List available tabs for a course or group
        :rtype: requests.Response (with void data)

    """

    include_types = ('external')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/groups/{group_id}/tabs'
    payload = {
        'include' : include,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_tab_for_course(request_ctx, course_id, tab_id, position, hidden, **request_kwargs):
    """
    Home and Settings tabs are not manageable, and can't be hidden or moved
    
    Returns a tab object

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param tab_id: (required) ID
        :type tab_id: string
        :param position: (required) The new position of the tab, 1-based
        :type position: integer
        :param hidden: (required) \\ true, or false.
        :type hidden: string
        :return: Update a tab for a course
        :rtype: requests.Response (with Tab data)

    """

    path = '/v1/courses/{course_id}/tabs/{tab_id}'
    payload = {
        'position' : position,
        'hidden' : hidden,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, tab_id=tab_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


