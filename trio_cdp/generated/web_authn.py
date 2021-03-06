# DO NOT EDIT THIS FILE!
#
# This code is generated off of PyCDP modules. If you need to make
# changes, edit the generator and regenerate all of the modules.

from __future__ import annotations
import typing

from ..context import get_connection_context, get_session_context

import cdp.web_authn
from cdp.web_authn import (
    AuthenticatorId,
    AuthenticatorProtocol,
    AuthenticatorTransport,
    Credential,
    VirtualAuthenticatorOptions
)


async def add_credential(
        authenticator_id: AuthenticatorId,
        credential: Credential
    ) -> None:
    '''
    Adds the credential to the specified authenticator.

    :param authenticator_id:
    :param credential:
    '''
    session = get_session_context('web_authn.add_credential')
    return await session.execute(cdp.web_authn.add_credential(authenticator_id, credential))


async def add_virtual_authenticator(
        options: VirtualAuthenticatorOptions
    ) -> AuthenticatorId:
    '''
    Creates and adds a virtual authenticator.

    :param options:
    :returns: 
    '''
    session = get_session_context('web_authn.add_virtual_authenticator')
    return await session.execute(cdp.web_authn.add_virtual_authenticator(options))


async def clear_credentials(
        authenticator_id: AuthenticatorId
    ) -> None:
    '''
    Clears all the credentials from the specified device.

    :param authenticator_id:
    '''
    session = get_session_context('web_authn.clear_credentials')
    return await session.execute(cdp.web_authn.clear_credentials(authenticator_id))


async def disable() -> None:
    '''
    Disable the WebAuthn domain.
    '''
    session = get_session_context('web_authn.disable')
    return await session.execute(cdp.web_authn.disable())


async def enable() -> None:
    '''
    Enable the WebAuthn domain and start intercepting credential storage and
    retrieval with a virtual authenticator.
    '''
    session = get_session_context('web_authn.enable')
    return await session.execute(cdp.web_authn.enable())


async def get_credentials(
        authenticator_id: AuthenticatorId
    ) -> typing.List[Credential]:
    '''
    Returns all the credentials stored in the given virtual authenticator.

    :param authenticator_id:
    :returns: 
    '''
    session = get_session_context('web_authn.get_credentials')
    return await session.execute(cdp.web_authn.get_credentials(authenticator_id))


async def remove_virtual_authenticator(
        authenticator_id: AuthenticatorId
    ) -> None:
    '''
    Removes the given authenticator.

    :param authenticator_id:
    '''
    session = get_session_context('web_authn.remove_virtual_authenticator')
    return await session.execute(cdp.web_authn.remove_virtual_authenticator(authenticator_id))


async def set_user_verified(
        authenticator_id: AuthenticatorId,
        is_user_verified: bool
    ) -> None:
    '''
    Sets whether User Verification succeeds or fails for an authenticator.
    The default is true.

    :param authenticator_id:
    :param is_user_verified:
    '''
    session = get_session_context('web_authn.set_user_verified')
    return await session.execute(cdp.web_authn.set_user_verified(authenticator_id, is_user_verified))
