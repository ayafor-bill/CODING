//Dijkstra's Algorithm to compute the shortest path through a graph

#include <stdio.h>
#include <stdlib.h>

#define MAX_NODES 1024
#define INFINITY 1000000000
int n, dist[MAX_NODES][MAX_NODES];                                      //dist[][] holds the information about the nodes

void shortest_path(int s, int t, int path[])                            //s = source | t = target
{
    // Declaring the defining variables for Dijkstra's algorithm
    struct state {
        int predecessor;                                                //previous node in the shortest path
        int length;                                                     // Current shortest distance to the target
        enum {permanent, tentative} label;                              // Wether node is finalized or still being evaluated
    } state[MAX_NODES];                                                 //State array to hold the information for each node

    int i, k, min;
    struct state *p;                                                    //This is just a simple pointer to iterate through the state array

    //Initialization of the values for the state structure using the state structure to store the information
    for(p = &state[0]; p < &state[n]; p++){
        p->predecessor = -1;
        p->length = INFINITY;
        p->label = tentative;
    }
    state[t].length = 0; state[t].label = permanent;
    k=t;
    do {
        for (i = 0; i < n; i++)
            if (dist[k][i] != 0 && state[i].label == tentative)
            {
                if (state[k].length + dist[k][i] < state[i].length)
                {
                    state[i].predecessor = k;
                    state[i].length = state[k].length + dist[k][i];
                }    
            }

        k = 0; min = INFINITY;
        for (i = 0; i < n; i++)
            if (state[i].label == tentative && state[i].length < min)
            {
                min = state[i].length;
                k=i;
            }
            state[k].label = permanent;
    } while (k != s);
        
        i = 0; k = s;
        do {path[i++] = k; k = state[k].predecessor;} while(k >= 0);
}

