# Noble Audio Dulce Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.1; 23 -10.3; 25 -10.5; 28 -10.7; 31 -10.9; 34 -11.0; 37 -11.2; 41 -11.3; 45 -11.5; 49 -11.6; 54 -11.7; 60 -12.0; 66 -12.2; 72 -12.4; 79 -12.7; 87 -13.0; 96 -13.4; 106 -13.6; 116 -13.8; 128 -14.0; 141 -14.1; 155 -14.1; 170 -14.0; 187 -13.9; 206 -13.6; 227 -13.4; 249 -13.1; 274 -12.7; 302 -12.2; 332 -11.6; 365 -11.0; 402 -10.4; 442 -9.9; 486 -9.2; 535 -8.6; 588 -7.9; 647 -7.3; 712 -6.5; 783 -5.8; 861 -5.2; 947 -4.9; 1042 -4.9; 1146 -5.2; 1261 -5.5; 1387 -5.3; 1526 -4.8; 1678 -4.2; 1846 -3.7; 2031 -3.1; 2234 -2.4; 2457 -1.0; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -2.4; 4788 -4.0; 5267 -7.0; 5793 -9.8; 6373 -7.5; 7010 -5.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.9; 15026 -20.4; 16529 -27.4; 18182 -23.0; 20000 -10.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noble Audio Dulce Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble Audio Dulce Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 46 Hz    | 0.32 | -4.3 dB  |
| Peaking | 153 Hz   | 0.79 | -4.8 dB  |
| Peaking | 305 Hz   | 1.28 | -3.0 dB  |
| Peaking | 2965 Hz  | 1.07 | 6.6 dB   |
| Peaking | 17117 Hz | 1.6  | -23.5 dB |
| Peaking | 917 Hz   | 3.54 | 1.7 dB   |
| Peaking | 4028 Hz  | 5.47 | 1.7 dB   |
| Peaking | 5726 Hz  | 5.65 | -5.2 dB  |
| Peaking | 13380 Hz | 1.52 | 8.3 dB   |
| Peaking | 15393 Hz | 2.34 | -10.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB  |
| Peaking | 62 Hz    | 1.41 | -3.9 dB  |
| Peaking | 125 Hz   | 1.41 | -6.3 dB  |
| Peaking | 250 Hz   | 1.41 | -5.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 16000 Hz | 1.41 | -19.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Noble%20Audio%20Dulce%20Bass/Noble%20Audio%20Dulce%20Bass.png)