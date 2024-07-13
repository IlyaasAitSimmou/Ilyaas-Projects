document.addEventListener('DOMContentLoaded', function() {
  
  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {
  document.querySelector('.btn-primary').disabled = true;
  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#email-view').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
  recipientsComposer = document.querySelector('#compose-recipients')
  subjectComposer = document.querySelector('#compose-subject')
  bodyComposer = document.querySelector('#compose-body')
  function submitDisabler() {
    if (recipientsComposer.value.length > 0 && subjectComposer.value.length > 0) {
      document.querySelector('.btn-primary').disabled = false;
    } else {
      document.querySelector('.btn-primary').disabled = true;
    }
  }
  recipientsComposer.onkeyup = submitDisabler
  subjectComposer.onkeyup = submitDisabler
  document.querySelector('.btn-primary').addEventListener('click', () => {
    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
          recipients: recipientsComposer.value,
          subject: subjectComposer.value,
          body: bodyComposer.value
      })
    })
    .then(response => response.json())
    .then(result => {
        // Print result
        console.log(result);
    });
  });

}

function view_email(email, archival) {
  if (document.querySelector('#archival_button')) {
    document.querySelector('#archival_button').remove();
  }
  fetch(`/emails/${email.id}`, {
    method: 'PUT',
    body: JSON.stringify({
        read: true
    })
  })
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'block';
  document.querySelector('#from').innerHTML = `From: ${email.sender}`;
  document.querySelector('#to').innerHTML = `To: ${email.recipients}`;
  document.querySelector('#subject').innerHTML = `Subject: ${email.subject}`;
  document.querySelector('#timestamp').innerHTML = `timestamp: ${email.timestamp}`;
  document.querySelector('#body').innerHTML = `${email.body}`;

  if (archival === true) {
    const button = document.createElement('input');
    button.type = 'submit'
    button.id = "archival_button"
    button.value = 'Archive'
    button.addEventListener('click', () => {
      fetch(`/emails/${email.id}`, {
        method: 'PUT',
        body: JSON.stringify({
            archived: true
        })
      })
    })
    document.querySelector('#email-view').append(button)
  } else if (archival === false) {
    const button = document.createElement('input');
    button.type = 'submit'
    button.id = "archival_button"
    button.value = 'Unarchive'
    button.addEventListener('click', () => {
      fetch(`/emails/${email.id}`, {
        method: 'PUT',
        body: JSON.stringify({
            archived: false
        })
      })
    })
    document.querySelector('#email-view').append(button)
  }
  const reply = document.createElement('input');
  reply.type = 'submit'
  reply.id = "reply_button"
  reply.value = 'Reply'
  document.querySelector('#email-view').append(reply)
  reply.addEventListener('click', () => {
    compose_email();
    document.querySelector('#compose-recipients').value = email.sender
  })
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // fetch mailbox
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
      // Print emails
      console.log(emails);

      // ... do something else with emails ...
      emails.forEach((email) => {
        console.log(email)
        const newEmail = document.createElement('div');
        // newEmail.className = "list-group-item"
        const list = newEmail.classList;
        list.add("list-group-item");
        list.add("email");
        newEmail.id = email.id
        newEmail.innerHTML = `<h5>${email.sender}  ${email.subject}      ${email.timestamp}</h5>`;
        newEmail.addEventListener('click', () => {
          if (String(mailbox) === 'inbox') {
            view_email(email, true)
          }
          else if (String(mailbox) === 'archive') {
            view_email(email, false)
          }
          else {
            view_email(email)
          }
          console.log(mailbox)
        });
        if (email.read) {
          newEmail.style.background = 'gray'
        }
        document.querySelector('#emails-view').append(newEmail);
      })
  });
}