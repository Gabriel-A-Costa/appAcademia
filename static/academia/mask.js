$(document).ready(function () {
  $('#cpf').mask('000.000.000-00')
  $('#data').mask('00/00/0000')

  var SPMaskBehavior = function (val) {
      return val.replace(/\D/g, '').length === 11
        ? '(00) 0 0000-0000'
        : '(00) 0000-00009'
    },
    spOptions = {
      onKeyPress: function (val, e, field, options) {
        field.mask(SPMaskBehavior.apply({}, arguments), options)
      }
    }

  $('#phone_number').mask(SPMaskBehavior, spOptions)
})
