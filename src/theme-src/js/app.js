import '../css/styles.css'
import '@fontsource/jetbrains-mono/latin-400.css'
import '@fontsource/jetbrains-mono/latin-400-italic.css'
import '@fontsource/jetbrains-mono/latin-500.css'
import '@fontsource/jetbrains-mono/latin-500-italic.css'
import '@fontsource/jetbrains-mono/latin-700.css'
import '@fontsource/jetbrains-mono/latin-700-italic.css'

import Alpine from 'alpinejs'
// import intersect from '@alpinejs/intersect'
import { addCodeButtons } from './code'
import { scrollSpy } from './scrollspy'

window.Alpine = Alpine
// Alpine.plugin(intersect)
Alpine.start()

window.addEventListener('DOMContentLoaded', () => {
  addCodeButtons()
  scrollSpy()
})
