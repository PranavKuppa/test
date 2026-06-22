import org.junit.Test
import org.junit.Assert.assertEquals

class ParserTest {
    @Test
    fun testParseConfigBasic() {
        val raw = "name=hello\nage=30"
        val result = parseConfig(raw)
        // BUG IN TEST: demands age be an Int, but parseConfig's contract
        // returns Map<String, String> for every caller - changing this
        // return type is an architectural change, not a healable bug.
        assertEquals(mapOf("name" to "hello", "age" to 30), result)
    }
}
