import unittest
from HomePageTests.CarouselTest import TestCarousel
from HomePageTests.ProductsTest import TestProducts
from ProductPageTests.CatalogTest import TestCatalog
from ProductPageTests.ProductBuyTest import TestProductBuy
from UserTests.ProfileTest import TestProfile
from UserTests.Registration import TestRegistration
from UserTests.SignInTest import TestSignIn
from CartTest import TestCart
from NavbarTest import TestNavbar


def runTests(testClasses):
    loader = unittest.TestLoader()
    suitesList = []
    for testClass in testClasses:
        suite = loader.loadTestsFromTestCase(testClass)
        suitesList.append(suite)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(unittest.TestSuite(suitesList))

def main():
    runTests([TestCarousel, TestProducts])
    runTests([TestNavbar])
    runTests([TestCatalog, TestProductBuy])
    runTests([TestCart])
    runTests([TestProfile, TestRegistration, TestSignIn])

if __name__ == '__main__':
    main()
