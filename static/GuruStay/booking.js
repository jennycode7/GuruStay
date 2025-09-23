let currentStep = 1;
const totalSteps = 5;

function showStep(step) {
    // Update pages
    document.querySelectorAll('.page').forEach((p, i) => {
    p.classList.toggle('active', i === step - 1);
    });

    //change body style
    if (step === 2)
    {
        document.body.style.background = 'white';
    }
    else{
        document.body.style.background = "url('Static/css/images/image13.jpg')"
    }

    // Update stepper
    document.querySelectorAll('.step').forEach((s, i) => {
    s.classList.remove('active', 'done');
    if (i < step - 1) s.classList.add('done');
    else if (i === step - 1) s.classList.add('active');
    });
}

function nextStep() {
    if (currentStep < totalSteps) {
    currentStep++;
    showStep(currentStep);
    }
}

function prevStep() {
    if (currentStep > 1) {
    currentStep--;
    showStep(currentStep);
    }
}