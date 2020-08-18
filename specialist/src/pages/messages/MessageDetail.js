import React, { useEffect, useState } from 'react';

import { useParams, Link } from 'react-router-dom';

import { getThreadRef, sendMessage } from '../../services/firebase';

const MessageDetail = (props) => {

    const { uid } = useParams();

    const [messages, setMessages] = useState([]);

    useEffect(() => {
        const unsubscribe = getThreadRef(uid).onSnapshot(querySnapshot => {
            const threadMessages = [];
            querySnapshot.forEach(messsage => {
                const messageData = messsage.data();
                threadMessages.push({
                    text: messageData["text"],
                    time: messageData["createdAt"]
                });
            });
            setMessages(threadMessages);
        });

        return () => {
            unsubscribe();
        }
    }, []);

    const handleSubmit = async (event) => {
        event.preventDefault();
        const { text } = event.target.elements;
        const message = {
            createdAt: 0,
            customProperties: null,
            id: "",
            image: null,
            quickReplies: null,
            text: text.value,
            user: {
                avatar: "",
                color: null,
                containerColor: null,
                customProperties: null,
                firstName: null,
                lastName: null,
                name: "",
                uid: ""
            },
            video: null
        }
        await sendMessage(uid, message);
    }

    return (
        <>
            <Link to={"/"}>Back home</Link>
            <div className="ui container">
                {messages.length ?
                    <div className="ui comments">
                        <h3 className="ui dividing header">Messages with {uid}</h3>
                        {messages.map(message => 
                            <div className="comment" key={message["time"]}>
                                <div className="content">
                                    <div className="text">
                                        {message["text"]}
                                    </div>
                                </div>
                            </div>
                        )}
                        <form className="ui reply form" onSubmit={handleSubmit}>
                            <input name="text" type="text" placeholder="Reply..."/>
                            <button>Send</button>
                        </form>
                    </div>
                :
                    <>
                        <h3 className="ui dividing header">No messages found with {uid}</h3>
                    </>
                }
            </div>
        </>
    );
}

export default MessageDetail;