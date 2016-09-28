import QtQuick 1.0
Rectangle{
	color: "gray"
	width:500
	height: 1000
	Grid {
		    id: grid
		    columns: 2
		    width: parent.width
		    height: parent.height

		    Text { text: "Number of puzzles: "; font.bold: true; font.pixelSize: 40}

		    TextInput {
		        id: numpuzzles
		        fillColor:"white"
		        color: "black"
		        text: "6"
		        width: parent.width-16; height: 40
		        focus: true
		        font.pixelSize: 40
	    	}

	    	Text { text: "Puzzles per page: "; font.bold: true; font.pixelSize: 40}

		    TextInput {
		        id: puzzlesperpage
		        fillColor:"white"
		        color: "black"
		        text: "6"
		        width: parent.width-16; height: 40
		        focus: true
		        font.pixelSize: 40
	    	}
		    Text { text: "words"; color: "red" }
		    Text { text: "in"; font.underline: true }
		    Text { text: "a"; font.pixelSize: 20 }
		    Text { text: "row"; font.strikeout: true }
	}
}