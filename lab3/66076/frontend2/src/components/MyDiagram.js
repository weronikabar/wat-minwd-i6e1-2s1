import React from 'react';

import go from 'gojs';
import { DiagramModel, LinkModel, GojsDiagram, ModelChangeEvent } from 'react-gojs';
import  '../MyDiagram.css'
import { Diagram, ToolManager } from 'gojs';

class MyDiagram extends  React.Component {

    constructor(props) {
        super(props);
        this.createDiagram = this.createDiagram.bind(this);
    }
    createDiagram(diagramId) {
        const $ = go.GraphObject.make;

        const myDiagram = $(go.Diagram, diagramId, {
            initialContentAlignment: go.Spot.LeftCenter,
            layout: $(go.TreeLayout, {
                angle: 0,
                arrangement: go.TreeLayout.ArrangementVertical,
                treeStyle: go.TreeLayout.StyleLayered
            }),
            isReadOnly: false,
            allowHorizontalScroll: true,
            allowVerticalScroll: true,
            allowZoom: false,
            allowSelect: true,
            autoScale: Diagram.Uniform,
            contentAlignment: go.Spot.LeftCenter,
            TextEdited: this.onTextEdited
        });

        myDiagram.toolManager.panningTool.isEnabled = false;
        myDiagram.toolManager.mouseWheelBehavior = ToolManager.WheelScroll;

        myDiagram.nodeTemplate = $(
            go.Node,
            'Auto',
            {
                selectionChanged: node => this.props.onNodeSelection(node.key, node.isSelected)
            },
            $(go.Shape, 'RoundedRectangle', { strokeWidth: 0 }, new go.Binding('fill', 'color')),
            $(go.TextBlock, { margin: 8, editable: true }, new go.Binding('text', 'label'))
        );

        return myDiagram;
    }

    getModel = () => {
        return {
            nodeDataArray: [
                {key: 'Alpha', color: 'lightblue'},
                {key: 'Beta', color: 'orange'},
                {key: 'Gamma', color: 'lightgreen'},
                {key: 'Delta', color: 'pink'},
                {key: 'Omega', color: 'grey'}
            ],
            linkDataArray: [
                {from: 'Alpha', to: 'Beta'},
                {from: 'Alpha', to: 'Gamma'},
                {from: 'Beta', to: 'Delta'},
                {from: 'Gamma', to: 'Omega'}
            ]
        }
    }

    render() {
        return (
            <>
                <h5>My diagram: </h5>
                <GojsDiagram
                    diagramId="myDiagramDiv"
                    model={this.getModel()}
                    createDiagram={this.createDiagram}
                    className="myDiagram"
                />
                </>
        )
    }
}
export default MyDiagram;