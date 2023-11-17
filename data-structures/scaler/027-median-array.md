

## Median of the array
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/122354/assignment/problems/198/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/027-median-array-question.png)


### Approach

```js
module.exports = {
  //param A : array of integers
  //param B : array of integers
  //return an integer
  findMedianSortedArrays: function (A, B) {
        i = 0
        j = 0
        C = []
        while (i < A.length  && j < B.length) {
            if (A[i] <= B[j]) {
                C.push(A[i])
                i += 1
            } else {
                C.push(B[j])
                j += 1
            }
        }
        C = C.concat(A.slice(i,A.length))
        C = C.concat(B.slice(j,B.length))

        mid = Math.floor(C.length/2)
        if (C.length % 2 != 0) {
            return parseFloat(C[mid]).toFixed(1)
        } else {
            return parseFloat((C[mid] + C[mid-1])/2).toFixed(1)
        }


  },
};
```