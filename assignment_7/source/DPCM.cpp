#include<stdio.h>
#include<math.h>
#include<iostream>
#include<malloc.h>
void dpcm_encode(unsigned char*ybuf, unsigned char*qbuf, unsigned char*rebuf, int width, int height,int bitdepth)
{
	for (int i = 0; i < height; i++)
	{
		qbuf[i*width] = (ybuf[i*width] - 128 + 255) / pow(2, (9 - bitdepth));
		rebuf[i*width] = qbuf[i*width] * pow(2, (9 - bitdepth))+255 - 128;
	}
	for (int i = 0; i < width; i++)
	{
		for (int j = 1; j < height; j++)
		{
			qbuf[i*width+j] = (ybuf[i*width+j] - rebuf[i*width + j-1] + 255) / pow(2, (9 - bitdepth));
			rebuf[i*width+j] = qbuf[i*width+j] * pow(2, (9 - bitdepth)) - 255 + rebuf[i*width + j - 1];
		}
	}
	for (int i = 0; i < width*height; i++)
	{
		if (qbuf[i] > 255)
			qbuf[i] = 255;
		if (qbuf[i] < 0 )
			qbuf[i] = 0;
		if (rebuf[i] > 255)
			rebuf[i] = 255;
		if (rebuf[i] < 0)
			rebuf[i] = 0;
	}
}
int main()
{
	FILE *yuv = NULL; FILE *qyuv = NULL; FILE *reyuv = NULL;
	const int width = 256; const int height = 256;
	if (!(yuv = fopen("origin.yuv", "rb")))
	{
		printf("open file error!");
		exit(-1);
	}
	else
	{
		printf("open file success");
	}
	if (!(qyuv = fopen("lena_q.yuv", "wb")))
	{
		printf("open file error!");
		exit(-1);
	}
	else
	{
		printf("open file success");
	}
	if (!(reyuv = fopen("lena_re.yuv", "wb")))//8,4,2,1 
	{
		printf("open file error!");
		exit(-1);
	}
	else
	{
		printf("open file success");
	}
	unsigned char *ybuf = (unsigned char*)malloc(sizeof(unsigned char) * width * height);
	unsigned char *ubuf= (unsigned char*)malloc(sizeof(unsigned char) * width * height*0.25);
	unsigned char *vbuf = (unsigned char*)malloc(sizeof(unsigned char) * width * height*0.25);
	unsigned char *qbuf = (unsigned char*)malloc(sizeof(unsigned char) * width * height);
	unsigned char *rebuf = (unsigned char*)malloc(sizeof(unsigned char) * width * height);
	fread(ybuf, sizeof(unsigned char), width* height, yuv);
	fread(ubuf, sizeof(unsigned char), width* height*0.25, yuv);
	fread(vbuf, sizeof(unsigned char), width* height*0.25, yuv);
	int bitdepth = 8; //8,4,2,1
	dpcm_encode(ybuf, qbuf, rebuf,  width, height, bitdepth);
	double freq_q[256] = { 0 };double freq_lena[256] = { 0 };
	for (int i = 0; i < 256; i++)
	{
		freq_q[i] = double(qbuf[i]) / (width*height);
		freq_lena[i] = double(ybuf[i]) / (width*height);
	}	
	FILE *qfile; FILE *lenafile;
	if ((qfile = fopen("8pre_error.txt", "w")) == NULL) //8pre_error.txt,4pre_error.txt,2pre_error.txt,1pre_error.txt
		printf("fail\n");
	else
		printf("success\n");
	if ((lenafile = fopen("orgin.txt", "w")) == NULL)
		printf("fail\n");
	else
		printf("success\n");
	char s[] = "symbol\frequency\n";
	fprintf(qfile, s); fprintf(lenafile, s); 
	for (int i = 0; i < 256; i++)
	{
		fprintf(qfile, "%d\t%f\n", i, freq_q[i]);
		fprintf(lenafile, "%d\t%f\n", i, freq_lena[i]);
	}
	fwrite(qbuf, sizeof(unsigned char), width * height, qyuv);
	fwrite(ubuf, sizeof(unsigned char), width * height*0.25, qyuv);
	fwrite(vbuf, sizeof(unsigned char), width * height*0.25, qyuv);
	fwrite(rebuf, sizeof(unsigned char), width * height, reyuv);
	fwrite(ubuf, sizeof(unsigned char), width * height*0.25, reyuv);
	fwrite(vbuf, sizeof(unsigned char), width * height*0.25, reyuv);
	free(ybuf); free(ubuf); free(vbuf);
	free(qbuf); free(rebuf);
	fclose(yuv);
	fclose(qyuv);
	fclose(reyuv);
	fclose(qfile);
	fclose(lenafile);
}

