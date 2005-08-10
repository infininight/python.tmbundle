# encoding: latin-1

# copyright (c) Domenico Carbotta, 2005
# with enhancements by Brad Miller
# this script is released under the GNU General Public License


preface = '''
    <html>
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
    <title>PyMate</title>
    <style type="text/css">
    <!--
    body {
    	font-family: "Lucida Grande";
    	font-size: 10pt;
    	background-color: rgb(170, 200, 255);
    	margin: 0;
    	height: 100%%;
    }
    p {
    	margin: 0;
    	padding: 2px 0 2px 0;
    }
    p#version {
    	font-size: 10pt;
    	font-weight: bold;
    	color: #005C3E;
    }
    div {
    	border-style: dotted;
    	border-width: 1px 0;
    	border-color: #666;
    	margin: 10px 0;
    	padding: 10px
    }
    div#script_output {
    	background-color: rgb(230, 240, 255);
    }
    pre {
    	padding: 0;
    	margin: 0;
    	line-height: 1.5;
    	font-family: Monaco;
    	font-size: 8pt;
    }
    pre strong {
    	/* used for messages */
    	font-weight: normal;
    	color: #0000CC;
    }
    pre em {
    	/* used for stderr */
    	font-style: normal;
    	color: #FF5600;
    }
    div#exception_report {
    	background-color: rgb(210, 220, 255);
    }
    p#exception strong {
    	color: #FF5600;
    }
    p#traceback {
    	font-size: 8pt;
    }
    table {
    	margin: 0;
    	padding: 0;
    }
    td {
    	margin: 0;
    	padding: 2px 2px 2px 5px;
    	font-size: 10pt;
    }
    a {
    	color: #FF5600;
    }
    -->
    </style>
    </head>
    <body>
    <div id="script_output">
    <pre><strong>%s</strong>
<strong>&gt;&gt;&gt %s</strong>
''' # % (version, short_filename)

exception_preface = '''</pre></div>
<div id="exception_report">
<p id="exception"><strong>%s</strong>%s</p>
<p id="traceback">Traceback:</p>
<blockquote><table border="0" cellspacing="0" cellpadding="0">
''' # % (exception_name, exception_arguments)

traceback_item = '''
    <tr>
        <td width="30%%">function
            <a href="txmt://open?url=file://%s&line=%d">%s</a></td>
        <td width="70%%">in <strong>%s</strong> at line %d</td>
    </tr>
''' # % (filename, lineno, func_name, short_filename, lineno)

exception_end = '''</table>
</blockquote>
</div>
</body>
</html>
'''

syntax_preface = '''</pre></div>
<div id="exception_report">
<p id="exception"><strong>%s</strong>%s</p>
''' # % (exception_name, exception_arguments)

syntax_item = '''
    <tr>
        <td width="40%%">SyntaxError
            <a href="txmt://open?url=file://%s&line=%d">%s</a></td>
        <td width="70%%">at line %d line: <strong>%s</strong></td>
    </tr>
''' # % (filename, lineno, func_name, lineno, short_filename)

syntax_end = '''
</div>
</body>
</html>
'''

normal_end = '''</pre>
</div>
</body>
</html>
'''