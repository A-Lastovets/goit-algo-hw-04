from pathlib import Path 

def get_cats_info(file_path) -> list:
 
    try:
        file_path = Path("A:/Home_work/goit-algo-hw-04/cats.txt")
        info_cats = ["60b90c1c13067a15887e1ae1,Tayson,3",
                     "60b90c2413067a15887e1ae2,Vika,1",
                     "60b90c2e13067a15887e1ae3,Barsik,2",
                     "60b90c3b13067a15887e1ae4,Simon,12",
                     "60b90c4613067a15887e1ae5,Tessi,5"
                    ]
 
        with open(file_path, "w", encoding="utf-8") as file:
            file.write('\n'.join(info_cats))

        with open(file_path, "r", encoding="utf-8") as file:
                info_dict = []
                for info_cats in file:
                    id_info, name_info, age_info = info_cats.split(",")
                    info_dict.append({"id": id_info, "name": name_info, "age": age_info})

        return (info_dict)
    
    except FileNotFoundError:
        print("File not found or corrupted")

info_dict = get_cats_info("cats.txt")

print(f"Загальна інформація всіх котів: {info_dict}\n")