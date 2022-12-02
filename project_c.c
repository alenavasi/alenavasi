#include <math.h>
#include <stdio.h>

double yo = 100;
double sigma = 3;

double fonction(double x) {
    double simple = x/sigma;
    double y = yo * exp(-0.5*simple*simple);
    return y;
}

int main(){
    int step = 10;                /*nombre d'élément dans une unité des x*/
    double increment = 0.2;
    int longueur = 101; 

    double masse = 10;
    double coef_frot = 8;
    double vo = 10;

    double x[longueur];
    double y[longueur];
    int compteur0 = 0;
    while(compteur0 < longueur) {
        double c0 = compteur0;
        double s0 = step;
        double x0 = c0/s0;
        x[compteur0] = x0;
        y[compteur0] = fonction(x0);
        compteur0 += 1;
    }

    double derivee[longueur];
    int compteur1 = 0;
    while(compteur1 < longueur){
        double c1 = compteur1;
        double s1 = step;
        double x1 = c1/s1;
        double fp = (fonction(x1 + increment) - fonction(x1))/increment;
        derivee[compteur1] = fp;
        compteur1++;
    }

    double vitesse[longueur];
    int compteur2 = 0;
    while(compteur2 < longueur){
        double v = -derivee[compteur2]*masse/coef_frot + vo;
        vitesse[compteur2] = v;
        if((vo-0.1) > 0){
            vo = vo- 0.1;          /*importance de la vitesse initiale decroissante*/
        }
        compteur2++;
    }

    int len = longueur/10;
    double vitesse_moy[len];
    int compteur3 = 0;
    for(int i=0; i<len; i++){
        double sum = 0;
        for(int j = 0; j<10; j++){
            sum = sum + vitesse[compteur3];
            compteur3++;
        }
        sum = sum / 10;
        vitesse_moy[i] = sum;
    }

    double puissance[longueur];
    for(int i=0; i<longueur; i++){
        double Ec = (masse*vitesse[i]*vitesse[i])/2;
        puissance[i] = Ec/1000;                //puissance en kJ
    }

    double maxi = puissance[0];
    int x_max = 0;
    for(int i=0; i<longueur; i++){
        if(puissance[i]>maxi){
            x_max = i;
            maxi = puissance[i];
        }
    }
    double result[2];
    result[0] = maxi;
    result[1] = x_max;

    FILE * fichier = fopen("Resultats", "w");
    if(fichier == NULL){
        printf("Impossible d'ouvrir le fichier.\n");
        return 1;
    }
    fprintf(fichier, "Vitesse :\n");
    for(int i=0; i<longueur; i++){
        fprintf(fichier, "%f\n", vitesse[i]);
    }
    fprintf(fichier, "Vitesse_moyenne :\n");
    for(int i=0; i<len; i++){
        fprintf(fichier, "%0.1f\n", vitesse_moy[i]);
    }
    fprintf(fichier, "Puissance :\n");
    for(int i=0; i<longueur; i++){
        fprintf(fichier, "%f\n", puissance[i]);
    }
    fprintf(fichier, "Maximum :\n");
    for(int i=0; i<2; i++){
        fprintf(fichier, "%f\n", result[i]);
    }
    fprintf(fichier, "Step :\n%d\n", step);

    fprintf(fichier, "X :\n");
    for(int i=0; i<longueur; i++){
        fprintf(fichier, "%f\n", x[i]);
    }
    fprintf(fichier, "Y :\n");
    for(int i=0; i<longueur; i++){
        fprintf(fichier, "%f\n", y[i]);
    }
    fclose(fichier);

    return 0;
}