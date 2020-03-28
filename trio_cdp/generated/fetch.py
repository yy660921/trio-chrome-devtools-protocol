# DO NOT EDIT THIS FILE!
#
# This code is generated off of PyCDP modules. If you need to make
# changes, edit the generator and regenerate all of the modules.

from __future__ import annotations
import typing

from ..context import get_connection_context, get_session_context

import cdp.fetch
from cdp.fetch import (
    AuthChallenge,
    AuthChallengeResponse,
    AuthRequired,
    HeaderEntry,
    RequestId,
    RequestPattern,
    RequestPaused,
    RequestStage
)


async def continue_request(
        request_id: RequestId,
        url: typing.Optional[str] = None,
        method: typing.Optional[str] = None,
        post_data: typing.Optional[str] = None,
        headers: typing.Optional[typing.List[HeaderEntry]] = None
    ) -> None:
    '''
    Continues the request, optionally modifying some of its parameters.

    :param request_id: An id the client received in requestPaused event.
    :param url: *(Optional)* If set, the request url will be modified in a way that's not observable by page.
    :param method: *(Optional)* If set, the request method is overridden.
    :param post_data: *(Optional)* If set, overrides the post data in the request.
    :param headers: *(Optional)* If set, overrides the request headrts.
    '''
    session = get_session_context('fetch.continue_request')
    return await session.execute(cdp.fetch.continue_request(request_id, url, method, post_data, headers))


async def continue_with_auth(
        request_id: RequestId,
        auth_challenge_response: AuthChallengeResponse
    ) -> None:
    '''
    Continues a request supplying authChallengeResponse following authRequired event.

    :param request_id: An id the client received in authRequired event.
    :param auth_challenge_response: Response to  with an authChallenge.
    '''
    session = get_session_context('fetch.continue_with_auth')
    return await session.execute(cdp.fetch.continue_with_auth(request_id, auth_challenge_response))


async def disable() -> None:
    '''
    Disables the fetch domain.
    '''
    session = get_session_context('fetch.disable')
    return await session.execute(cdp.fetch.disable())


async def enable(
        patterns: typing.Optional[typing.List[RequestPattern]] = None,
        handle_auth_requests: typing.Optional[bool] = None
    ) -> None:
    '''
    Enables issuing of requestPaused events. A request will be paused until client
    calls one of failRequest, fulfillRequest or continueRequest/continueWithAuth.

    :param patterns: *(Optional)* If specified, only requests matching any of these patterns will produce fetchRequested event and will be paused until clients response. If not set, all requests will be affected.
    :param handle_auth_requests: *(Optional)* If true, authRequired events will be issued and requests will be paused expecting a call to continueWithAuth.
    '''
    session = get_session_context('fetch.enable')
    return await session.execute(cdp.fetch.enable(patterns, handle_auth_requests))


async def fail_request(
        request_id: RequestId,
        error_reason: cdp.network.ErrorReason
    ) -> None:
    '''
    Causes the request to fail with specified reason.

    :param request_id: An id the client received in requestPaused event.
    :param error_reason: Causes the request to fail with the given reason.
    '''
    session = get_session_context('fetch.fail_request')
    return await session.execute(cdp.fetch.fail_request(request_id, error_reason))


async def fulfill_request(
        request_id: RequestId,
        response_code: int,
        response_headers: typing.List[HeaderEntry],
        body: typing.Optional[str] = None,
        response_phrase: typing.Optional[str] = None
    ) -> None:
    '''
    Provides response to the request.

    :param request_id: An id the client received in requestPaused event.
    :param response_code: An HTTP response code.
    :param response_headers: Response headers.
    :param body: *(Optional)* A response body.
    :param response_phrase: *(Optional)* A textual representation of responseCode. If absent, a standard phrase mathcing responseCode is used.
    '''
    session = get_session_context('fetch.fulfill_request')
    return await session.execute(cdp.fetch.fulfill_request(request_id, response_code, response_headers, body, response_phrase))


async def get_response_body(
        request_id: RequestId
    ) -> typing.Tuple[str, bool]:
    '''
    Causes the body of the response to be received from the server and
    returned as a single string. May only be issued for a request that
    is paused in the Response stage and is mutually exclusive with
    takeResponseBodyForInterceptionAsStream. Calling other methods that
    affect the request or disabling fetch domain before body is received
    results in an undefined behavior.

    :param request_id: Identifier for the intercepted request to get body for.
    :returns: A tuple with the following items:

        0. **body** – Response body.
        1. **base64Encoded** – True, if content was sent as base64.
    '''
    session = get_session_context('fetch.get_response_body')
    return await session.execute(cdp.fetch.get_response_body(request_id))


async def take_response_body_as_stream(
        request_id: RequestId
    ) -> cdp.io.StreamHandle:
    '''
    Returns a handle to the stream representing the response body.
    The request must be paused in the HeadersReceived stage.
    Note that after this command the request can't be continued
    as is -- client either needs to cancel it or to provide the
    response body.
    The stream only supports sequential read, IO.read will fail if the position
    is specified.
    This method is mutually exclusive with getResponseBody.
    Calling other methods that affect the request or disabling fetch
    domain before body is received results in an undefined behavior.

    :param request_id:
    :returns: 
    '''
    session = get_session_context('fetch.take_response_body_as_stream')
    return await session.execute(cdp.fetch.take_response_body_as_stream(request_id))
