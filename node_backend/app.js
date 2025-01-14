import express from 'express'
import cors from 'cors'
import 'dotenv/config'
import axios from 'axios';
const PORT = 5000;
const app = express();
app.use(cors());
app.use(express.json());



app.post('/add_user', async (req, res) => {
    try {
        

        console.log(`This is url ${process.env.API_URL}`);
        const response = await axios.post(`${process.env.API_URL}/add_user`);
        return res.status(200).json({message: "Successfully added User", response: response.data});
    } catch (error) {
        console.log("This is error in catch block", error);
        return res.status(500).json({message: "Internal server error."});
    }
});


app.get('/history/:username', async(req, res) => {
    try {
        const username = req.params.username;

        const response = await axios.get(`${process.env.API_URL}/history/${username}`);

        return res.status(200).json({message: "History fetched Successfully", response: response.data});
    }
    catch(error)
    {
        console.log("This is error from catch block", error);
        return res.status(500).json({message:"Internal Server error"});
    }
});


app.post('/add_data/:username', async(req, res) => {
    try {
        const username = req.params.username;

        const response = await axios.post(`${process.env.API_URL}/add_data/${username}`);

        return res.status(200).json({message: "Data added successfully", response: response.data});
    }
    catch(error)
    {
        console.log("This is error from catch block", error);
        return res.status(500).json({message:"Internal Server error"});
    }
});

app.listen(PORT, () => {
    console.log(`App is running on Port ${PORT}`)
});
