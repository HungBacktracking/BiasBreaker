import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import sampleData from '../data/sample.json';

const sampleKey = ['Key 1', 'Key 2', 'Key 3', 'Key 4', 'Key 5', 'Key 6', 'Key 7', 'Key 8'];

function NewsDetail() {
  const { id } = useParams();
  const [post, setPost] = useState(null);

  useEffect(() => {
    const fetchPost = async () => {
      const res = await fetch(`http://localhost:8080/articles/${id}`);
      const data = await res.json();
      setPost(data);
    };
    fetchPost();
  });

  return (
    <div className="flex justify-between gap-6 p-6">
      <aside className="w-[30%] h-full">
        <h2 className="text-xl font-medium mb-6">Prediction</h2>
        <div className="flex flex-col gap-8">
          <div>
            <h3 className="text-lg font-medium mb-2">Chart</h3>
            <div className="w-full h-48 p-4 border rounded-md"></div>
          </div>
          <div>
            <h3 className="text-lg font-medium mb-2">Summarize</h3>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea, pariatur modi saepe recusandae reiciendis
              adipisci. Obcaecati, id optio. Ratione, suscipit magni asperiores sunt quidem dolorem sit repellat
              deleniti illum expedita.
            </p>
          </div>
          <div>
            <h3 className="text-lg font-medium mb-2">Trending</h3>
            <ul>
              {sampleData.map((item) => (
                <li key={item.id} className="flex gap-4 mb-4 items-center">
                  <p className="text-md font-medium">{item.id}</p>
                  <img src={item.imagePath} alt={item.title} className="w-12 h-12 object-cover rounded-lg" />
                  <div>
                    <p className="text-sm font-medium">{item.title}</p>
                    <p className="text-sm">{item.date}</p>
                  </div>
                </li>
              ))}
            </ul>
          </div>
          <div>
            <h3 className="text-lg font-medium mb-2">Keywords</h3>
            <div className="flex gap-2 flex-wrap">
              {sampleKey.map((item) => {
                return (
                  <p key={item} className="border px-4 py-1 rounded-full border-green-500">
                    {item}
                  </p>
                );
              })}
            </div>
          </div>
        </div>
      </aside>
      <main className="w-[70%] h-full">
        <img
          src="https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp"
          alt="title"
          className="w-full h-96 object-cover rounded-xl mb-4"
        />
        <h1 className="text-4xl font-bold mb-6">Title</h1>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet, repellendus assumenda facere sapiente
          praesentium ducimus ut repudiandae hic totam possimus distinctio quasi voluptatum magnam quod, esse voluptates
          saepe labore illum?
          <br />
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus asperiores ea, aspernatur fugit soluta
          similique saepe magni vitae odio maiores quasi assumenda quaerat rem ab numquam cum a et aut? Lorem ipsum
          dolor sit amet, consectetur adipisicing elit. Amet, repellendus assumenda facere sapiente praesentium ducimus
          ut repudiandae hic totam possimus distinctio quasi voluptatum magnam quod, esse voluptates saepe labore illum?
          <br />
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus asperiores ea, aspernatur fugit soluta
          similique saepe magni vitae odio maiores quasi assumenda quaerat rem ab numquam cum a et aut? Lorem ipsum
          dolor sit amet, consectetur adipisicing elit. Amet, repellendus assumenda facere sapiente praesentium ducimus
          ut repudiandae hic totam possimus distinctio quasi voluptatum magnam quod, esse voluptates saepe labore illum?
          <br />
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus asperiores ea, aspernatur fugit soluta
          similique saepe magni vitae odio maiores quasi assumenda quaerat rem ab numquam cum a et aut? Lorem ipsum
          dolor sit amet, consectetur adipisicing elit. Amet, repellendus assumenda facere sapiente praesentium ducimus
          ut repudiandae hic totam possimus distinctio quasi voluptatum magnam quod, esse voluptates saepe labore illum?
          <br />
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus asperiores ea, aspernatur fugit soluta
          similique saepe magni vitae odio maiores quasi assumenda quaerat rem ab numquam cum a et aut?
        </p>
      </main>
      <aside className="w-[30%] h-full">
        <h2 className="text-xl font-medium mb-6">Related News</h2>
        <ul>
          {sampleData.map((item) => (
            <li key={item.id} className="flex gap-4 mb-4">
              <img src={item.imagePath} alt={item.title} className="w-24 h-24 object-cover rounded-lg" />
              <div>
                <h3 className="text-lg font-medium">{item.title}</h3>
                <p className="text-sm">{item.date}</p>
              </div>
            </li>
          ))}
        </ul>
      </aside>
    </div>
  );
}

export default NewsDetail;
