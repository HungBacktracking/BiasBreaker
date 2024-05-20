import React from 'react';
import { useParams } from 'react-router-dom';
import CategoryNews from '../components/CategoryNews/CategoryNews';

const categoryDescriptions = {
    "thế giới": "Những chuyển động bất ngờ trên toàn cầu",
    "thể thao": "Trải nghiệm nhịp sống thể thao sôi động",
    "kinh doanh": "Nắm bắt cơ hội và thách thức từ thị trường",
    "giải trí": "Chìm đắm trong thế giới giải trí không giới hạn",
    "du lịch": "Hành trình đến những miền đất kỳ diệu",
    "công nghệ": "Khám phá tương lai với những đột phá công nghệ",
    "chính trị": "Đi sâu vào những quyết định định hình thế giới"
};

function CategoryPage() {
    const { category } = useParams();
    const description = categoryDescriptions[category];

    return (
        <div className="flex flex-col">
        <div style={{ height: '125px' }}></div>
            <CategoryNews category={category} description={description}/>
        </div>
    );
}

export default CategoryPage;
