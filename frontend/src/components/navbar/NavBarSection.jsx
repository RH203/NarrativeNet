import { IoIosSearch } from "react-icons/io";
import { ImCross } from "react-icons/im";
import { useState } from "react";

const NavBarSection = () => {
  const [isHidden, setIsHidden] = useState(false);

  const toggleVisibility = () => {
    setIsHidden(!isHidden);
  };

  return (
    <div className="w-full h-[67px] bg-bg-nav box-border flex justify-around">
      {isHidden === false && (
        <>
          <div className="flex justify-evenly items-center gap-10 animate-fadeIn">
            <div className="flex justify-between items-center">
              <a href="">
                <img
                  src="../../public/icons/PDI-Perjuangan.svg"
                  alt="Logo"
                  className="w-[80px] cursor-pointer"
                />
              </a>
              <p className="text-black font-Quicksand font-medium text-2xl">
                NarrativeNet
              </p>
            </div>
            <div className="flex ">
              <ul className="flex items-center">
                <li className="items-start">
                  <a
                    href=""
                    className="text-black font-Quicksand font-normal text-xl relative hover:before:opacity-100 before:absolute before:inset-x-0 before:bottom-0 before:h-[3px] before:bg-black before:opacity-0 before:transition-opacity before:duration-500"
                  >
                    browse
                  </a>
                </li>
              </ul>
            </div>
          </div>

          <div className="flex items-center animate-fadeIn">
            <nav>
              <ul className="flex justify-between items-center gap-6">
                <li>
                  <button
                    onClick={toggleVisibility}
                    className="btn btn-circle bg-gray-300 active:text-white"
                  >
                    <IoIosSearch className="size-[30px] text-black hover:text-white active:text-white" />
                  </button>
                </li>
                <li>
                  <input
                    type="checkbox"
                    className="toggle toggle-warning [--tglbg:white] bg-gray-700  border-black"
                    // hover:bg-black
                  />
                </li>
              </ul>
            </nav>
          </div>
        </>
      )}

      {isHidden === true && (
        <div className="flex items-center animate-fadeIn">
          <button onClick={toggleVisibility} className="btn btn-square rounded-tr-none rounded-br-none bg-black text-2xl">
            <ImCross />
          </button>
          <input
            type="text"
            placeholder="Search"
            className="input w-[500px] max-w-xs rounded-none bg-black"
          />
          <button className="btn btn-square rounded-tl-none rounded-bl-none bg-black text-2xl">
            <IoIosSearch />
          </button>
        </div>
      )}
    </div>
  );
};


export default NavBarSection;
