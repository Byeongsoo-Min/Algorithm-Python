import Foundation

func solution(_ n: Int) -> Int {
    var answer: Int = 0
    var deci: Double = 1.0
    var num: Double = Double(n)

    while num != 0 {
        for i in 0...9 {
            let now = Double(i) * pow(10.0, deci - 1.0)
            let powDeci = Int(pow(10.0, Double(Int(deci))))
            
            if Int(num - now) % powDeci == 0 {
                answer += i
                num -= now
                break
            }
        }
        deci += 1
        print(num)  // 디버깅용
    }

    print(answer)  // 최종 출력
    return answer
}