:- dynamic elective/2.
:- multifile(elective/2).

check_elective(X) :-    elective(X,E),
                        E > 0.

getelectives('ML') :- machine_learning.
getelectives('CN') :- computer_networks.
getelectives('NS') :- network_security.
getelectives('CG') :- computer_graphics.
getelectives('IOT') :- internet_of_things.
getelectives('FF') :- foundations_of_finance.
getelectives('Rob') :- robotics.
getelectives('AI') :- artificial_intelligence.
getelectives('DA') :- d_animation.
getelectives('CGDAD') :- computer_game_design_and_development.

/*rules for each elective*/
machine_learning :-     check_elective('ML'),
                        nl,
                        format("MACHINE LEARNING"),nl,
                        write("--------------------------------------------------------"),
                        nl.            

computer_networks :-    check_elective('IS'),
                        nl,
                        write("COMPUTER NETWORKS"),nl,
                        write("--------------------------------------------------------"),nl.
                       
                    
                         
network_security:-  check_elective('IS'),
                    nl,
                    write("NETWORK SECURITY"),nl,
                    write("--------------------------------------------------------"),nl.
                    

computer_graphics :- check_elective('Design'),
                     nl,
                     write("COMPUTER GRAPHICS"),nl,
                     write("--------------------------------------------------------"),nl.

internet_of_things :-   check_elective('Electric'),
                        nl,
                        write("INTERNET OF THINGS"),nl,
                        write("--------------------------------------------------------"),nl.
    
foundations_of_finance :-   check_elective('Eco'),
                            nl,
                            write("FOUNDATIONS OF FINANCE"),nl,
                            write("--------------------------------------------------------"),nl.

robotics :- check_elective('AI'),
            nl,
            write("ROBOTICS"),nl,
            write("--------------------------------------------------------"),nl.

artificial_intelligence :-  check_elective('AI'),
                            nl,
                            write("ARTIFICIAL INTELLIGENCE"),nl,
                            write("--------------------------------------------------------"),nl.

d_animation :- check_elective('Design'),
               nl,
               write("3D ANIMATION"),nl,
               write("--------------------------------------------------------"),nl.

computer_game_design_and_development :- check_elective('Design'),
                                        nl,
                                        write("GAME DESIGN AND DEVELOPMENT"),nl,
                                        write("--------------------------------------------------------"),nl.

induced_facts(X):-
    consult('facts.pl'),
    getelectives(X).




                        