# Dita Audio Answer
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -5.2; 25 -5.6; 28 -6.0; 31 -6.3; 34 -6.6; 37 -6.8; 41 -7.0; 45 -7.2; 49 -7.4; 54 -7.6; 60 -7.7; 66 -8.0; 72 -8.2; 79 -8.4; 87 -8.7; 96 -9.0; 106 -9.3; 116 -9.5; 128 -9.7; 141 -9.9; 155 -10.0; 170 -10.0; 187 -10.0; 206 -10.1; 227 -10.2; 249 -10.2; 274 -10.1; 302 -10.0; 332 -9.8; 365 -9.6; 402 -9.4; 442 -9.2; 486 -8.9; 535 -8.5; 588 -8.1; 647 -7.7; 712 -7.1; 783 -6.4; 861 -5.8; 947 -5.3; 1042 -5.1; 1146 -5.1; 1261 -5.4; 1387 -5.3; 1526 -4.5; 1678 -3.3; 1846 -2.2; 2031 -1.3; 2234 -0.6; 2457 -0.5; 2703 -0.6; 2973 -1.1; 3270 -1.9; 3597 -3.0; 3957 -4.0; 4353 -5.2; 4788 -7.1; 5267 -8.0; 5793 -6.1; 6373 -3.8; 7010 -4.1; 7711 -7.0; 8482 -8.2; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -9.4; 20000 -14.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dita Audio Answer GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dita Audio Answer ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.8  | 2.0 dB  |
| Peaking | 205 Hz   | 0.46 | -3.9 dB |
| Peaking | 2211 Hz  | 1.3  | 5.4 dB  |
| Peaking | 3034 Hz  | 2.9  | 2.5 dB  |
| Peaking | 19658 Hz | 1.46 | -8.2 dB |
| Peaking | 941 Hz   | 4.25 | 1.4 dB  |
| Peaking | 5209 Hz  | 5.12 | -3.2 dB |
| Peaking | 6664 Hz  | 3.78 | 3.4 dB  |
| Peaking | 8127 Hz  | 5.39 | -2.8 dB |
| Peaking | 16793 Hz | 3.07 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Dita%20Audio%20Answer/Dita%20Audio%20Answer.png)