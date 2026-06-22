fun parseConfig(raw: String): Map<String, String> {
    val result = mutableMapOf<String, String>()
    raw.trim().split("\n").forEach { line ->
        if (line.contains("=")) {
            val (key, value) = line.split("=", limit = 2)
            result[key.trim()] = value.trim()
        }
    }
    return result
}
