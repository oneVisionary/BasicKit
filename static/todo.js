
function addTodo(){
    const title = $('#todoInput').val().trim();
    console.log('Adding todo:', title);
    if(title === '') {
        alert('Please enter a todo item.');
        return;
    }
    $.ajax({
        url:addTodoUrl,
        type:'POST',
        contentType:'application/json',
        data: JSON.stringify({title: title}),
        success: function(response) {
          
            $('#todoInput').val(''); // Clear input field
             location.reload(); 
           alert("Todo added successfully")
          
        },
        error:function(error) {
            alert('Error adding todo: ' + error.responseText);
        }
    })
}

function toggleComplete(taskid,isChecked){
console.log(`updated data:${taskid},${isChecked}`)
 $.ajax({
        url:updateTodoUrl,
        type:'POST',
        contentType:'application/json',
        data: JSON.stringify({id: taskid, completed:isChecked}),
        success: function(response) {
           location.reload(); 
          console.log('Task updated successfully',response)
        },
        error:function(error) {
            alert('Error adding todo: ' + error.responseText);
        }
    })
}

function deleteTodo(taskid){
  
 $.ajax({
        url:deleteTodoUrl,
        type:'POST',
        contentType:'application/json',
        data: JSON.stringify({id: taskid}),
        success: function(response) {
           location.reload(); 
          alert('Task deleted successfully')
        },
        error:function(error) {
            alert('Error adding todo: ' + error.responseText);
        }
    })
}