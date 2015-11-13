package lection2.module2;

import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.seleniumhq.selenium.fluent.FluentWebDriver;
import org.seleniumhq.selenium.fluent.Period;

import static com.codeborne.selenide.Selenide.*;
import static com.codeborne.selenide.Condition.*;

import static org.openqa.selenium.support.ui.ExpectedConditions.presenceOfElementLocated;

public class Sample3 {

    @Test
    public void testInObjectStyle() {
        WebDriver driver = new ChromeDriver();
        driver.get("http://selenium2.ru/");
        driver.findElement(By.name("searchword")).sendKeys("webdriver" + Keys.ENTER);
        WebElement result = new WebDriverWait(driver, 10).until(presenceOfElementLocated(By.cssSelector("div.searchintro")));
        Assert.assertEquals(result.getText(), "Результат поиска: найдено 53 объекта.");
        driver.quit();
    }

    @Test
    public void testInFluentStyle() {
        WebDriver driver = new ChromeDriver();
        driver.get("http://selenium2.ru/");
        FluentWebDriver fwd = new FluentWebDriver(driver);
        fwd.input(By.name("searchword"))
                .sendKeys("webdriver").sendKeys(Keys.ENTER);
        fwd.div(By.cssSelector("div.searchintro"))
                .within(Period.secs(10)).getText().shouldBe("Результат поиска: найдено 53 объекта.");
        driver.quit();
    }

    @Test
    public void testInProceduralStyle() {
        open("http://selenium2.ru/");
        $(By.name("searchword")).sendKeys("webdriver" + Keys.ENTER);
        $(By.cssSelector("div.searchintro")).should(appear)
                .should(have(text("Результат поиска: найдено 53 объекта.")));
    }

}
