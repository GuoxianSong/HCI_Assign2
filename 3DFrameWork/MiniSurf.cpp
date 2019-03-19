#include "MiniSurf.h"


CMiniSurf::CMiniSurf(void)
{
	ptr_mesh_ = NULL;
}

CMiniSurf::CMiniSurf(Mesh3D *pMesh, float maxOffset=0.005)
{
	step_factor_ = 0.1;
	max_offset_ = maxOffset;
	ptr_mesh_ = pMesh;
	Init();
}

CMiniSurf::~CMiniSurf(void)
{
}

void CMiniSurf::Init(void)
{
	if (!ptr_mesh_->isValid())
	{
		std::cout<<"Mesh is not valid!"<<std::endl;
		return;
	}
    ptr_vertlist_ = ptr_mesh_->get_vertex_list();
    new_positions_.resize(ptr_vertlist_->size());


	float currentOffset = 0;
	do
	{
        currentOffset = MakeNewPositions();
		WriteNewPositions();
    }while(currentOffset>max_offset_);


    std::cout<<"="<<step_factor_<<",="<<max_offset_<<"."<<"."<<std::endl;

}

float CMiniSurf::MakeNewPositions()
{
	float curOffset = 0.0;
	HE_vert *pVert;
	int i,j;

	for (i=0;i<ptr_vertlist_->size();i++)
	{
		pVert = ptr_vertlist_->at(i);
        if (pVert->isOnBoundary())
			continue;

		int degree = pVert->degree();
		point newPosition(0.0,0.0,0.0);
		point newDir;

		for (j=0;j<degree;j++)
		{
			newPosition += ptr_mesh_->get_vertex(pVert->neighborIdx[j])->position();
		}
        newPosition /= (float)degree;
		newDir = newPosition - pVert->position();
        new_positions_[i] = pVert->position() + step_factor_*newDir;
		if (newDir*newDir > curOffset*curOffset)
            curOffset = sqrt(newDir*newDir);
	}

    return curOffset;
}

void CMiniSurf::WriteNewPositions(void)
{
	for (int i=0;i<ptr_vertlist_->size();i++)
        if (!ptr_vertlist_->at(i)->isOnBoundary())
			ptr_vertlist_->at(i)->set_position(new_positions_[i]);
}
