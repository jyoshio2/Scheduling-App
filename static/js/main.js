function add_task(){
    let start_time = $('#start_date').val();
    let end_time = $('#end_date').val();
    let task_name = $('#task_name').val();
    let hours = $('#max_hours').val();

    console.log(task_name + " " + hours + " " + end_time + " " + start_time);
    $.ajax({
    url: '/api',
    data: {'start_time': start_time, 'end_time': end_time, 'task_name': task_name, 'hours': hours},
    success: function (data) {
        console.log(data);

        $('#response_div').html('success');
    //    reload calendar

    }
});
}
