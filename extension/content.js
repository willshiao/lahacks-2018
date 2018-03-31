let lastMessage = null

function getMessages () {
  return $('div>span._3oh-').toArray()
}

function getLastMessage () {
  return $('div>span._3oh-').last()
}

function getSender (msg) {
  const top = $(msg).parent().parent()
    .parent().parent().parent()
  return $(top).find('div._lt_q>a')
    .attr('href')
    .split('/')
    .pop()
}

function getData () {
  const chatId = window.location.href.split('/').pop()
  const targetName = $('h2>span._3oh-').text()
  const messages = getMessages()
  console.log('Title:', targetName)
  console.log('Chat ID: ', chatId)
  messages.forEach(msg => {
    console.log('Found message: ', $(msg).text())
  })
  lastMessage = messages[messages.length - 1]
  setInterval(getNewMessages, 1000)
}

function getNewMessages () {
  let newMessages = []
  if (getLastMessage() !== lastMessage) {
    const messages = getMessages()
    for (let i = messages.length - 1; i >= 0; --i) {
      if (messages[i] === lastMessage) break
      newMessages.push(messages[i])
    }
  }
  if (newMessages.length <= 0) return []
  lastMessage = newMessages[0]
  console.log('Setting last message to:', $(lastMessage).text())
  newMessages = newMessages.reverse()
  newMessages.forEach(msg => {
    const sender = getSender(msg)
    console.log(`Got new message: "${$(msg).text()}" from ${sender}`)
  })
  return newMessages
}

$(function () {
  setTimeout(getData, 5000)
})
