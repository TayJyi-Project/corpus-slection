function All_Proc_Matlab_Python_VC
% tic;
% fclose all;clear all;close all;clc;
%
% addpath('C:\Users\sypdbhee\Documents\MATLAB\sypdbhee\130402_VoiceConversion\VoiceConversion\VC_function');

%% Parameter Setting

InputPar.ClusterNum  =1;
InputPar.FeaType     ='powspec'; % lpsmfcc, powspec, mel, powspecmel, vocoder, mfcc

%%%% For GLOBAL SETTING
InputPar.SampleRate  = 44100;
% InputPar.SampleRate  =16000;        % 8k Hz, sampling rate
InputPar.FFT_SIZE    = 2048; % according to Sprocket
% InputPar.FFT_SIZE    =1024;
%%%% For GLOBAL SETTING

%%%% For STFT
InputPar.FrameSize   =1024; %16ms per frame (256 points)
InputPar.FrameRate   = 256; 
% InputPar.FrameRate   =512 ; %8ms frame shift
InputPar.FeaDim      =InputPar.FrameSize/2+1;
%%%% For STFT


%%%% List pathes of training data
% target list
InputPar.TriNoisyPath ='/home/ecl/corpus-slection/src/audList/hawa-long';
% source list
InputPar.TriCleanPath ='/home/ecl/corpus-slection/src/audList/kp-long';


%%%% Parameters for NN training
InputPar.Ws              =0;
InputPar.HiddenLayerSizes=[500 500 500 500];
InputPar.MaxEpoch        =50;


%% Inp: Sor; Out: Tar
%%%%% Training

InputPar.runName  =[upper(InputPar.FeaType),'_FrSiz_',num2str(InputPar.FrameSize),'_FrSft_'...
    ,num2str(InputPar.FrameRate),'_Cls_',num2str(InputPar.ClusterNum),'_MaxEpoch_',num2str(InputPar.MaxEpoch),'_Ws_',num2str(InputPar.Ws)...
    ,'_InpaOut_SaT'];
for i=1:length(InputPar.HiddenLayerSizes)
    InputPar.runName=[InputPar.runName,'_HS',num2str(InputPar.HiddenLayerSizes(i))];
end
InputPar.Model=cell(InputPar.ClusterNum,1);

% [InpDim,OutDim]=Train_DWT_Feature_Extraction(InputPar); %���testing(���@training)���ѳo��
Train_DWT_Feature_Extraction(InputPar); %���testing(���@training)���ѳo��

fprintf('Finished Evaluation.\n');

