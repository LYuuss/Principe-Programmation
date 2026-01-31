import javax.xml.bind.annotation.XmlRootElement;
import java.io.Serializable;

@XmlRootElement
public class Trader implements Serializable {
    //trader's amount of eur
    private double eurSpot;

    //trader's amount of btc
    private double btcSpot;

    public Trader(double eurSpot, double btcSpot){
        this.eurSpot = eurSpot;
        this.btcSpot = btcSpot;
    }

    public Trader(){

    }

    //getters
    public double getEurSpot() {
        return this.eurSpot;
    }

    public double getBtcSpot() {
        return btcSpot;
    }
    //setters
    public void setEurSpot(double eurSpot){
        this.eurSpot = eurSpot;
    }

    public void setBtcSpot(double btcSpot) {
        this.btcSpot = btcSpot;
    }
}
