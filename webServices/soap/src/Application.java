import javax.xml.ws.Endpoint;

public class Application {
    public static void main(String[] args){
        System.out.println("First run test");
        String url = "http://127.0.0.1:5006/";
        Endpoint.publish(url, new ConverterBtcEur());
        System.out.println("Converter service has been deployed");
    }
}
