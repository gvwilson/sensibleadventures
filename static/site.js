const fixFootnotes = () => {
  Array.from(document.querySelectorAll('section')).forEach((section, i) => {
    const list = document.createElement('ol')
    Array.from(section.querySelectorAll('sup')).forEach((sup, j) => {
      const text = sup.innerHTML
      label = `footnote.${i+1}.${j+1}`
      sup.innerHTML = `<a href="#${label}">${j+1}</a>`
      const item = document.createElement('li')
      item.id = label
      item.innerHTML = text
      list.appendChild(item)
    })
    section.appendChild(list)
  })
}

const fixPage = () => {
  fixFootnotes()
}
