# DO NOT EDIT THIS FILE!
#
# This code is generated off of PyCDP modules. If you need to make
# changes, edit the generator and regenerate all of the modules.

from __future__ import annotations
import typing

from ..context import get_connection_context, get_session_context

import cdp.overlay
from cdp.overlay import (
    HighlightConfig,
    InspectMode,
    InspectModeCanceled,
    InspectNodeRequested,
    NodeHighlightRequested,
    ScreenshotRequested
)


async def disable() -> None:
    '''
    Disables domain notifications.
    '''
    session = get_session_context('overlay.disable')
    return await session.execute(cdp.overlay.disable())


async def enable() -> None:
    '''
    Enables domain notifications.
    '''
    session = get_session_context('overlay.enable')
    return await session.execute(cdp.overlay.enable())


async def get_highlight_object_for_test(
        node_id: cdp.dom.NodeId,
        include_distance: typing.Optional[bool] = None,
        include_style: typing.Optional[bool] = None
    ) -> dict:
    '''
    For testing.

    :param node_id: Id of the node to get highlight object for.
    :param include_distance: *(Optional)* Whether to include distance info.
    :param include_style: *(Optional)* Whether to include style info.
    :returns: Highlight data for the node.
    '''
    session = get_session_context('overlay.get_highlight_object_for_test')
    return await session.execute(cdp.overlay.get_highlight_object_for_test(node_id, include_distance, include_style))


async def hide_highlight() -> None:
    '''
    Hides any highlight.
    '''
    session = get_session_context('overlay.hide_highlight')
    return await session.execute(cdp.overlay.hide_highlight())


async def highlight_frame(
        frame_id: cdp.page.FrameId,
        content_color: typing.Optional[cdp.dom.RGBA] = None,
        content_outline_color: typing.Optional[cdp.dom.RGBA] = None
    ) -> None:
    '''
    Highlights owner element of the frame with given id.

    :param frame_id: Identifier of the frame to highlight.
    :param content_color: *(Optional)* The content box highlight fill color (default: transparent).
    :param content_outline_color: *(Optional)* The content box highlight outline color (default: transparent).
    '''
    session = get_session_context('overlay.highlight_frame')
    return await session.execute(cdp.overlay.highlight_frame(frame_id, content_color, content_outline_color))


async def highlight_node(
        highlight_config: HighlightConfig,
        node_id: typing.Optional[cdp.dom.NodeId] = None,
        backend_node_id: typing.Optional[cdp.dom.BackendNodeId] = None,
        object_id: typing.Optional[cdp.runtime.RemoteObjectId] = None,
        selector: typing.Optional[str] = None
    ) -> None:
    '''
    Highlights DOM node with given id or with the given JavaScript object wrapper. Either nodeId or
    objectId must be specified.

    :param highlight_config: A descriptor for the highlight appearance.
    :param node_id: *(Optional)* Identifier of the node to highlight.
    :param backend_node_id: *(Optional)* Identifier of the backend node to highlight.
    :param object_id: *(Optional)* JavaScript object id of the node to be highlighted.
    :param selector: *(Optional)* Selectors to highlight relevant nodes.
    '''
    session = get_session_context('overlay.highlight_node')
    return await session.execute(cdp.overlay.highlight_node(highlight_config, node_id, backend_node_id, object_id, selector))


async def highlight_quad(
        quad: cdp.dom.Quad,
        color: typing.Optional[cdp.dom.RGBA] = None,
        outline_color: typing.Optional[cdp.dom.RGBA] = None
    ) -> None:
    '''
    Highlights given quad. Coordinates are absolute with respect to the main frame viewport.

    :param quad: Quad to highlight
    :param color: *(Optional)* The highlight fill color (default: transparent).
    :param outline_color: *(Optional)* The highlight outline color (default: transparent).
    '''
    session = get_session_context('overlay.highlight_quad')
    return await session.execute(cdp.overlay.highlight_quad(quad, color, outline_color))


