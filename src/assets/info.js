


var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};


dagcomponentfuncs.CustomTooltip = function (props) {
    
    if (props.rowIndex === undefined) {
    return React.createElement('div',{},[React.createElement(
        window.dash_bootstrap_components.Tooltip,
        {
            target: `ticker_${props.value}`,
            placement: 'bottom'
        },
        props.value
    ),
    React.createElement(
        "div",
        {
            id: `ticker_${props.value}`,
        },
        props.value
    )])
};
};