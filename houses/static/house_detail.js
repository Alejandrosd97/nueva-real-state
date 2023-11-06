const buttons= document.querySelectorAll('[data-carousel-button]')

    buttons.forEach(button => {
      button.addEventListener('click', ()=>{
        const offset = button.dataset.carouselButton === 'next' ? 1 : -1
        const slides = button.closest('[data-carousel]').querySelector('[data-slides]')

        const activeSlide = slides.querySelector('[data-active]')
        let newIndex = [...slides.children].indexOf(activeSlide) + offset
        if (newIndex < 0){
          newIndex = slides.children.length -1
        }
        if (newIndex >= slides.children.length){
          newIndex = 0
        }

        slides.children[newIndex].dataset.active = true
        delete activeSlide.dataset.active
        console.log(newIndex)})
    })


    
      const closeModalBtn = document.getElementById('close-modal-button')
      closeModalBtn.addEventListener('click',()=>{
        document.getElementById('modal-bg').classList.remove('modal-active')
        document.getElementById('modal-box').classList.remove('modal-box-active')
        document.getElementById('modal-box').classList.add('modal-box-inactive')
      })

      const openModalBtn = document.getElementById('open-modal-button')
      openModalBtn.addEventListener('click',()=>{
        document.getElementById('modal-bg').classList.add('modal-active')
        document.getElementById('modal-box').classList.add('modal-box-active')
        document.getElementById('modal-box').classList.remove('modal-box-inactive')
      })

      const openModalMessage = document.getElementById('contact-owner-button')
      openModalMessage.addEventListener('click',()=>{
        console.log('a ver que pasa')
        document.getElementById('modal-message-bg').classList.add('modal-active')
        document.getElementById('modal-message-box').classList.add('modal-box-active')
        document.getElementById('modal-mesage-box').classList.remove('modal-box-inactive')
      })

      const closeModalMessage = document.getElementById('close-message-button')
      closeModalMessage.addEventListener('click', ()=>{
        document.getElementById('modal-message-bg').classList.remove('modal-active')
        document.getElementById('modal-message-box').classList.remove('modal-box-active')
        document.getElementById('modal-message-box').classList.add('modal-box-inactive')
      })