async def highlight_rect(
        x: int,
        y: int,
        width: int,
        height: int,
        color: typing.Optional[cdp.dom.RGBA] = None,
        outline_color: typing.Optional[cdp.dom.RGBA] = None
    ) -> None:
    '''
    Highlights given rectangle. Coordinates are absolute with respect to the main frame viewport.

    :param x: X coordinate
    :param y: Y coordinate
    :param width: Rectangle width
    :param height: Rectangle height
    :param color: *(Optional)* The highlight fill color (default: transparent).
    :param outline_color: *(Optional)* The highlight outline color (default: transparent).
    '''
    session = get_session_context('overlay.highlight_rect')
    return await session.execute(cdp.overlay.highlight_rect(x, y, width, height, color, outline_color))


async def set_inspect_mode(
        mode: InspectMode,
        highlight_config: typing.Optional[HighlightConfig] = None
    ) -> None:
    '''
    Enters the 'inspect' mode. In this mode, elements that user is hovering over are highlighted.
    Backend then generates 'inspectNodeRequested' event upon element selection.

    :param mode: Set an inspection mode.
    :param highlight_config: *(Optional)* A descriptor for the highlight appearance of hovered-over nodes. May be omitted if ```enabled == false```.
    '''
    session = get_session_context('overlay.set_inspect_mode')
    return await session.execute(cdp.overlay.set_inspect_mode(mode, highlight_config))


async def set_paused_in_debugger_message(
        message: typing.Optional[str] = None
    ) -> None:
    '''
    :param message: *(Optional)* The message to display, also triggers resume and step over controls.
    '''
    session = get_session_context('overlay.set_paused_in_debugger_message')
    return await session.execute(cdp.overlay.set_paused_in_debugger_message(message))


async def set_show_ad_highlights(
        show: bool
    ) -> None:
    '''
    Highlights owner element of all frames detected to be ads.

    :param show: True for showing ad highlights
    '''
    session = get_session_context('overlay.set_show_ad_highlights')
    return await session.execute(cdp.overlay.set_show_ad_highlights(show))


async def set_show_debug_borders(
        show: bool
    ) -> None:
    '''
    Requests that backend shows debug borders on layers

    :param show: True for showing debug borders
    '''
    session = get_session_context('overlay.set_show_debug_borders')
    return await session.execute(cdp.overlay.set_show_debug_borders(show))


async def set_show_fps_counter(
        show: bool
    ) -> None:
    '''
    Requests that backend shows the FPS counter

    :param show: True for showing the FPS counter
    '''
    session = get_session_context('overlay.set_show_fps_counter')
    return await session.execute(cdp.overlay.set_show_fps_counter(show))


async def set_show_hit_test_borders(
        show: bool
    ) -> None:
    '''
    Requests that backend shows hit-test borders on layers

    :param show: True for showing hit-test borders
    '''
    session = get_session_context('overlay.set_show_hit_test_borders')
    return await session.execute(cdp.overlay.set_show_hit_test_borders(show))


async def set_show_layout_shift_regions(
        result: bool
    ) -> None:
    '''
    Requests that backend shows layout shift regions

    :param result: True for showing layout shift regions
    '''
    session = get_session_context('overlay.set_show_layout_shift_regions')
    return await session.execute(cdp.overlay.set_show_layout_shift_regions(result))


async def set_show_paint_rects(
        result: bool
    ) -> None:
    '''
    Requests that backend shows paint rectangles

    :param result: True for showing paint rectangles
    '''
    session = get_session_context('overlay.set_show_paint_rects')
    return await session.execute(cdp.overlay.set_show_paint_rects(result))


async def set_show_scroll_bottleneck_rects(
        show: bool
    ) -> None:
    '''
    Requests that backend shows scroll bottleneck rects

    :param show: True for showing scroll bottleneck rects
    '''
    session = get_session_context('overlay.set_show_scroll_bottleneck_rects')
    return await session.execute(cdp.overlay.set_show_scroll_bottleneck_rects(show))


async def set_show_viewport_size_on_resize(
        show: bool
    ) -> None:
    '''
    Paints viewport size upon main frame resize.

    :param show: Whether to paint size or not.
    '''
    session = get_session_context('overlay.set_show_viewport_size_on_resize')
    return await session.execute(cdp.overlay.set_show_viewport_size_on_resize(show))
