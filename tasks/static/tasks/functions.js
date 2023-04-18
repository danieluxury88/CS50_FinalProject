document.addEventListener('DOMContentLoaded', function () {
  console.log('page loaded');
  filterListByStatus();
  sortListByPriority();
});

function filterListByTitle() {
    let input = document.querySelector('#title-filter');
    let filter = input.value.toUpperCase();
    let workItems = document.querySelectorAll('.work-item');
    workItems.forEach(function(item) {
      let title = item.querySelector('.title').textContent.toUpperCase();
      if (title.indexOf(filter) > -1) {
        item.style.display = '';
      } else {
        item.style.display = 'none';
      }
    });
  }

  let durationSortedAscending = false;
  function sortListByDuration() {
    let workItems = document.querySelectorAll('.work-item');
    workItems = Array.prototype.slice.call(workItems, 0);
    workItems.sort(function(a, b) {
      let aDuration = parseInt(a.querySelector('.duration').textContent);
      let bDuration = parseInt(b.querySelector('.duration').textContent);
      if (aDuration < bDuration) return -1;
      if (aDuration > bDuration) return 1;
      return 0;
    });
    durationSortedAscending = !durationSortedAscending;
    if (durationSortedAscending) {
      workItems.reverse();
    }
    let parent = document.querySelector('.work-items-container');
    parent.innerHTML = '';
    workItems.forEach(function(item) {
      parent.appendChild(item);
    });
  }

  let statusSortedAscending = false;
  function sortListByStatus() {
    let workItems = document.querySelectorAll('.work-item');
    workItems = Array.prototype.slice.call(workItems, 0);
    workItems.sort(function(a, b) {
      let aStatus = a.querySelector('.status').textContent.toUpperCase();
      let bStatus = b.querySelector('.status').textContent.toUpperCase();
      if (aStatus < bStatus) return -1;
      if (aStatus > bStatus) return 1;
      return 0;
    });
    
    statusSortedAscending = !statusSortedAscending;
    if (statusSortedAscending) {
      workItems.reverse();
    }
    

    let parent = document.querySelector('.work-items-container');
    parent.innerHTML = '';
    workItems.forEach(function(item) {
      parent.appendChild(item);
    });
    console.log(statusSortedAscending);
  }

  function filterListByStatus() {
    let workItems = document.querySelectorAll('.work-item');
    workItems = Array.prototype.slice.call(workItems, 0);
    let selectedStatuses = Array.from(document.querySelectorAll('input[name="status"]:checked'))
      .map(function(checkbox) { return checkbox.value; });
    workItems.forEach(function(item) {
      let status = item.querySelector('.status').textContent.toUpperCase();
      if (selectedStatuses.length === 0 || selectedStatuses.includes(status)) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });
  }


  let prioritySortedAscending = true;
  function sortListByPriority() {
    let workItems = document.querySelectorAll('.work-item');
    workItems = Array.prototype.slice.call(workItems, 0);
    workItems.sort(function(a, b) {
      let aPriority = parseInt(a.querySelector('.priority').textContent);
      let bPriority = parseInt(b.querySelector('.priority').textContent);
      if (aPriority < bPriority) return -1;
      if (aPriority > bPriority) return 1;
      return 0;
    });
    prioritySortedAscending = !prioritySortedAscending;
    if (prioritySortedAscending) {
      workItems.reverse();
    }
    let parent = document.querySelector('.work-items-container');
    parent.innerHTML = '';
    workItems.forEach(function(item) {
      parent.appendChild(item);
    });
  }


  function update_task_state(task_id , state) {
    fetch(`tasks/${task_id}/update` , {
        method: 'PUT',
        body: JSON.stringify({
            state: state
        })
    }).then(()=> filterListByStatus())
  }

  function updateStatus(task_id, status) {
    let status_content = document.getElementById(`status_${task_id}`);
    console.log(status_content);
    console.log(status_content.innerHTML);
    console.log(status_content.textContent);
    fetch(`duty/tasks/${task_id}/update-status/`, {
      method: 'PUT',
      body: JSON.stringify({
        id: task_id,
        status: status,
      })
    }).then(() => {
      status_content.textContent = status;
      filterListByStatus();
    })
  }

  function updateTaskDueDate(task_id, selectElement) {
    console.log(task_id);
    console.log(selectElement);
    const selectedOption = selectElement.options[selectElement.selectedIndex];
    const selectedValue = selectedOption.value;
    const selectedText = selectedOption.text;

    console.log(`Selected Value: ${selectedValue}, Selected Text: ${selectedText}`);
    // fetch(`${task_id}/update-task-due-date/`, {
    //   method: 'PUT',
    //   body: JSON.stringify({
    //     id: task_id,
    //     status: status,
    //   })
    // }).then(() => {
    //   console.log("ok");
    // })
  }

  function updateMilestoneDueDate(milestone_id, selectElement) {
    console.log(milestone_id);
    console.log(selectElement);
    const selectedOption = selectElement.options[selectElement.selectedIndex];
    const selectedValue = selectedOption.value;
    const selectedText = selectedOption.text;

    console.log(`Selected Value: ${selectedValue}, Selected Text: ${selectedText}`);
    // fetch(`${task_id}/update-milestone-due-date/`, {
    //   method: 'PUT',
    //   body: JSON.stringify({
    //     id: milestone_id,
    //     status: status,
    //   })
    // }).then(() => {
    //   console.log("ok");
    // })
  }