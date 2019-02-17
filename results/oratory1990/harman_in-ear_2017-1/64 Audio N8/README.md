# 64 Audio N8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.9; 25 -7.4; 28 -7.5; 31 -7.5; 34 -7.7; 37 -7.7; 41 -7.8; 45 -8.0; 49 -8.1; 54 -8.5; 60 -8.7; 66 -9.1; 72 -9.0; 79 -9.3; 87 -9.5; 96 -9.0; 106 -9.4; 116 -9.3; 128 -9.4; 141 -9.4; 155 -9.4; 170 -9.4; 187 -9.6; 206 -9.6; 227 -9.5; 249 -9.5; 274 -9.5; 302 -9.3; 332 -9.2; 365 -8.9; 402 -8.8; 442 -8.7; 486 -8.4; 535 -8.2; 588 -7.9; 647 -7.5; 712 -7.1; 783 -6.7; 861 -6.3; 947 -6.2; 1042 -6.5; 1146 -7.1; 1261 -7.9; 1387 -8.3; 1526 -8.4; 1678 -8.2; 1846 -7.9; 2031 -7.3; 2234 -6.2; 2457 -4.8; 2703 -3.4; 2973 -2.3; 3270 -1.7; 3597 -1.8; 3957 -2.6; 4353 -3.5; 4788 -4.4; 5267 -3.9; 5793 -0.5; 6373 -0.8; 7010 -3.8; 7711 -6.0; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -16.2; 15026 -26.1; 16529 -25.3; 18182 -18.2; 20000 -10.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 142 Hz   | 0.44 | -1.8 dB  |
| Peaking | 364 Hz   | 0.09 | -1.6 dB  |
| Peaking | 5789 Hz  | 0.59 | 7.9 dB   |
| Peaking | 12285 Hz | 1.97 | 11.9 dB  |
| Peaking | 15412 Hz | 0.81 | -25.3 dB |
| Peaking | 960 Hz   | 1.17 | 4.7 dB   |
| Peaking | 1499 Hz  | 0.55 | -4.6 dB  |
| Peaking | 3142 Hz  | 1.31 | 5.1 dB   |
| Peaking | 5060 Hz  | 1.81 | -4.5 dB  |
| Peaking | 6022 Hz  | 4.31 | 5.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB  |
| Peaking | 250 Hz   | 1.41 | -2.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.3 dB   |
| Peaking | 16000 Hz | 1.41 | -22.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/64%20Audio%20N8/64%20Audio%20N8.png)