# SoundMAGIC PL50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.9; 23 -10.0; 25 -10.1; 28 -10.2; 31 -10.2; 34 -10.2; 37 -10.2; 41 -10.2; 45 -10.3; 49 -10.4; 54 -10.5; 60 -10.6; 66 -10.5; 72 -10.5; 79 -10.5; 87 -10.5; 96 -10.5; 106 -10.5; 116 -10.5; 128 -10.5; 141 -10.5; 155 -10.3; 170 -10.2; 187 -10.0; 206 -9.9; 227 -9.9; 249 -10.3; 274 -10.8; 302 -10.9; 332 -10.7; 365 -10.3; 402 -10.1; 442 -9.9; 486 -9.9; 535 -9.7; 588 -9.3; 647 -9.0; 712 -8.7; 783 -8.4; 861 -8.1; 947 -7.8; 1042 -7.5; 1146 -7.3; 1261 -7.0; 1387 -7.0; 1526 -7.0; 1678 -7.3; 1846 -8.1; 2031 -9.4; 2234 -12.2; 2457 -15.0; 2703 -15.1; 2973 -11.6; 3270 -5.7; 3597 -1.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundMAGIC PL50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundMAGIC PL50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 0.53 | -2.7 dB  |
| Peaking | 93 Hz   | 0.49 | -3.2 dB  |
| Peaking | 385 Hz  | 0.71 | -3.3 dB  |
| Peaking | 2638 Hz | 2.66 | -13.5 dB |
| Peaking | 4167 Hz | 1.16 | 9.0 dB   |
| Peaking | 1465 Hz | 0.94 | -0.8 dB  |
| Peaking | 1475 Hz | 1.73 | 1.4 dB   |
| Peaking | 6345 Hz | 3.4  | 4.1 dB   |
| Peaking | 7437 Hz | 2.5  | -1.9 dB  |
| Peaking | 7803 Hz | 0.88 | -1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -3.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/SoundMAGIC%20PL50/SoundMAGIC%20PL50.png)