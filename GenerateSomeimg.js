let duck = require("duckduckgo-images-api");
let axios = require("axios");
let fs = require("fs");
let path = require("path");

async function downloadAndSaveImage(url, directory, fileName) {
    try {
        const imagePath = path.join(directory, fileName);
        const writer = fs.createWriteStream(imagePath);

        const response = await axios({
            url,
            method: 'GET',
            responseType: 'stream'
        });

        response.data.pipe(writer);

        return new Promise((resolve, reject) => {
            writer.on('finish', resolve);
            writer.on('error', reject);
        });
    }
    catch (err) {
        console.log('erro')
    }
}


async function main() {
    const query = "write black plates";
    const moderate = true;
    const iterations = 4;

    let index = 0;
    for await (let resultSet of duck.image_search_generator({ query, moderate, iterations, })) {
        const images = resultSet.map((result) => ({
            url: result.image,
            fileName: `image_${index++}.jpg`
        }));

        const directory = 'results'; // Directory to save images
        if (!fs.existsSync(directory)) {
            fs.mkdirSync(directory);
        }

        for (let { url, fileName } of images) {
            await downloadAndSaveImage(url, directory, fileName);
            console.log(`Saved ${fileName}`);
        }
    }
}

main().catch(console.error);