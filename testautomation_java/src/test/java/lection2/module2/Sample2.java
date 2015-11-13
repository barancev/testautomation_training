package lection2.module2;

import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import ru.stqa.selenium.wrapper.LoggingWrapper;
import static org.openqa.selenium.support.ui.ExpectedConditions.*;

public class Sample2 {

    @Test
    public void testWithoutLogging() {
        performScenario(new ChromeDriver());
    }

    @Test
    public void testWithLogging() {
        performScenario(new LoggingWrapper(new ChromeDriver()).getDriver());
    }

    private static void performScenario(WebDriver driver) {
        driver.get("http://selenium2.ru/");
        driver.findElement(By.name("searchword")).sendKeys("webdriver" + Keys.ENTER);
        new WebDriverWait(driver, 10).until(presenceOfElementLocated(By.cssSelector("div.searchintro")));
        driver.quit();
    }

}
