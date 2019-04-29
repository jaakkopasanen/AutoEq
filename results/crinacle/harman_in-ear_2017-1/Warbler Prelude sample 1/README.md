# Warbler Prelude sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.3; 25 -1.9; 28 -2.6; 31 -3.3; 34 -3.9; 37 -4.4; 41 -5.0; 45 -5.4; 49 -5.7; 54 -6.1; 60 -6.6; 66 -7.2; 72 -7.7; 79 -8.2; 87 -8.6; 96 -9.3; 106 -9.8; 116 -10.2; 128 -10.6; 141 -11.1; 155 -11.4; 170 -11.6; 187 -11.8; 206 -11.9; 227 -12.0; 249 -12.1; 274 -12.1; 302 -12.0; 332 -11.8; 365 -11.6; 402 -11.5; 442 -11.3; 486 -11.1; 535 -10.8; 588 -10.4; 647 -10.1; 712 -9.6; 783 -9.1; 861 -8.7; 947 -8.6; 1042 -8.7; 1146 -9.2; 1261 -9.7; 1387 -9.7; 1526 -9.3; 1678 -8.6; 1846 -7.7; 2031 -6.6; 2234 -5.5; 2457 -4.9; 2703 -4.6; 2973 -4.7; 3270 -4.7; 3597 -3.6; 3957 -1.6; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.7; 15026 -16.2; 16529 -9.2; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Warbler Prelude sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Warbler Prelude sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.49 | 7.2 dB   |
| Peaking | 245 Hz   | 0.37 | -5.8 dB  |
| Peaking | 1409 Hz  | 2.81 | -2.7 dB  |
| Peaking | 4921 Hz  | 1.38 | 6.8 dB   |
| Peaking | 15012 Hz | 3.23 | -10.9 dB |
| Peaking | 2498 Hz  | 2.95 | 2.6 dB   |
| Peaking | 2577 Hz  | 1.55 | -1.4 dB  |
| Peaking | 6406 Hz  | 5.56 | 2.4 dB   |
| Peaking | 7760 Hz  | 3.29 | -2.1 dB  |
| Peaking | 17599 Hz | 4.97 | 1.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -3.4 dB |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -6.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Warbler%20Prelude%20sample%201/Warbler%20Prelude%20sample%201.png)