# qdc Anole V6 Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -9.8; 25 -9.8; 28 -9.8; 31 -9.9; 34 -9.9; 37 -9.9; 41 -10.0; 45 -10.0; 49 -9.9; 54 -9.9; 60 -9.9; 66 -10.0; 72 -10.1; 79 -10.1; 87 -10.2; 96 -10.3; 106 -10.3; 116 -10.3; 128 -10.2; 141 -10.1; 155 -9.9; 170 -9.7; 187 -9.4; 206 -9.1; 227 -8.7; 249 -8.4; 274 -8.0; 302 -7.6; 332 -7.3; 365 -7.1; 402 -6.8; 442 -6.6; 486 -6.4; 535 -6.3; 588 -6.2; 647 -6.1; 712 -5.9; 783 -5.8; 861 -5.7; 947 -5.9; 1042 -6.3; 1146 -7.2; 1261 -8.0; 1387 -8.6; 1526 -8.6; 1678 -8.3; 1846 -7.8; 2031 -7.4; 2234 -6.9; 2457 -6.2; 2703 -5.3; 2973 -4.6; 3270 -4.5; 3597 -4.5; 3957 -4.9; 4353 -4.4; 4788 -1.4; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.1; 7711 -6.9; 8482 -9.7; 9330 -7.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.5; 15026 -12.6; 16529 -12.6; 18182 -13.1; 20000 -20.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole V6 Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole V6 Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 63 Hz    | 0.31 | -4.0 dB  |
| Peaking | 1558 Hz  | 2.92 | -2.4 dB  |
| Peaking | 3133 Hz  | 3.41 | 1.8 dB   |
| Peaking | 5560 Hz  | 2.55 | 7.2 dB   |
| Peaking | 20308 Hz | 0.34 | -11.7 dB |
| Peaking | 20 Hz    | 2.22 | -0.9 dB  |
| Peaking | 698 Hz   | 1.53 | 1.1 dB   |
| Peaking | 8537 Hz  | 6.73 | -4.0 dB  |
| Peaking | 11700 Hz | 3.03 | 2.2 dB   |
| Peaking | 18305 Hz | 4.94 | 1.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -8.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/qdc%20Anole%20V6%20Bass/qdc%20Anole%20V6%20Bass.png)