# Axelvox HD 272
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.1; 45 -1.4; 49 -1.6; 54 -1.7; 60 -1.6; 66 -1.2; 72 -0.7; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.7; 249 -2.4; 274 -4.3; 302 -5.9; 332 -7.1; 365 -7.8; 402 -8.1; 442 -7.9; 486 -6.8; 535 -5.8; 588 -5.9; 647 -6.6; 712 -7.0; 783 -7.1; 861 -7.1; 947 -7.1; 1042 -7.4; 1146 -7.5; 1261 -7.8; 1387 -7.8; 1526 -7.7; 1678 -7.2; 1846 -7.2; 2031 -8.0; 2234 -8.7; 2457 -8.5; 2703 -7.7; 2973 -7.1; 3270 -6.6; 3597 -5.6; 3957 -3.4; 4353 -5.8; 4788 -11.5; 5267 -13.3; 5793 -12.3; 6373 -12.1; 7010 -14.5; 7711 -16.9; 8482 -16.9; 9330 -14.5; 10263 -12.5; 11289 -13.3; 12418 -14.9; 13660 -14.6; 15026 -11.8; 16529 -7.0; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Axelvox HD 272 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Axelvox HD 272 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.3  | 5.9 dB  |
| Peaking | 165 Hz   | 1.41 | 4.7 dB  |
| Peaking | 7893 Hz  | 1.48 | -9.8 dB |
| Peaking | 13288 Hz | 1.87 | -7.6 dB |
| Peaking | 22050 Hz | 2.11 | -6.8 dB |
| Peaking | 229 Hz   | 5.02 | 2.5 dB  |
| Peaking | 372 Hz   | 2.68 | -2.9 dB |
| Peaking | 1937 Hz  | 0.71 | -1.3 dB |
| Peaking | 4073 Hz  | 3.43 | 6.3 dB  |
| Peaking | 4971 Hz  | 4.83 | -5.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB   |
| Peaking | 62 Hz    | 1.41 | 3.3 dB   |
| Peaking | 125 Hz   | 1.41 | 5.9 dB   |
| Peaking | 250 Hz   | 1.41 | 2.8 dB   |
| Peaking | 500 Hz   | 1.41 | -1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 8000 Hz  | 1.41 | -12.1 dB |
| Peaking | 16000 Hz | 1.41 | -4.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Axelvox%20HD%20272/Axelvox%20HD%20272.png)