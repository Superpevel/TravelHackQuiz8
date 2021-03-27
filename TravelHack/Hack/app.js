const count = [];
let card_0 = [];
let card_1 = [];
let card_2 = [];
let card_3 = [];
let card_4 = [];

$(document).ready(() =>{
    //Home
    $('#homeBtn').on('click', () => {
        $('.home').fadeOut('fast');
        $('#card0').fadeIn('slow');
    })

    $('#reload').click(function() {
        location.reload();
    });

  });

