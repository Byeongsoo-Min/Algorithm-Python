func solution(_ n:Int) -> Int {
    var nums = Set<Int>()
    if n == 0 {
        return 0
    }
    for i in (1...n){
        if n % i == 0{
            nums.insert(i)
            nums.insert(n / i)
        }
    }
    return nums.reduce(0, +)
}