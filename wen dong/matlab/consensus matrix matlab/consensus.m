function con = consensus(D, kind)
% consensus  Calculates the consensus matrix after applying 
%            k-medoids with a partition configuration into 
%            a set of distance matrices.

%   con = consensus(D) Calculates the consensus matrix for D 
%         in a default partition kind= [2:20]. D is a three
%          dimensional array, where the third dimension provides 
%         the node identity whose distance matrix in the subject  
%         space (given by the first two dimensions of the array) 
%         is partitioned using k-medoids.

%   con = consensus(D,kind) Calculates the consensus matrix for D 
%         in a supplied partition configuration kind. D is a three
%          dimensional array, where the third dimension provides 
%         the node identity whose distance matrix in the subject  
%         space (given by the first two dimensions of the array) 
%         is partitioned using k-medoids.

if isempty(D)
	error('D must be provided')

if not(size(D,3))
    error('D must be an array of distance matrices')
end

if (nargin < 2) || isempty(kind)
	kind=[2:20];
end

m = size(D, 1);
nk=length(kind);
c=zeros(m,nk,n);
A=logical(zeros(m,m,nk,n));

for i=1:n
    for k=1:nk
	  kk=kind(k);
	  c(:,k,i) = kmedoids(D(:,:,i),kk);
	  for l=1:m
	      for j=l+1:m
	          A(l,j,k,i)=c(l,k,i)==c(j,k,i);
	          A(j,l,k,i)=A(l,j,k,i);
	      end
	  end
    end
end

con = mean(mean(A,4),3)
end
