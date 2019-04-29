# Noble Audio Dulce Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -9.1; 25 -9.3; 28 -9.5; 31 -9.7; 34 -9.9; 37 -10.0; 41 -10.2; 45 -10.3; 49 -10.4; 54 -10.6; 60 -10.8; 66 -11.0; 72 -11.3; 79 -11.6; 87 -11.9; 96 -12.2; 106 -12.4; 116 -12.6; 128 -12.8; 141 -12.9; 155 -12.9; 170 -12.9; 187 -12.7; 206 -12.5; 227 -12.2; 249 -11.9; 274 -11.5; 302 -11.1; 332 -10.6; 365 -10.1; 402 -9.6; 442 -9.1; 486 -8.5; 535 -7.9; 588 -7.3; 647 -6.6; 712 -5.9; 783 -5.1; 861 -4.5; 947 -4.1; 1042 -4.1; 1146 -4.5; 1261 -5.0; 1387 -5.1; 1526 -4.9; 1678 -4.4; 1846 -3.9; 2031 -3.6; 2234 -3.5; 2457 -2.7; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.7; 4353 -3.6; 4788 -4.8; 5267 -7.9; 5793 -10.9; 6373 -9.0; 7010 -8.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.6; 18182 -6.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noble Audio Dulce Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble Audio Dulce Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.38 | -2.2 dB |
| Peaking | 170 Hz   | 0.45 | -6.0 dB |
| Peaking | 907 Hz   | 1.49 | 2.9 dB  |
| Peaking | 3293 Hz  | 1.2  | 6.7 dB  |
| Peaking | 5827 Hz  | 3.39 | -6.4 dB |
| Peaking | 1400 Hz  | 4.55 | -0.5 dB |
| Peaking | 1992 Hz  | 1.57 | 0.5 dB  |
| Peaking | 2298 Hz  | 6.76 | -1.0 dB |
| Peaking | 16967 Hz | 3.32 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Noble%20Audio%20Dulce%20Bass/Noble%20Audio%20Dulce%20Bass.png)