document.addEventListener('DOMContentLoaded', function () {
  filterListByStatus();
});

function filterListByTitle() {
    console.log("filterListByTitle");
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
    console.log("sortListByDuration");
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
    console.log("sortListByStatus");
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
    console.log("filterListByStatus");
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
    console.log("sortListByPriority");
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
    console.log("update_task_state");
    fetch(`tasks/${task_id}/update` , {
        method: 'PUT',
        body: JSON.stringify({
            state: state
        })
    }).then(()=> filterListByStatus())
  }

  function updateStatus(task_id, status) {
    console.log("updateStatus");
    let status_content = document.getElementById(`status_${task_id}`);
    fetch(`duty/tasks/${task_id}/update-status/`, {
      method: 'PUT',
      body: JSON.stringify({
        id: task_id,
        status: status,
      })
    }).then(response => response.json())
      .then(data => {
        const newStatus = data.status;
        status_content.textContent = newStatus;
    }).then(() => {
      filterListByStatus();
    })
  }

  function updateTaskDueDate(task_id, selectElement) {
    console.log("updateTaskDueDate");
    console.log(task_id);
    console.log(selectElement);
    const selectedOption = selectElement.options[selectElement.selectedIndex];
    const selectedValue = selectedOption.value;
    const selectedText = selectedOption.text;

    console.log(selectedText);
    console.log(selectedValue);

    console.log(`Selected Value: ${selectedValue}, Selected Text: ${selectedText}`);
    fetch(`duty/tasks/${task_id}/update-task-due-date/`, {
      method: 'PUT',
      body: JSON.stringify({
        id: task_id,
        due_date: selectedValue,
      })
    }).then(() => {
      console.log("ok");
    })
  }

  function updateMilestoneDueDate(milestone_id, selectElement) {
    console.log("updateMilestoneDueDate");
    console.log(milestone_id);
    console.log(selectElement);
    const selectedOption = selectElement.options[selectElement.selectedIndex];
    const selectedValue = selectedOption.value;
    const selectedText = selectedOption.text;
    console.log(selectedText);
    console.log(selectedValue);

    console.log(`Selected Value: ${selectedValue}, Selected Text: ${selectedText}`);
    fetch(`duty/milestones/${milestone_id}/update-milestone-due-date/`, {
      method: 'PUT',
      body: JSON.stringify({
        id: milestone_id,
        due_date: selectedValue,
      })
    }).then(() => {
      console.log("ok");
    })
  }