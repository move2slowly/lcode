class Solution {
public:
    int max(int first, int second){
            
             if(first >= second){
                 return first;
             }
             return second;
    }
    
    int min(int first, int second){
            
             if(first <= second){
                 return first;
             }
             return second;
    }
    
    int maxArea(vector<int>& height) {
      
        int maxArea = 0;
        int a=0;
        int b=0;
        
        for(int i=0; i <height.size()-1; i++){
            maxArea = max(maxArea,(height.size()-a-b-1)*min(height.at(a),height.at(height.size()-1-b)));
            if(height.at(a)<=height.at(height.size()-1-b)){
                a++;
            }else{
                b++;
            }
            
        }
        return maxArea;
    }
};
