fun add(a: Int, b: Int): Int {
    return a - b // BUG: should be a + b
}

fun main() {
    println(add(2, 3))
}
