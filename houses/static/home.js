const showResidential = document.getElementById('residential-link')
const showApartments = document.getElementById('apartments-link')
const showCountryside = document.getElementById('countryside-link')
const showCommercial = document.getElementById('commercial-link')
const showAll = document.getElementById('all-link')

const showMore = document.getElementById('view-more-button')



const allGrid = document.getElementById('all')
const residentialGrid = document.getElementById('residential')
const commercialGrid = document.getElementById('commercial')
const countrysideGrid = document.getElementById('countryside')
const apartmentsGrid = document.getElementById('apartments')
const moreGrid = document.getElementById('view-more')


showResidential.addEventListener('click', toggleResidential)

function toggleResidential(){
    allGrid.classList.add('hidden')
    //console.log(residentialGrid)
    residentialGrid.classList.remove('hidden')
    commercialGrid.classList.add('hidden');
    apartmentsGrid.classList.add('hidden');
    countrysideGrid.classList.add('hidden');

    showResidential.classList.add('bold')
    showCommercial.classList.remove('bold');
    showCountryside.classList.remove('bold');
    showAll.classList.remove('bold');
    showApartments.classList.remove('bold')
}



showCommercial.addEventListener('click', toggleCommercial)

function toggleCommercial(){
    allGrid.classList.add('hidden')
    //console.log(residentialGrid)
    commercialGrid.classList.remove('hidden');
    residentialGrid.classList.add('hidden');
    apartmentsGrid.classList.add('hidden');
    countrysideGrid.classList.add('hidden');

    showResidential.classList.remove('bold')
    showCommercial.classList.add('bold');
    showCountryside.classList.remove('bold');
    showAll.classList.remove('bold');
    showApartments.classList.remove('bold')
}


showCountryside.addEventListener('click', toggleCountryside)

function toggleCountryside(){
    allGrid.classList.add('hidden')
    //console.log(residentialGrid)
    countrysideGrid.classList.remove('hidden');
    residentialGrid.classList.add('hidden');
    apartmentsGrid.classList.add('hidden');
    commercialGrid.classList.add('hidden');

    showResidential.classList.remove('bold')
    showCommercial.classList.remove('bold');
    showCountryside.classList.add('bold');
    showAll.classList.remove('bold');
    showApartments.classList.remove('bold')
}


showApartments.addEventListener('click', toggleApartments)

function toggleApartments(){
    allGrid.classList.add('hidden')
    //console.log(residentialGrid)
    apartmentsGrid.classList.remove('hidden')
    residentialGrid.classList.add('hidden');
    commercialGrid.classList.add('hidden');
    countrysideGrid.classList.add('hidden');

    showResidential.classList.remove('bold')
    showCommercial.classList.remove('bold');
    showCountryside.classList.remove('bold');
    showAll.classList.remove('bold');
    showApartments.classList.add('bold')
}


showAll.addEventListener('click', toggleAll)

function toggleAll(){
    allGrid.classList.remove('hidden')
    apartmentsGrid.classList.add('hidden')
    residentialGrid.classList.add('hidden');
    commercialGrid.classList.add('hidden');
    countrysideGrid.classList.add('hidden');

    showResidential.classList.remove('bold')
    showCommercial.classList.remove('bold');
    showCountryside.classList.remove('bold');
    showAll.classList.add('bold');
    showApartments.classList.remove('bold')

}




showMore.addEventListener('click', toggleViewMore)

function toggleViewMore(){
    
    console.log("view more")
    if (moreGrid.style['display']){
        
        moreGrid.style.removeProperty('display')
        showMore.textContent ='Show less'
        console.log('yessss')
    }
    else{
        console.log('no')
        moreGrid.style.display= 'none'
        showMore.textContent ='View more'
    }

    
}