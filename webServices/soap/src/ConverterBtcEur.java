import javax.jws.WebService;
import java.util.ArrayList;

@WebService(targetNamespace = "http://www.converter.com")
public class ConverterBtcEur {

    static ArrayList<Trader> database = new ArrayList<>();

    //bitcoin price in euros
    static double btcPrice = 82000.00;

    //convert the amount in euros given into btc
    public double convertEurToBtc(double eurAmount){
        return btcPrice / eurAmount;
    }

    //convert the amount in btc given into euros
    public double convertBtcToEur(double btcAmount){
        return btcAmount * btcPrice;
    }

    public Trader getTrader(int index){
        return database.get(index);
    }

}
