using System;
using OpenQA.Selenium;
using OpenQA.Selenium.Remote;
using OpenQA.Selenium.Firefox;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.IE;
using OpenQA.Selenium.Support.UI;
using System;
using System.Collections.Generic;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace testautomation_dotnet
{
    [TestClass]
    public class UnitTest1
    {
        private IWebDriver driver;

        [TestInitialize]
        public void LoginWithValidCredentials()
        {
            driver = new FirefoxDriver();
            driver.Url = "http://localhost/php4dvd";
            driver.FindElement(By.Name("username")).SendKeys("admin");
            driver.FindElement(By.Name("password")).SendKeys("admin");
            driver.FindElement(By.CssSelector("input[type=submit]")).Click();
        }

        [TestMethod]
        public void FoundSomething()
        {
            driver.FindElement(By.Id("q")).Click();
            driver.FindElement(By.Id("q")).Clear();
            driver.FindElement(By.Id("q")).SendKeys("father");
            driver.FindElement(By.Id("q")).SendKeys(Keys.Enter);

            IList<IWebElement> list = driver.FindElements(By.CssSelector("movie_box > .title"));
            var foundFilm = new List<IWebElement>();

            if (driver.FindElement(By.CssSelector("div[id^=movie_]")).Displayed)
            {
                foreach (var film in list)
                {
                    film.Text.Contains("father");
                    foundFilm.Add(film);
                }

                var countFoundFilm = foundFilm.Count;
                Assert.IsTrue(list.Count.Equals(countFoundFilm));
            }

        }
    }
}
