import { NavBarSection, JumboTron } from "../../components";

const HomePage = () => {
  return (
    <div className="w-full h-dvh bg-white flex flex-col">
      <div>
        <nav className="fixed top-0 w-full">
          <NavBarSection />
        </nav>
      </div>
      <div className="mt-20 w-full flex flex-col items-center justify-center">
        <div className="w-full">
          <JumboTron />
        </div>
      </div>
    </div>
  );
};

export default HomePage;
