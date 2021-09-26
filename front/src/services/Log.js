import {timer} from "rxjs";
import {filter, map} from "rxjs/operators";

class LogService {
    getLogStream(context) {
        //TODO
        console.info("Get log stream " + context)
        return timer(1000, 100)
            .pipe(
                map(counter => {
                    return {
                        index: counter,
                        text: mockData.logs.split("\n")[counter]
                    }
                }),
                filter(log => !!log.text)
            )
    }
}

const mockData = {
    logs: "Jun 29, 2008 11:16:20 AM org.apache.catalina.core.ApplicationContext log\n" +
        "INFO: ContextListener: contextInitialized()\n" +
        "Jun 29, 2008 11:16:20 AM org.apache.catalina.core.ApplicationContext log\n" +
        "INFO: SessionListener: contextInitialized()\n" +
        "Jun 29, 2008 11:22:43 AM org.apache.catalina.core.StandardWrapperValve invoke\n" +
        "SEVERE: Servlet.service() for servlet jsp threw exception\n" +
        "org.apache.jasper.JasperException: /testmysql.jsp(3,4) Invalid directive\n" +
        "\tat org.apache.jasper.compiler.DefaultErrorHandler.jspError(DefaultErrorHandler.java:40)\n" +
        "\tat org.apache.jasper.compiler.ErrorDispatcher.dispatch(ErrorDispatcher.java:407)\n" +
        "\tat org.apache.jasper.compiler.ErrorDispatcher.jspError(ErrorDispatcher.java:88)\n" +
        "\tat org.apache.jasper.compiler.Parser.parseDirective(Parser.java:506)\n" +
        "\tat org.apache.jasper.compiler.Parser.parseElements(Parser.java:1433)\n" +
        "\tat org.apache.jasper.compiler.Parser.parse(Parser.java:133)\n" +
        "\tat org.apache.jasper.compiler.ParserController.doParse(ParserController.java:216)\n" +
        "\tat org.apache.jasper.compiler.ParserController.parse(ParserController.java:103)\n" +
        "\tat org.apache.jasper.compiler.Compiler.generateJava(Compiler.java:153)\n" +
        "\tat org.apache.jasper.compiler.Compiler.compile(Compiler.java:314)\n" +
        "\tat org.apache.jasper.compiler.Compiler.compile(Compiler.java:294)\n" +
        "\tat org.apache.jasper.compiler.Compiler.compile(Compiler.java:281)\n" +
        "\tat org.apache.jasper.JspCompilationContext.compile(JspCompilationContext.java:566)\n" +
        "\tat org.apache.jasper.servlet.JspServletWrapper.service(JspServletWrapper.java:317)\n" +
        "\tat org.apache.jasper.servlet.JspServlet.serviceJspFile(JspServlet.java:337)\n" +
        "\tat org.apache.jasper.servlet.JspServlet.service(JspServlet.java:266)\n" +
        "\tat javax.servlet.http.HttpServlet.service(HttpServlet.java:803)\n" +
        "\tat org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:290)\n" +
        "\tat org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:206)\n" +
        "\tat org.apache.catalina.core.StandardWrapperValve.invoke(StandardWrapperValve.java:233)\n" +
        "\tat org.apache.catalina.core.StandardContextValve.invoke(StandardContextValve.java:175)\n" +
        "\tat org.apache.catalina.core.StandardHostValve.invoke(StandardHostValve.java:128)\n" +
        "\tat org.apache.catalina.valves.ErrorReportValve.invoke(ErrorReportValve.java:102)\n" +
        "\tat org.apache.catalina.core.StandardEngineValve.invoke(StandardEngineValve.java:109)\n" +
        "\tat org.apache.catalina.connector.CoyoteAdapter.service(CoyoteAdapter.java:286)\n" +
        "\tat org.apache.coyote.http11.Http11Processor.process(Http11Processor.java:844)\n" +
        "\tat org.apache.coyote.http11.Http11Protocol$Http11ConnectionHandler.process(Http11Protocol.java:583)\n" +
        "\tat org.apache.tomcat.util.net.JIoEndpoint$Worker.run(JIoEndpoint.java:447)\n" +
        "\tat java.lang.Thread.run(Thread.java:619)\n" +
        "Jun 29, 2008 11:23:02 AM org.apache.catalina.core.StandardWrapperValve invoke\n" +
        "SEVERE: Servlet.service() for servlet jsp threw exception\n" +
        "org.apache.jasper.JasperException: Unable to compile class for JSP: \n" +
        "\n" +
        "An error occurred at line: 13 in the jsp file: /testmysql.jsp\n" +
        "Syntax error, insert \"AssignmentOperator Expression\" to complete Assignment\n" +
        "10: Connection dbconn;\n" +
        "11: ResultSet results;\n" +
        "12: PreparedStatement sql;\n" +
        "13: TRY\n" +
        "14: {\n" +
        "15: \tClass.forname(\"com.mysql.jdbc.Driver\").newInstance();\n" +
        "16: \tTRY\n" +
        "\n" +
        "\n" +
        "An error occurred at line: 13 in the jsp file: /testmysql.jsp\n" +
        "Syntax error, insert \";\" to complete Statement\n" +
        "10: Connection dbconn;\n" +
        "11: ResultSet results;\n" +
        "12: PreparedStatement sql;\n" +
        "13: TRY\n" +
        "14: {\n" +
        "15: \tClass.forname(\"com.mysql.jdbc.Driver\").newInstance();\n" +
        "16: \tTRY\n" +
        "\n" +
        "\n" +
        "An error occurred at line: 13 in the jsp file: /testmysql.jsp\n" +
        "TRY cannot be resolved\n" +
        "10: Connection dbconn;\n" +
        "11: ResultSet results;\n" +
        "12: PreparedStatement sql;\n" +
        "13: TRY\n" +
        "14: {\n" +
        "15: \tClass.forname(\"com.mysql.jdbc.Driver\").newInstance();\n" +
        "16: \tTRY\n" +
        "\n" +
        "\n" +
        "An error occurred at line: 15 in the jsp file: /testmysql.jsp\n" +
        "The method forname(String) is undefined for the type Class\n" +
        "12: PreparedStatement sql;\n" +
        "13: TRY\n" +
        "14: {\n" +
        "15: \tClass.forname(\"com.mysql.jdbc.Driver\").newInstance();\n" +
        "16: \tTRY\n" +
        "17: \t{\n" +
        "18: \t\tdbconn = DriverManager.getConnection(\"jdbc:mysql://localhost/visitor\",\"\",\"\");\n" +
        "\n" +
        "\n" +
        "An error occurred at line: 16 in the jsp file: /testmysql.jsp\n" +
        "Syntax error, insert \"AssignmentOperator Expression\" to complete Assignment\n" +
        "13: TRY\n" +
        "14: {\n" +
        "15: \tClass.forname(\"com.mysql.jdbc.Driver\").newInstance();\n" +
        "16: \tTRY\n" +
        "17: \t{\n" +
        "18: \t\tdbconn = DriverManager.getConnection(\"jdbc:mysql://localhost/visitor\",\"\",\"\");\n" +
        "19: \t\tuid = request.getParameter(\"userid\");\n"
}

export default new LogService()
