const APP_ID = 'bbe2fe97634041caa9d55f28ad84e061'
const CHANNEL = sessionStorage.getItem('room')
const TOKEN = sessionStorage.getItem('token')
let UID = Number(sessionStorage.getItem('UID'))
let NAME = sessionStorage.getItem('name')

const client = AgoraRTC.createClient({mode: 'rtc', codec: 'vp8'})

let localTracks = []
let remoteUsers = {}

let joinAndDisplayLocalStream = async () => {

  document.getElementById('room-name').innerText = CHANNEL

  client.on('user-published', handleUserJoined)
  client.on('user-left', handleUserLeft)

  try {
    await client.join(APP_ID, CHANNEL, TOKEN, UID)
  }catch(error){
    console.error(error)
    window.open('/video-chat/', '_self')
  }


  localTracks = await AgoraRTC.createMicrophoneAndCameraTracks()  // at pos 0 and 1 we receive audio and video track

  let member = await createMember()

  let player = `<div class="video-container" id="user-container-${UID}">
                  <div class="video-player" id="user-${UID}"></div>
                  <div class="username-wrapper"><span class="user-name">${member.name}</span></div>
                </div>`

  document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)

  localTracks[1].play(`user-${UID}`)

  await client.publish([localTracks[0], localTracks[1]])
}

let handleUserJoined = async (user, mediaType) => {
    remoteUsers[user.uid] = user
    await client.subscribe(user, mediaType)

    if(mediaType === 'video') {
        let player = document.getElementById(`user-container-${user.uid}`)
        if(player != null){
            player.remove()
        }

        let member = await getMember(user)

        player = `<div class="video-container" id="user-container-${user.uid}">
                  <div class="username-wrapper"><span class="user-name">${member.name}</span></div>
                  <div class="video-player" id="user-${user.uid}"></div>
                </div>`

        document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)
        user.videoTrack.play(`user-${user.uid}`)
    }

    if(mediaType === 'audio') {
        user.audioTrack.play()
    }
}

let handleUserLeft = async (user) => {
    delete remoteUsers[user.uid]
    document.getElementById(`user-container-${user.uid}`).remove()
}

let leaveAndRemoveLocalStream = async () => {
    for (let i = 0; localTracks.length > i; i++) {
        localTracks[i].stop()
        localTracks[i].close()
    }

    await client.leave()

    deleteMember()

    window.open('/', '_self')
}

let toggelCamera = async (e) => {
    if(localTracks[1].muted){
        await localTracks[1].setMuted(false)
        e.target.style.backgroundColor = '#fff'
    }else{
        await localTracks[1].setMuted(true)
        e.target.style.backgroundColor = 'rgb(255, 80, 80, 1)'
    }
}

let toggelMic = async (e) => {
    if(localTracks[0].muted){
        await localTracks[0].setMuted(false)
        e.target.style.backgroundColor = '#fff'
    }else{
        await localTracks[0].setMuted(true)
        e.target.style.backgroundColor = 'rgb(255, 80, 80, 1)'
    }
}

let startStopRecording = async (e) => {
    if (e.target.dataset.val == 'start') {
        let response = await fetch(`/video-chat/start-recording/?channel=${CHANNEL}`)
        e.target.setAttribute('data-val','stop')
        e.target.style.backgroundColor = 'rgb(255, 80, 80, 1)'
        data = await response.json()
        sessionStorage.setItem('record_uid', data.record_uid)
        sessionStorage.setItem('sid', data.sid)
        sessionStorage.setItem('resource_id', data.resource_id)
    }
    else if (e.target.dataset.val == 'stop') {
        let record_uid = sessionStorage.getItem('record_uid')
        let sid = sessionStorage.getItem('sid')
        let resource_id = sessionStorage.getItem('resource_id')
        let response = await fetch(`/video-chat/stop-recording/?channel=${CHANNEL}&record_uid=${record_uid}&sid=${sid}&resource_id=${resource_id}`)
        sessionStorage.removeItem('record_uid')
        sessionStorage.removeItem('sid')
        sessionStorage.removeItem('resource_id')
        e.target.setAttribute('data-val','start')
        e.target.style.backgroundColor = '#fff'
    }
}

let createMember = async () => {
    let response = await fetch('/video-chat/create-member/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'name': NAME, 'room_name': CHANNEL, 'UID': UID})
    })

    let member = await response.json()
    return member
}

let getMember = async (user) => {
    let response = await fetch(`/video-chat/get-member/?UID=${user.uid}&room_name=${CHANNEL}`)
    let member = await response.json()
    return member
}


let deleteMember = async () => {
    let response = await fetch('/video-chat/delete-member/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'name': NAME, 'room_name': CHANNEL, 'UID': UID})
    })

    let member = await response.json()
}

joinAndDisplayLocalStream()

window.addEventListener('beforeunload', deleteMember)

document.getElementById('leave-btn').addEventListener('click', leaveAndRemoveLocalStream)
document.getElementById('camera-btn').addEventListener('click', toggelCamera)
document.getElementById('mic-btn').addEventListener('click', toggelMic)
document.getElementById('rec-btn').addEventListener('click', startStopRecording)
