import org.junit.Test
import org.junit.Assert.assertEquals

class CalcTest {
    @Test
    fun testAdd() {
        assertEquals(5, add(2, 3)) // FAILS due to bug in Calc.kt
    }
}
