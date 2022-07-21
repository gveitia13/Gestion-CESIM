// $(document).ready(function () {
//   $('#my-select').select2({
//   });
// });

let modal_form = $('#form-modal'),
  modal = document.querySelector('#staticBackdrop')

modal.addEventListener('shown.bs.modal', function () {
  document.querySelector('#id_nombre').focus()
})

modal.addEventListener('hidden.bs.modal', function () {
  document.querySelector('#id_nombre').value = ''
  document.querySelector('#id_ci').value = ''
  document.querySelector('#id_cuenta_bancaria').value = ''
  document.querySelector('#id_apellidos').value = ''
  document.querySelector('#id_categoria_ocupacional').value = ''
  document.querySelector('#id_categoria_cientifica').value = ''
  document.querySelector('#id_cargo').value = ''
  document.querySelector('#id_clasificador_entidad').value = ''
  document.querySelector('#id_porciento_de_remuneracion').value = ''
  document.querySelector('#id_salario_mensual_basico').value = ''
  document.querySelector('#id_institucion').value = ''
  document.querySelector('#id_porciento_de_participacion').value = ''
  document.querySelector('#id_tiempo').value = ''
})

document.querySelector('#create-member').addEventListener('click', () => {
  document.querySelector('#hidden').value = 'create'
})

document.querySelectorAll('button[rel=edit]').forEach(e => {
  e.addEventListener('click', function () {
    document.querySelector('#hidden').value = 'edit'
    document.querySelector('#id_to_edit').value = this.id
    let params = new FormData()
    params.append('action', 'search_member')
    params.append('pk', this.id)
    ajaxFunction(location.pathname, params, 'POST', data => {
      console.log(data)
      document.querySelector('#id_nombre').value = data.nombre
      document.querySelector('#id_ci').value = data.ci
      document.querySelector('#id_cuenta_bancaria').value = data.cuenta_bancaria
      document.querySelector('#id_apellidos').value = data.apellidos
      document.querySelector('#id_categoria_ocupacional').value = data.categoria_ocupacional
      document.querySelector('#id_categoria_cientifica').value = data.categoria_cientifica
      document.querySelector('#id_cargo').value = data.cargo
      document.querySelector('#id_clasificador_entidad').value = data.clasificador_entidad
      document.querySelector('#id_porciento_de_remuneracion').value = data.porciento_de_remuneracion
      document.querySelector('#id_salario_mensual_basico').value = data.salario_mensual_basico
      document.querySelector('#id_institucion').value = data.institucion
      document.querySelector('#id_porciento_de_participacion').value = data.porciento_de_participacion
      document.querySelector('#id_tiempo').value = data.tiempo
    })
  })
})


modal_form.on('submit', function (event) {
  event.preventDefault()
  let params = new FormData(this)

  if (document.querySelector('#hidden').value === 'edit')
    params.append('pk', document.querySelector('#id_to_edit').value)

  ajaxFunction(location.pathname, params, 'POST', data => {
    console.log(data)

    location.reload()
  })
})