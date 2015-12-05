package lesson2.module3;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.WebDriverWait;

import static org.openqa.selenium.support.ui.ExpectedConditions.presenceOfElementLocated;

public class Sample1 {

    private WebDriver driver;

    @Before
    public void initDriver() {
        driver = new ChromeDriver();
    }
    
    @Test
    public void testCase() {
        driver.get("http://selenium2.ru/");
        driver.findElement(By.name("searchword")).sendKeys("webdriver" + Keys.ENTER);
        new WebDriverWait(driver, 10).until(presenceOfElementLocated(By.cssSelector("div.searchintro")));
    }

    @After
    public void stopDriver() {
        driver.quit();
    }

}
