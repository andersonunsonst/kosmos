# Native Module, Import : re, regex
import re

# Name Class : CrositeScript
class CrositeScript:

    # Class Method : m_get
    def m_get(v_response, v_uri):

        # Regex Condition - exist if check
        if re.search(
            r"FSCommand|onAbort|onActivate|onAfterPrint|onAfterUpdate|onBeforeActivate|"
            r"onBeforeCopy|onBeforeCut|onBeforeDeactivate|onBeforeEditFocus|onBeforePaste|"
            r"onBeforePrint|onBeforeUnload|onBeforeUpdate|onBegin|onBlur|onBounce|onCellChange|"
            r"onChange|onClick|onContextMenu|onControlSelect|onCopy|onCut|onDataAvailable|"
            r"onDataSetChanged|onDataSetComplete|onDblClick|onDeactivate|onDrag|onDragEnd|"
            r"onDragLeave|onDragEnter|onDragOver|onDragDrop|onDragStart|onDrop|onEnd|onError|"
            r"onErrorUpdate|onFilterChange|onFinish|onFocus|onFocusIn|onFocusOut|onHashChange|"
            r"onHelp|onInput|onKeyDown|onKeyPress|onKeyUp|onLayoutComplete|onLoad|onLoseCapture|"
            r"onMediaComplete|onMediaError|onMessage|onMouseDown|onMouseEnter|onMouseLeave|"
            r"onMouseMove|onMouseOut|onMouseOver|onMouseUp|onMouseWheel|onMove|onMoveEnd|onMoveStart|"
            r"onOffline|onOnline|onOutOfSync|onPaste|onPause|onPopState|onProgress|onPropertyChange|"
            r"onReadyStateChange|onRedo|onRepeat|onReset|onResize|onResizeEnd|onResizeStart|onResume|"
            r"onReverse|onRowsEnter|onRowExit|onRowDelete|onRowInserted|onScroll|onSeek|onSelect|"
            r"onSelectionChange|onSelectStart|onStart|onStop|onStorage|onSyncRestored|onSubmit|onTimeError|"
            r"onTrackChange|onUndo|onUnload|onURLFlip|seekSegmentTime|bgsound|xss|rocks|noxss|"
            r"<script>|</script>|script|livescript|vbscript|alert|[(]|[)]|>|<|;|&#|[*]|`",
            v_uri, re.IGNORECASE
        ):
            # Variable : obtem status de resposta para client browser :
            status = "400 Bad Request"
            # Variable : obtem cabeçalho http para o browser do client
            headers = [("Content-type", "application/json; charset=utf-8")]
            # Function : Envio de variable para o client browser :
            v_response(status, headers)
            # Output :
            return "Hacker Attempt: True, Threat : Cross-Site Scripting, Syntax: " + v_uri

        else: # return "Hancking: False, Threat : Not Found, Syntax: No threats detected in the string : " + v_uri
            # Custom Module, Import : sqlinjection
            from cern.safe.sqlinjection import SqlInjection
            # Module Access, return : SqlInjection
            return SqlInjection.m_get(v_response, v_uri)

    def m_post(v_response, v_uri, v_inp):

        # Regex Condition - exist if check
        if re.search(
            r"FSCommand|onAbort|onActivate|onAfterPrint|onAfterUpdate|onBeforeActivate|"
            r"onBeforeCopy|onBeforeCut|onBeforeDeactivate|onBeforeEditFocus|onBeforePaste|"
            r"onBeforePrint|onBeforeUnload|onBeforeUpdate|onBegin|onBlur|onBounce|onCellChange|"
            r"onChange|onClick|onContextMenu|onControlSelect|onCopy|onCut|onDataAvailable|"
            r"onDataSetChanged|onDataSetComplete|onDblClick|onDeactivate|onDrag|onDragEnd|"
            r"onDragLeave|onDragEnter|onDragOver|onDragDrop|onDragStart|onDrop|onEnd|onError|"
            r"onErrorUpdate|onFilterChange|onFinish|onFocus|onFocusIn|onFocusOut|onHashChange|"
            r"onHelp|onInput|onKeyDown|onKeyPress|onKeyUp|onLayoutComplete|onLoad|onLoseCapture|"
            r"onMediaComplete|onMediaError|onMessage|onMouseDown|onMouseEnter|onMouseLeave|"
            r"onMouseMove|onMouseOut|onMouseOver|onMouseUp|onMouseWheel|onMove|onMoveEnd|onMoveStart|"
            r"onOffline|onOnline|onOutOfSync|onPaste|onPause|onPopState|onProgress|onPropertyChange|"
            r"onReadyStateChange|onRedo|onRepeat|onReset|onResize|onResizeEnd|onResizeStart|onResume|"
            r"onReverse|onRowsEnter|onRowExit|onRowDelete|onRowInserted|onScroll|onSeek|onSelect|"
            r"onSelectionChange|onSelectStart|onStart|onStop|onStorage|onSyncRestored|onSubmit|onTimeError|"
            r"onTrackChange|onUndo|onUnload|onURLFlip|seekSegmentTime|bgsound|xss|rocks|noxss|"
            r"<script>|</script>|script|livescript|vbscript|alert|[(]|[)]|>|<|;|&#|[*]|`",
            v_uri, re.IGNORECASE
        ):
            # Variable : obtem status de resposta para client browser :
            status = "400 Bad Request"
            # Variable : obtem cabeçalho http para o browser do client
            headers = [("Content-type", "application/json; charset=utf-8")]
            # Function : Envio de variable para o client browser :
            v_response(status, headers)
            # Output :
            return "Hacker Attempt: True, Threat : Cross-Site Scripting, Syntax: " + v_uri

        else:
            # Regex Condition - exist if check
            if re.search(
                r"FSCommand|onAbort|onActivate|onAfterPrint|onAfterUpdate|onBeforeActivate|"
                r"onBeforeCopy|onBeforeCut|onBeforeDeactivate|onBeforeEditFocus|onBeforePaste|"
                r"onBeforePrint|onBeforeUnload|onBeforeUpdate|onBegin|onBlur|onBounce|onCellChange|"
                r"onChange|onClick|onContextMenu|onControlSelect|onCopy|onCut|onDataAvailable|"
                r"onDataSetChanged|onDataSetComplete|onDblClick|onDeactivate|onDrag|onDragEnd|"
                r"onDragLeave|onDragEnter|onDragOver|onDragDrop|onDragStart|onDrop|onEnd|onError|"
                r"onErrorUpdate|onFilterChange|onFinish|onFocus|onFocusIn|onFocusOut|onHashChange|"
                r"onHelp|onInput|onKeyDown|onKeyPress|onKeyUp|onLayoutComplete|onLoad|onLoseCapture|"
                r"onMediaComplete|onMediaError|onMessage|onMouseDown|onMouseEnter|onMouseLeave|"
                r"onMouseMove|onMouseOut|onMouseOver|onMouseUp|onMouseWheel|onMove|onMoveEnd|onMoveStart|"
                r"onOffline|onOnline|onOutOfSync|onPaste|onPause|onPopState|onProgress|onPropertyChange|"
                r"onReadyStateChange|onRedo|onRepeat|onReset|onResize|onResizeEnd|onResizeStart|onResume|"
                r"onReverse|onRowsEnter|onRowExit|onRowDelete|onRowInserted|onScroll|onSeek|onSelect|"
                r"onSelectionChange|onSelectStart|onStart|onStop|onStorage|onSyncRestored|onSubmit|onTimeError|"
                r"onTrackChange|onUndo|onUnload|onURLFlip|seekSegmentTime|bgsound|xss|rocks|noxss|"
                r"<script>|</script>|script|livescript|vbscript|alert|[(]|[)]|>|<|;|&#|[*]|`",
                v_inp, re.IGNORECASE
            ):
                # Variable : obtem status de resposta para client browser :
                status = "400 Bad Request"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/json; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output :
                return "Hacker Attempt: True, Threat : Cross-Site Scripting, Syntax: " + v_inp

            else:
                # Custom Module, Import : sqlinjection
                from cern.safe.sqlinjection import SqlInjection
                # Module Access, return : SqlInjection
                return SqlInjection.m_post(v_response, v_uri, v_inp)