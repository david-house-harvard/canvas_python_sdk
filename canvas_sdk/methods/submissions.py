from canvas_sdk import client, utils


def submit_assignment_courses(request_ctx, course_id, assignment_id, submission_submission_type, comment_text_comment=None, submission_body=None, submission_url=None, submission_file_ids=None, submission_media_comment_id=None, submission_media_comment_type=None, **request_kwargs):
    """
    Make a submission for an assignment. You must be enrolled as a student in
    the course/section to do this.
    
    All online turn-in submission types are supported in this API. However,
    there are a few things that are not yet supported:
    
    * Files can be submitted based on a file ID of a user or group file. However, there is no API yet for listing the user and group files, or uploading new files via the API. A file upload API is coming soon.
    * Media comments can be submitted, however, there is no API yet for creating a media comment to submit.
    * Integration with Google Docs is not yet supported.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param submission_submission_type: (required) The type of submission being made. The assignment submission_types must
include this submission type as an allowed option, or the submission will be rejected with a 400 error.

The submission_type given determines which of the following parameters is
used. For instance, to submit a URL, submission [submission_type] must be
set to "online_url", otherwise the submission [url] parameter will be
ignored.
        :type submission_submission_type: string
        :param comment_text_comment: (optional) Include a textual comment with the submission.
        :type comment_text_comment: string or None
        :param submission_body: (optional) Submit the assignment as an HTML document snippet. Note this HTML snippet
will be sanitized using the same ruleset as a submission made from the
Canvas web UI. The sanitized HTML will be returned in the response as the
submission body. Requires a submission_type of "online_text_entry".
        :type submission_body: string or None
        :param submission_url: (optional) Submit the assignment as a URL. The URL scheme must be "http" or "https",
no "ftp" or other URL schemes are allowed. If no scheme is given (e.g.
"www.example.com") then "http" will be assumed. Requires a submission_type
of "online_url" or "basic_lti_launch".
        :type submission_url: string or None
        :param submission_file_ids: (optional) Submit the assignment as a set of one or more previously uploaded files
residing in the submitting user's files section (or the group's files
section, for group assignments).

To upload a new file to submit, see the submissions {api:SubmissionsApiController#create_file Upload a file API}.

Requires a submission_type of "online_upload".
        :type submission_file_ids: array or None
        :param submission_media_comment_id: (optional) The media comment id to submit. Media comment ids can be submitted via
this API, however, note that there is not yet an API to generate or list
existing media comments, so this functionality is currently of limited use.

Requires a submission_type of "media_recording".
        :type submission_media_comment_id: string or None
        :param submission_media_comment_type: (optional) The type of media comment being submitted.
        :type submission_media_comment_type: string or None
        :return: Submit an assignment
        :rtype: requests.Response (with void data)

    """

    submission_submission_type_types = ('online_text_entry', 'online_url', 'online_upload', 'media_recording', 'basic_lti_launch')
    submission_media_comment_type_types = ('audio', 'video')
    utils.validate_attr_is_acceptable(submission_submission_type, submission_submission_type_types)
    utils.validate_attr_is_acceptable(submission_media_comment_type, submission_media_comment_type_types)
    path = '/v1/courses/{course_id}/assignments/{assignment_id}/submissions'
    payload = {
        'comment[text_comment]': comment_text_comment,
        'submission[submission_type]': submission_submission_type,
        'submission[body]': submission_body,
        'submission[url]': submission_url,
        'submission[file_ids]': submission_file_ids,
        'submission[media_comment_id]': submission_media_comment_id,
        'submission[media_comment_type]': submission_media_comment_type,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def submit_assignment_sections(request_ctx, section_id, assignment_id, submission_submission_type, comment_text_comment=None, submission_body=None, submission_url=None, submission_file_ids=None, submission_media_comment_id=None, submission_media_comment_type=None, **request_kwargs):
    """
    Make a submission for an assignment. You must be enrolled as a student in
    the course/section to do this.
    
    All online turn-in submission types are supported in this API. However,
    there are a few things that are not yet supported:
    
    * Files can be submitted based on a file ID of a user or group file. However, there is no API yet for listing the user and group files, or uploading new files via the API. A file upload API is coming soon.
    * Media comments can be submitted, however, there is no API yet for creating a media comment to submit.
    * Integration with Google Docs is not yet supported.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param section_id: (required) ID
        :type section_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param submission_submission_type: (required) The type of submission being made. The assignment submission_types must
include this submission type as an allowed option, or the submission will be rejected with a 400 error.

The submission_type given determines which of the following parameters is
used. For instance, to submit a URL, submission [submission_type] must be
set to "online_url", otherwise the submission [url] parameter will be
ignored.
        :type submission_submission_type: string
        :param comment_text_comment: (optional) Include a textual comment with the submission.
        :type comment_text_comment: string or None
        :param submission_body: (optional) Submit the assignment as an HTML document snippet. Note this HTML snippet
will be sanitized using the same ruleset as a submission made from the
Canvas web UI. The sanitized HTML will be returned in the response as the
submission body. Requires a submission_type of "online_text_entry".
        :type submission_body: string or None
        :param submission_url: (optional) Submit the assignment as a URL. The URL scheme must be "http" or "https",
no "ftp" or other URL schemes are allowed. If no scheme is given (e.g.
"www.example.com") then "http" will be assumed. Requires a submission_type
of "online_url" or "basic_lti_launch".
        :type submission_url: string or None
        :param submission_file_ids: (optional) Submit the assignment as a set of one or more previously uploaded files
residing in the submitting user's files section (or the group's files
section, for group assignments).

To upload a new file to submit, see the submissions {api:SubmissionsApiController#create_file Upload a file API}.

Requires a submission_type of "online_upload".
        :type submission_file_ids: array or None
        :param submission_media_comment_id: (optional) The media comment id to submit. Media comment ids can be submitted via
this API, however, note that there is not yet an API to generate or list
existing media comments, so this functionality is currently of limited use.

Requires a submission_type of "media_recording".
        :type submission_media_comment_id: string or None
        :param submission_media_comment_type: (optional) The type of media comment being submitted.
        :type submission_media_comment_type: string or None
        :return: Submit an assignment
        :rtype: requests.Response (with void data)

    """

    submission_submission_type_types = ('online_text_entry', 'online_url', 'online_upload', 'media_recording', 'basic_lti_launch')
    submission_media_comment_type_types = ('audio', 'video')
    utils.validate_attr_is_acceptable(submission_submission_type, submission_submission_type_types)
    utils.validate_attr_is_acceptable(submission_media_comment_type, submission_media_comment_type_types)
    path = '/v1/sections/{section_id}/assignments/{assignment_id}/submissions'
    payload = {
        'comment[text_comment]': comment_text_comment,
        'submission[submission_type]': submission_submission_type,
        'submission[body]': submission_body,
        'submission[url]': submission_url,
        'submission[file_ids]': submission_file_ids,
        'submission[media_comment_id]': submission_media_comment_id,
        'submission[media_comment_type]': submission_media_comment_type,
    }
    url = request_ctx.base_api_url + path.format(section_id=section_id, assignment_id=assignment_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_assignment_submissions_courses(request_ctx, course_id, assignment_id, include=None, grouped=None, per_page=None, **request_kwargs):
    """
    Get all existing submissions for an assignment.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param include: (optional) Associations to include with the group.  "group" will add group_id and group_name.
        :type include: array or None
        :param grouped: (optional) If this argument is true, the response will be grouped by student groups.
        :type grouped: boolean or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List assignment submissions
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('submission_history', 'submission_comments', 'rubric_assessment', 'assignment', 'visibility', 'course', 'user', 'group')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/assignments/{assignment_id}/submissions'
    payload = {
        'include': include,
        'grouped': grouped,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_assignment_submissions_sections(request_ctx, section_id, assignment_id, include=None, grouped=None, per_page=None, **request_kwargs):
    """
    Get all existing submissions for an assignment.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param section_id: (required) ID
        :type section_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param include: (optional) Associations to include with the group.  "group" will add group_id and group_name.
        :type include: array or None
        :param grouped: (optional) If this argument is true, the response will be grouped by student groups.
        :type grouped: boolean or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List assignment submissions
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('submission_history', 'submission_comments', 'rubric_assessment', 'assignment', 'visibility', 'course', 'user', 'group')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/sections/{section_id}/assignments/{assignment_id}/submissions'
    payload = {
        'include': include,
        'grouped': grouped,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(section_id=section_id, assignment_id=assignment_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_submissions_for_multiple_assignments_courses(request_ctx, course_id, student_ids=None, assignment_ids=None, grouped=None, grading_period_id=None, order=None, order_direction=None, include=None, per_page=None, **request_kwargs):
    """
    Get all existing submissions for a given set of students and assignments.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param student_ids: (optional) List of student ids to return submissions for. If this argument is
omitted, return submissions for the calling user. Students may only list
their own submissions. Observers may only list those of associated
students. The special id "all" will return submissions for all students
in the course/section as appropriate.
        :type student_ids: array or None
        :param assignment_ids: (optional) List of assignments to return submissions for. If none are given,
submissions for all assignments are returned.
        :type assignment_ids: array or None
        :param grouped: (optional) If this argument is present, the response will be grouped by student,
rather than a flat array of submissions.
        :type grouped: boolean or None
        :param grading_period_id: (optional) The id of the grading period in which submissions are being requested
(Requires the Multiple Grading Periods account feature turned on)
        :type grading_period_id: integer or None
        :param order: (optional) The order submissions will be returned in.  Defaults to "id".  Doesn't
affect results for "grouped" mode.
        :type order: string or None
        :param order_direction: (optional) Determines whether ordered results are retured in ascending or descending
order.  Defaults to "ascending".  Doesn't affect results for "grouped" mode.
        :type order_direction: string or None
        :param include: (optional) Associations to include with the group. `total_scores` requires the
`grouped` argument.
        :type include: array or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List submissions for multiple assignments
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    order_types = ('id', 'graded_at')
    order_direction_types = ('ascending', 'descending')
    include_types = ('submission_history', 'submission_comments', 'rubric_assessment', 'assignment', 'total_scores', 'visibility', 'course', 'user')
    utils.validate_attr_is_acceptable(order, order_types)
    utils.validate_attr_is_acceptable(order_direction, order_direction_types)
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/students/submissions'
    payload = {
        'student_ids': student_ids,
        'assignment_ids': assignment_ids,
        'grouped': grouped,
        'grading_period_id': grading_period_id,
        'order': order,
        'order_direction': order_direction,
        'include': include,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_submissions_for_multiple_assignments_sections(request_ctx, section_id, student_ids=None, assignment_ids=None, grouped=None, grading_period_id=None, order=None, order_direction=None, include=None, per_page=None, **request_kwargs):
    """
    Get all existing submissions for a given set of students and assignments.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param section_id: (required) ID
        :type section_id: string
        :param student_ids: (optional) List of student ids to return submissions for. If this argument is
omitted, return submissions for the calling user. Students may only list
their own submissions. Observers may only list those of associated
students. The special id "all" will return submissions for all students
in the course/section as appropriate.
        :type student_ids: array or None
        :param assignment_ids: (optional) List of assignments to return submissions for. If none are given,
submissions for all assignments are returned.
        :type assignment_ids: array or None
        :param grouped: (optional) If this argument is present, the response will be grouped by student,
rather than a flat array of submissions.
        :type grouped: boolean or None
        :param grading_period_id: (optional) The id of the grading period in which submissions are being requested
(Requires the Multiple Grading Periods account feature turned on)
        :type grading_period_id: integer or None
        :param order: (optional) The order submissions will be returned in.  Defaults to "id".  Doesn't
affect results for "grouped" mode.
        :type order: string or None
        :param order_direction: (optional) Determines whether ordered results are retured in ascending or descending
order.  Defaults to "ascending".  Doesn't affect results for "grouped" mode.
        :type order_direction: string or None
        :param include: (optional) Associations to include with the group. `total_scores` requires the
`grouped` argument.
        :type include: array or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List submissions for multiple assignments
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    order_types = ('id', 'graded_at')
    order_direction_types = ('ascending', 'descending')
    include_types = ('submission_history', 'submission_comments', 'rubric_assessment', 'assignment', 'total_scores', 'visibility', 'course', 'user')
    utils.validate_attr_is_acceptable(order, order_types)
    utils.validate_attr_is_acceptable(order_direction, order_direction_types)
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/sections/{section_id}/students/submissions'
    payload = {
        'student_ids': student_ids,
        'assignment_ids': assignment_ids,
        'grouped': grouped,
        'grading_period_id': grading_period_id,
        'order': order,
        'order_direction': order_direction,
        'include': include,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(section_id=section_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_single_submission_courses(request_ctx, course_id, assignment_id, user_id, include=None, **request_kwargs):
    """
    Get a single submission, based on user id.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param user_id: (required) ID
        :type user_id: string
        :param include: (optional) Associations to include with the group.
        :type include: array or None
        :return: Get a single submission
        :rtype: requests.Response (with void data)

    """

    include_types = ('submission_history', 'submission_comments', 'rubric_assessment', 'visibility', 'course', 'user')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}'
    payload = {
        'include': include,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id, user_id=user_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_single_submission_sections(request_ctx, section_id, assignment_id, user_id, include=None, **request_kwargs):
    """
    Get a single submission, based on user id.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param section_id: (required) ID
        :type section_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param user_id: (required) ID
        :type user_id: string
        :param include: (optional) Associations to include with the group.
        :type include: array or None
        :return: Get a single submission
        :rtype: requests.Response (with void data)

    """

    include_types = ('submission_history', 'submission_comments', 'rubric_assessment', 'visibility', 'course', 'user')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}'
    payload = {
        'include': include,
    }
    url = request_ctx.base_api_url + path.format(section_id=section_id, assignment_id=assignment_id, user_id=user_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def upload_file_courses(request_ctx, course_id, assignment_id, user_id, **request_kwargs):
    """
    Upload a file to a submission.
    
    This API endpoint is the first step in uploading a file to a submission as a student.
    See the {file:file_uploads.html File Upload Documentation} for details on the file upload workflow.
    
    The final step of the file upload workflow will return the attachment data,
    including the new file id. The caller can then POST to submit the
    +online_upload+ assignment with these file ids.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param user_id: (required) ID
        :type user_id: string
        :return: Upload a file
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/files'
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id, user_id=user_id)
    response = client.post(request_ctx, url, **request_kwargs)

    return response


def upload_file_sections(request_ctx, section_id, assignment_id, user_id, **request_kwargs):
    """
    Upload a file to a submission.
    
    This API endpoint is the first step in uploading a file to a submission as a student.
    See the {file:file_uploads.html File Upload Documentation} for details on the file upload workflow.
    
    The final step of the file upload workflow will return the attachment data,
    including the new file id. The caller can then POST to submit the
    +online_upload+ assignment with these file ids.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param section_id: (required) ID
        :type section_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param user_id: (required) ID
        :type user_id: string
        :return: Upload a file
        :rtype: requests.Response (with void data)

    """

    path = '/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/files'
    url = request_ctx.base_api_url + path.format(section_id=section_id, assignment_id=assignment_id, user_id=user_id)
    response = client.post(request_ctx, url, **request_kwargs)

    return response


def grade_or_comment_on_submission_courses(request_ctx, course_id, assignment_id, user_id, comment_text_comment=None, comment_group_comment=None, comment_media_comment_id=None, comment_media_comment_type=None, comment_file_ids=None, include_visibility=None, submission_posted_grade=None, submission_excuse=None, rubric_assessment=None, **request_kwargs):
    """
    Comment on and/or update the grading for a student's assignment submission.
    If any submission or rubric_assessment arguments are provided, the user
    must have permission to manage grades in the appropriate context (course or
    section).

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param user_id: (required) ID
        :type user_id: string
        :param comment_text_comment: (optional) Add a textual comment to the submission.
        :type comment_text_comment: string or None
        :param comment_group_comment: (optional) Whether or not this comment should be sent to the entire group (defaults
to false). Ignored if this is not a group assignment or if no text_comment
is provided.
        :type comment_group_comment: boolean or None
        :param comment_media_comment_id: (optional) Add an audio/video comment to the submission. Media comments can be added
via this API, however, note that there is not yet an API to generate or
list existing media comments, so this functionality is currently of
limited use.
        :type comment_media_comment_id: string or None
        :param comment_media_comment_type: (optional) The type of media comment being added.
        :type comment_media_comment_type: string or None
        :param comment_file_ids: (optional) Attach files to this comment that were previously uploaded using the
Submission Comment API's files action
        :type comment_file_ids: array or None
        :param include_visibility: (optional) Whether this assignment is visible to the owner of the submission
        :type include_visibility: string or None
        :param submission_posted_grade: (optional) Assign a score to the submission, updating both the "score" and "grade"
fields on the submission record. This parameter can be passed in a few
different formats:

points:: A floating point or integral value, such as "13.5". The grade
  will be interpreted directly as the score of the assignment.
  Values above assignment.points_possible are allowed, for awarding
  extra credit.
percentage:: A floating point value appended with a percent sign, such as
   "40%". The grade will be interpreted as a percentage score on the
   assignment, where 100% == assignment.points_possible. Values above 100%
   are allowed, for awarding extra credit.
letter grade:: A letter grade, following the assignment's defined letter
   grading scheme. For example, "A-". The resulting score will be the high
   end of the defined range for the letter grade. For instance, if "B" is
   defined as 86% to 84%, a letter grade of "B" will be worth 86%. The
   letter grade will be rejected if the assignment does not have a defined
   letter grading scheme. For more fine-grained control of scores, pass in
   points or percentage rather than the letter grade.
"pass/complete/fail/incomplete":: A string value of "pass" or "complete"
   will give a score of 100%. "fail" or "incomplete" will give a score of
   0.

Note that assignments with grading_type of "pass_fail" can only be
assigned a score of 0 or assignment.points_possible, nothing inbetween. If
a posted_grade in the "points" or "percentage" format is sent, the grade
will only be accepted if the grade equals one of those two values.
        :type submission_posted_grade: string or None
        :param submission_excuse: (optional) Sets the "excused" status of an assignment.
        :type submission_excuse: boolean or None
        :param rubric_assessment: (optional) Assign a rubric assessment to this assignment submission. The
sub-parameters here depend on the rubric for the assignment. The general
format is, for each row in the rubric:

The points awarded for this row.
  rubric_assessment[criterion_id][points]

Comments to add for this row.
  rubric_assessment[criterion_id][comments]

For example, if the assignment rubric is (in JSON format):
  !!!javascript
  [
    {
      'id': 'crit1',
      'points': 10,
      'description': 'Criterion 1',
      'ratings':
      [
        { 'description': 'Good', 'points': 10 },
        { 'description': 'Poor', 'points': 3 }
      ]
    },
    {
      'id': 'crit2',
      'points': 5,
      'description': 'Criterion 2',
      'ratings':
      [
        { 'description': 'Complete', 'points': 5 },
        { 'description': 'Incomplete', 'points': 0 }
      ]
    }
  ]

Then a possible set of values for rubric_assessment would be:
    rubric_assessment[crit1][points]=3&rubric_assessment[crit2][points]=5&rubric_assessment[crit2][comments]=Well%20Done.
        :type rubric_assessment: RubricAssessment or None
        :return: Grade or comment on a submission
        :rtype: requests.Response (with void data)

    """

    comment_media_comment_type_types = ('audio', 'video')
    utils.validate_attr_is_acceptable(comment_media_comment_type, comment_media_comment_type_types)
    path = '/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}'
    payload = {
        'comment[text_comment]': comment_text_comment,
        'comment[group_comment]': comment_group_comment,
        'comment[media_comment_id]': comment_media_comment_id,
        'comment[media_comment_type]': comment_media_comment_type,
        'comment[file_ids]': comment_file_ids,
        'include[visibility]': include_visibility,
        'submission[posted_grade]': submission_posted_grade,
        'submission[excuse]': submission_excuse,
        'rubric_assessment': rubric_assessment,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id, user_id=user_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def grade_or_comment_on_submission_sections(request_ctx, section_id, assignment_id, user_id, comment_text_comment=None, comment_group_comment=None, comment_media_comment_id=None, comment_media_comment_type=None, comment_file_ids=None, include_visibility=None, submission_posted_grade=None, submission_excuse=None, rubric_assessment=None, **request_kwargs):
    """
    Comment on and/or update the grading for a student's assignment submission.
    If any submission or rubric_assessment arguments are provided, the user
    must have permission to manage grades in the appropriate context (course or
    section).

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param section_id: (required) ID
        :type section_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param user_id: (required) ID
        :type user_id: string
        :param comment_text_comment: (optional) Add a textual comment to the submission.
        :type comment_text_comment: string or None
        :param comment_group_comment: (optional) Whether or not this comment should be sent to the entire group (defaults
to false). Ignored if this is not a group assignment or if no text_comment
is provided.
        :type comment_group_comment: boolean or None
        :param comment_media_comment_id: (optional) Add an audio/video comment to the submission. Media comments can be added
via this API, however, note that there is not yet an API to generate or
list existing media comments, so this functionality is currently of
limited use.
        :type comment_media_comment_id: string or None
        :param comment_media_comment_type: (optional) The type of media comment being added.
        :type comment_media_comment_type: string or None
        :param comment_file_ids: (optional) Attach files to this comment that were previously uploaded using the
Submission Comment API's files action
        :type comment_file_ids: array or None
        :param include_visibility: (optional) Whether this assignment is visible to the owner of the submission
        :type include_visibility: string or None
        :param submission_posted_grade: (optional) Assign a score to the submission, updating both the "score" and "grade"
fields on the submission record. This parameter can be passed in a few
different formats:

points:: A floating point or integral value, such as "13.5". The grade
  will be interpreted directly as the score of the assignment.
  Values above assignment.points_possible are allowed, for awarding
  extra credit.
percentage:: A floating point value appended with a percent sign, such as
   "40%". The grade will be interpreted as a percentage score on the
   assignment, where 100% == assignment.points_possible. Values above 100%
   are allowed, for awarding extra credit.
letter grade:: A letter grade, following the assignment's defined letter
   grading scheme. For example, "A-". The resulting score will be the high
   end of the defined range for the letter grade. For instance, if "B" is
   defined as 86% to 84%, a letter grade of "B" will be worth 86%. The
   letter grade will be rejected if the assignment does not have a defined
   letter grading scheme. For more fine-grained control of scores, pass in
   points or percentage rather than the letter grade.
"pass/complete/fail/incomplete":: A string value of "pass" or "complete"
   will give a score of 100%. "fail" or "incomplete" will give a score of
   0.

Note that assignments with grading_type of "pass_fail" can only be
assigned a score of 0 or assignment.points_possible, nothing inbetween. If
a posted_grade in the "points" or "percentage" format is sent, the grade
will only be accepted if the grade equals one of those two values.
        :type submission_posted_grade: string or None
        :param submission_excuse: (optional) Sets the "excused" status of an assignment.
        :type submission_excuse: boolean or None
        :param rubric_assessment: (optional) Assign a rubric assessment to this assignment submission. The
sub-parameters here depend on the rubric for the assignment. The general
format is, for each row in the rubric:

The points awarded for this row.
  rubric_assessment[criterion_id][points]

Comments to add for this row.
  rubric_assessment[criterion_id][comments]

For example, if the assignment rubric is (in JSON format):
  !!!javascript
  [
    {
      'id': 'crit1',
      'points': 10,
      'description': 'Criterion 1',
      'ratings':
      [
        { 'description': 'Good', 'points': 10 },
        { 'description': 'Poor', 'points': 3 }
      ]
    },
    {
      'id': 'crit2',
      'points': 5,
      'description': 'Criterion 2',
      'ratings':
      [
        { 'description': 'Complete', 'points': 5 },
        { 'description': 'Incomplete', 'points': 0 }
      ]
    }
  ]

Then a possible set of values for rubric_assessment would be:
    rubric_assessment[crit1][points]=3&rubric_assessment[crit2][points]=5&rubric_assessment[crit2][comments]=Well%20Done.
        :type rubric_assessment: RubricAssessment or None
        :return: Grade or comment on a submission
        :rtype: requests.Response (with void data)

    """

    comment_media_comment_type_types = ('audio', 'video')
    utils.validate_attr_is_acceptable(comment_media_comment_type, comment_media_comment_type_types)
    path = '/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}'
    payload = {
        'comment[text_comment]': comment_text_comment,
        'comment[group_comment]': comment_group_comment,
        'comment[media_comment_id]': comment_media_comment_id,
        'comment[media_comment_type]': comment_media_comment_type,
        'comment[file_ids]': comment_file_ids,
        'include[visibility]': include_visibility,
        'submission[posted_grade]': submission_posted_grade,
        'submission[excuse]': submission_excuse,
        'rubric_assessment': rubric_assessment,
    }
    url = request_ctx.base_api_url + path.format(section_id=section_id, assignment_id=assignment_id, user_id=user_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_gradeable_students(request_ctx, course_id, assignment_id, per_page=None, **request_kwargs):
    """
    List students eligible to submit the assignment. The caller must have permission to view grades.
    
    Section-limited instructors will only see students in their own sections.
    
    returns [UserDisplay]

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List gradeable students
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/assignments/{assignment_id}/gradeable_students'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_multiple_assignments_gradeable_students(request_ctx, course_id, assignment_ids=None, per_page=None, **request_kwargs):
    """
    List students eligible to submit a list of assignments. The caller must have
    permission to view grades for the requested course.
    
    Section-limited instructors will only see students in their own sections.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_ids: (optional) Assignments being requested
        :type assignment_ids: array or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List multiple assignments gradeable students
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/assignments/gradeable_students'
    payload = {
        'assignment_ids': assignment_ids,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def grade_or_comment_on_multiple_submissions_courses_submissions(request_ctx, course_id, grade_data_student_id_posted_grade=None, grade_data_student_id_excuse=None, grade_data_student_id_rubric_assessment=None, grade_data_student_id_text_comment=None, grade_data_student_id_group_comment=None, grade_data_student_id_media_comment_id=None, grade_data_student_id_media_comment_type=None, grade_data_student_id_file_ids=None, **request_kwargs):
    """
    Update the grading and comments on multiple student's assignment
    submissions in an asynchronous job.
    
    The user must have permission to manage grades in the appropriate context
    (course or section).

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param grade_data_student_id_posted_grade: (optional) See documentation for the posted_grade argument in the
{api:SubmissionsApiController#update Submissions Update} documentation
        :type grade_data_student_id_posted_grade: string or None
        :param grade_data_student_id_excuse: (optional) See documentation for the excuse argument in the
{api:SubmissionsApiController#update Submissions Update} documentation
        :type grade_data_student_id_excuse: boolean or None
        :param grade_data_student_id_rubric_assessment: (optional) See documentation for the rubric_assessment argument in the
{api:SubmissionsApiController#update Submissions Update} documentation
        :type grade_data_student_id_rubric_assessment: RubricAssessment or None
        :param grade_data_student_id_text_comment: (optional) no description
        :type grade_data_student_id_text_comment: string or None
        :param grade_data_student_id_group_comment: (optional) no description
        :type grade_data_student_id_group_comment: boolean or None
        :param grade_data_student_id_media_comment_id: (optional) no description
        :type grade_data_student_id_media_comment_id: string or None
        :param grade_data_student_id_media_comment_type: (optional) no description
        :type grade_data_student_id_media_comment_type: string or None
        :param grade_data_student_id_file_ids: (optional) See documentation for the comment[] arguments in the
{api:SubmissionsApiController#update Submissions Update} documentation
        :type grade_data_student_id_file_ids: array or None
        :return: Grade or comment on multiple submissions
        :rtype: requests.Response (with Progress data)

    """

    grade_data_student_id_media_comment_type_types = ('audio', 'video')
    utils.validate_attr_is_acceptable(grade_data_student_id_media_comment_type, grade_data_student_id_media_comment_type_types)
    path = '/v1/courses/{course_id}/submissions/update_grades'
    payload = {
        'grade_data[student_id][posted_grade]': grade_data_student_id_posted_grade,
        'grade_data[student_id][excuse]': grade_data_student_id_excuse,
        'grade_data[student_id][rubric_assessment]': grade_data_student_id_rubric_assessment,
        'grade_data[student_id][text_comment]': grade_data_student_id_text_comment,
        'grade_data[student_id][group_comment]': grade_data_student_id_group_comment,
        'grade_data[student_id][media_comment_id]': grade_data_student_id_media_comment_id,
        'grade_data[student_id][media_comment_type]': grade_data_student_id_media_comment_type,
        'grade_data[student_id][file_ids]': grade_data_student_id_file_ids,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def grade_or_comment_on_multiple_submissions_courses_assignments(request_ctx, course_id, assignment_id, grade_data_student_id_posted_grade=None, grade_data_student_id_excuse=None, grade_data_student_id_rubric_assessment=None, grade_data_student_id_text_comment=None, grade_data_student_id_group_comment=None, grade_data_student_id_media_comment_id=None, grade_data_student_id_media_comment_type=None, grade_data_student_id_file_ids=None, **request_kwargs):
    """
    Update the grading and comments on multiple student's assignment
    submissions in an asynchronous job.
    
    The user must have permission to manage grades in the appropriate context
    (course or section).

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param grade_data_student_id_posted_grade: (optional) See documentation for the posted_grade argument in the
{api:SubmissionsApiController#update Submissions Update} documentation
        :type grade_data_student_id_posted_grade: string or None
        :param grade_data_student_id_excuse: (optional) See documentation for the excuse argument in the
{api:SubmissionsApiController#update Submissions Update} documentation
        :type grade_data_student_id_excuse: boolean or None
        :param grade_data_student_id_rubric_assessment: (optional) See documentation for the rubric_assessment argument in the
{api:SubmissionsApiController#update Submissions Update} documentation
        :type grade_data_student_id_rubric_assessment: RubricAssessment or None
        :param grade_data_student_id_text_comment: (optional) no description
        :type grade_data_student_id_text_comment: string or None
        :param grade_data_student_id_group_comment: (optional) no description
        :type grade_data_student_id_group_comment: boolean or None
        :param grade_data_student_id_media_comment_id: (optional) no description
        :type grade_data_student_id_media_comment_id: string or None
        :param grade_data_student_id_media_comment_type: (optional) no description
        :type grade_data_student_id_media_comment_type: string or None
        :param grade_data_student_id_file_ids: (optional) See documentation for the comment[] arguments in the
{api:SubmissionsApiController#update Submissions Update} documentation
        :type grade_data_student_id_file_ids: array or None
        :return: Grade or comment on multiple submissions
        :rtype: requests.Response (with Progress data)

    """

    grade_data_student_id_media_comment_type_types = ('audio', 'video')
    utils.validate_attr_is_acceptable(grade_data_student_id_media_comment_type, grade_data_student_id_media_comment_type_types)
    path = '/v1/courses/{course_id}/assignments/{assignment_id}/submissions/update_grades'
    payload = {
        'grade_data[student_id][posted_grade]': grade_data_student_id_posted_grade,
        'grade_data[student_id][excuse]': grade_data_student_id_excuse,
        'grade_data[student_id][rubric_assessment]': grade_data_student_id_rubric_assessment,
        'grade_data[student_id][text_comment]': grade_data_student_id_text_comment,
        'grade_data[student_id][group_comment]': grade_data_student_id_group_comment,
        'grade_data[student_id][media_comment_id]': grade_data_student_id_media_comment_id,
        'grade_data[student_id][media_comment_type]': grade_data_student_id_media_comment_type,
        'grade_data[student_id][file_ids]': grade_data_student_id_file_ids,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def grade_or_comment_on_multiple_submissions_sections_submissions(request_ctx, section_id, grade_data_student_id_posted_grade=None, grade_data_student_id_excuse=None, grade_data_student_id_rubric_assessment=None, grade_data_student_id_text_comment=None, grade_data_student_id_group_comment=None, grade_data_student_id_media_comment_id=None, grade_data_student_id_media_comment_type=None, grade_data_student_id_file_ids=None, **request_kwargs):
    """
    Update the grading and comments on multiple student's assignment
    submissions in an asynchronous job.
    
    The user must have permission to manage grades in the appropriate context
    (course or section).

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param section_id: (required) ID
        :type section_id: string
        :param grade_data_student_id_posted_grade: (optional) See documentation for the posted_grade argument in the
{api:SubmissionsApiController#update Submissions Update} documentation
        :type grade_data_student_id_posted_grade: string or None
        :param grade_data_student_id_excuse: (optional) See documentation for the excuse argument in the
{api:SubmissionsApiController#update Submissions Update} documentation
        :type grade_data_student_id_excuse: boolean or None
        :param grade_data_student_id_rubric_assessment: (optional) See documentation for the rubric_assessment argument in the
{api:SubmissionsApiController#update Submissions Update} documentation
        :type grade_data_student_id_rubric_assessment: RubricAssessment or None
        :param grade_data_student_id_text_comment: (optional) no description
        :type grade_data_student_id_text_comment: string or None
        :param grade_data_student_id_group_comment: (optional) no description
        :type grade_data_student_id_group_comment: boolean or None
        :param grade_data_student_id_media_comment_id: (optional) no description
        :type grade_data_student_id_media_comment_id: string or None
        :param grade_data_student_id_media_comment_type: (optional) no description
        :type grade_data_student_id_media_comment_type: string or None
        :param grade_data_student_id_file_ids: (optional) See documentation for the comment[] arguments in the
{api:SubmissionsApiController#update Submissions Update} documentation
        :type grade_data_student_id_file_ids: array or None
        :return: Grade or comment on multiple submissions
        :rtype: requests.Response (with Progress data)

    """

    grade_data_student_id_media_comment_type_types = ('audio', 'video')
    utils.validate_attr_is_acceptable(grade_data_student_id_media_comment_type, grade_data_student_id_media_comment_type_types)
    path = '/v1/sections/{section_id}/submissions/update_grades'
    payload = {
        'grade_data[student_id][posted_grade]': grade_data_student_id_posted_grade,
        'grade_data[student_id][excuse]': grade_data_student_id_excuse,
        'grade_data[student_id][rubric_assessment]': grade_data_student_id_rubric_assessment,
        'grade_data[student_id][text_comment]': grade_data_student_id_text_comment,
        'grade_data[student_id][group_comment]': grade_data_student_id_group_comment,
        'grade_data[student_id][media_comment_id]': grade_data_student_id_media_comment_id,
        'grade_data[student_id][media_comment_type]': grade_data_student_id_media_comment_type,
        'grade_data[student_id][file_ids]': grade_data_student_id_file_ids,
    }
    url = request_ctx.base_api_url + path.format(section_id=section_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def grade_or_comment_on_multiple_submissions_sections_assignments(request_ctx, section_id, assignment_id, grade_data_student_id_posted_grade=None, grade_data_student_id_excuse=None, grade_data_student_id_rubric_assessment=None, grade_data_student_id_text_comment=None, grade_data_student_id_group_comment=None, grade_data_student_id_media_comment_id=None, grade_data_student_id_media_comment_type=None, grade_data_student_id_file_ids=None, **request_kwargs):
    """
    Update the grading and comments on multiple student's assignment
    submissions in an asynchronous job.
    
    The user must have permission to manage grades in the appropriate context
    (course or section).

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param section_id: (required) ID
        :type section_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param grade_data_student_id_posted_grade: (optional) See documentation for the posted_grade argument in the
{api:SubmissionsApiController#update Submissions Update} documentation
        :type grade_data_student_id_posted_grade: string or None
        :param grade_data_student_id_excuse: (optional) See documentation for the excuse argument in the
{api:SubmissionsApiController#update Submissions Update} documentation
        :type grade_data_student_id_excuse: boolean or None
        :param grade_data_student_id_rubric_assessment: (optional) See documentation for the rubric_assessment argument in the
{api:SubmissionsApiController#update Submissions Update} documentation
        :type grade_data_student_id_rubric_assessment: RubricAssessment or None
        :param grade_data_student_id_text_comment: (optional) no description
        :type grade_data_student_id_text_comment: string or None
        :param grade_data_student_id_group_comment: (optional) no description
        :type grade_data_student_id_group_comment: boolean or None
        :param grade_data_student_id_media_comment_id: (optional) no description
        :type grade_data_student_id_media_comment_id: string or None
        :param grade_data_student_id_media_comment_type: (optional) no description
        :type grade_data_student_id_media_comment_type: string or None
        :param grade_data_student_id_file_ids: (optional) See documentation for the comment[] arguments in the
{api:SubmissionsApiController#update Submissions Update} documentation
        :type grade_data_student_id_file_ids: array or None
        :return: Grade or comment on multiple submissions
        :rtype: requests.Response (with Progress data)

    """

    grade_data_student_id_media_comment_type_types = ('audio', 'video')
    utils.validate_attr_is_acceptable(grade_data_student_id_media_comment_type, grade_data_student_id_media_comment_type_types)
    path = '/v1/sections/{section_id}/assignments/{assignment_id}/submissions/update_grades'
    payload = {
        'grade_data[student_id][posted_grade]': grade_data_student_id_posted_grade,
        'grade_data[student_id][excuse]': grade_data_student_id_excuse,
        'grade_data[student_id][rubric_assessment]': grade_data_student_id_rubric_assessment,
        'grade_data[student_id][text_comment]': grade_data_student_id_text_comment,
        'grade_data[student_id][group_comment]': grade_data_student_id_group_comment,
        'grade_data[student_id][media_comment_id]': grade_data_student_id_media_comment_id,
        'grade_data[student_id][media_comment_type]': grade_data_student_id_media_comment_type,
        'grade_data[student_id][file_ids]': grade_data_student_id_file_ids,
    }
    url = request_ctx.base_api_url + path.format(section_id=section_id, assignment_id=assignment_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def mark_submission_as_read_courses(request_ctx, course_id, assignment_id, user_id, **request_kwargs):
    """
    No request fields are necessary.
    
    On success, the response will be 204 No Content with an empty body.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param user_id: (required) ID
        :type user_id: string
        :return: Mark submission as read
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/read'
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id, user_id=user_id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def mark_submission_as_read_sections(request_ctx, section_id, assignment_id, user_id, **request_kwargs):
    """
    No request fields are necessary.
    
    On success, the response will be 204 No Content with an empty body.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param section_id: (required) ID
        :type section_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param user_id: (required) ID
        :type user_id: string
        :return: Mark submission as read
        :rtype: requests.Response (with void data)

    """

    path = '/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/read'
    url = request_ctx.base_api_url + path.format(section_id=section_id, assignment_id=assignment_id, user_id=user_id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def mark_submission_as_unread_courses(request_ctx, course_id, assignment_id, user_id, **request_kwargs):
    """
    No request fields are necessary.
    
    On success, the response will be 204 No Content with an empty body.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param user_id: (required) ID
        :type user_id: string
        :return: Mark submission as unread
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/read'
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id, user_id=user_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def mark_submission_as_unread_sections(request_ctx, section_id, assignment_id, user_id, **request_kwargs):
    """
    No request fields are necessary.
    
    On success, the response will be 204 No Content with an empty body.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param section_id: (required) ID
        :type section_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param user_id: (required) ID
        :type user_id: string
        :return: Mark submission as unread
        :rtype: requests.Response (with void data)

    """

    path = '/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/read'
    url = request_ctx.base_api_url + path.format(section_id=section_id, assignment_id=assignment_id, user_id=user_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


