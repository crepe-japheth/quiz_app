const quizForm = document.querySelector('#quiz-form');
const btnSubmit = document.querySelector('.btn-quiz');
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const checkedAnswers = [...document.getElementsByClassName('answer')]
const url = window.location.href
const displayMarks = document.querySelector('.display-marks')
const time = document.querySelector('.timer')
const timeBox = document.querySelector('.timer-box')

const checkCorrect = (answer, correct) => {
    if (!correct) {
        return 'bg-danger'
    } else {

        for (let i = 0; i < answer.length; i++) {
            if (answer[i] != correct[i]) {
                return 'bg-danger'
            } else {
                return 'bg-success'
            }
        }
    }
}
const checkStatus = (passOrFail) => {
    if (passOrFail == 'Failed') {
        return 'bg-danger'
    } else {
        return 'bg-success'
    }
}
const submit = async() => {
    const data = {};
    checkedAnswers.forEach(ans => {

        if (ans.checked) {
            if (data[ans.name]) {
                data[ans.name].push(ans.value)
            } else {
                data[ans.name] = [ans.value];
            }
        } else {
            if (!data[ans.name]) {
                data[ans.name] = null
            }
        }
    })
    try {
        const response = await fetch(`${url}save`, {
            method: 'POST',
            credentials: 'same-origin',
            headers: {
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': csrf[0].value
            },
            body: JSON.stringify(data)
        })

        const res = await response.json()
        const results = res.answers
        const status = res.status
        const score = res.scored
        quizForm.classList.add('not-visible')

        timeBox.innerHTML = `<span class="${checkStatus(status)}">${status}</span> - ${score}%`


        for (let i = 0; i < results.length; i++) {
            for (const [key, value] of Object.entries(results[i])) {
                displayMarks.insertAdjacentHTML("afterbegin",
                    `
                    <div class="row g-4">
                    <h1 class="display-6 mb-4">${key}</h1>
                        <div class="col-sm-6">
                            <p class="${checkCorrect(results[i][key].correct_answer, results[i][key].answered)} text-white py-3 answered px-5">answered: ${results[i][key].answered}</p>
                        </div>
                        <div class="col-sm-6">
                            <p class="bg-success text-white py-3 px-5">correct answer: ${results[i][key].correct_answer}</p>
                        </div>
                    </div>
                `)

            }
        }


    } catch (err) {
        // quizForm.classList.add('not-visible')
        alert("Something went wrong!!")
    }



}

quizForm.addEventListener('submit', e => {
    e.preventDefault();
    submit();
})