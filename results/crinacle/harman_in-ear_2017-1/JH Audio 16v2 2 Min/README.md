# JH Audio 16v2 2 Min
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.4; 25 -5.6; 28 -5.9; 31 -6.2; 34 -6.5; 37 -6.7; 41 -7.0; 45 -7.3; 49 -7.6; 54 -7.9; 60 -8.3; 66 -8.6; 72 -9.0; 79 -9.4; 87 -9.9; 96 -10.4; 106 -10.8; 116 -11.1; 128 -11.5; 141 -11.8; 155 -12.0; 170 -12.1; 187 -12.2; 206 -12.2; 227 -12.2; 249 -12.0; 274 -11.9; 302 -11.7; 332 -11.3; 365 -11.0; 402 -10.7; 442 -10.4; 486 -10.0; 535 -9.6; 588 -9.2; 647 -8.7; 712 -8.1; 783 -7.6; 861 -7.1; 947 -6.9; 1042 -6.9; 1146 -6.8; 1261 -6.6; 1387 -6.1; 1526 -5.3; 1678 -4.3; 1846 -3.4; 2031 -2.6; 2234 -2.0; 2457 -1.5; 2703 -0.8; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -9.3; 9330 -12.5; 10263 -8.4; 11289 -6.5; 12418 -6.5; 13660 -8.7; 15026 -18.2; 16529 -22.3; 18182 -24.7; 20000 -27.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio 16v2 2 Min GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio 16v2 2 Min ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.41 | 2.0 dB   |
| Peaking | 162 Hz   | 0.64 | -1.4 dB  |
| Peaking | 230 Hz   | 0.35 | -4.6 dB  |
| Peaking | 4013 Hz  | 0.6  | 7.4 dB   |
| Peaking | 19159 Hz | 0.53 | -21.7 dB |
| Peaking | 1319 Hz  | 5.65 | -1.0 dB  |
| Peaking | 6203 Hz  | 5.86 | 2.1 dB   |
| Peaking | 9232 Hz  | 3.65 | -7.5 dB  |
| Peaking | 13039 Hz | 1.42 | 9.0 dB   |
| Peaking | 15404 Hz | 1.63 | -7.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB   |
| Peaking | 62 Hz    | 1.41 | -1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.3 dB  |
| Peaking | 250 Hz   | 1.41 | -5.0 dB  |
| Peaking | 500 Hz   | 1.41 | -2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 16000 Hz | 1.41 | -18.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/JH%20Audio%2016v2%202%20Min/JH%20Audio%2016v2%202%20Min.png)