# HiFi BOY OS V3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.5; 25 -7.7; 28 -7.9; 31 -8.0; 34 -8.1; 37 -8.2; 41 -8.3; 45 -8.5; 49 -8.6; 54 -8.8; 60 -8.9; 66 -9.2; 72 -9.4; 79 -9.7; 87 -10.0; 96 -10.3; 106 -10.6; 116 -10.8; 128 -11.1; 141 -11.1; 155 -11.2; 170 -11.3; 187 -11.2; 206 -11.1; 227 -10.9; 249 -10.6; 274 -10.4; 302 -10.0; 332 -9.6; 365 -9.1; 402 -8.7; 442 -8.2; 486 -7.5; 535 -7.2; 588 -6.6; 647 -5.9; 712 -5.1; 783 -4.4; 861 -3.8; 947 -3.4; 1042 -3.7; 1146 -5.1; 1261 -6.0; 1387 -5.7; 1526 -5.2; 1678 -4.3; 1846 -3.5; 2031 -2.9; 2234 -2.5; 2457 -2.5; 2703 -2.8; 2973 -3.2; 3270 -3.1; 3597 -1.9; 3957 -0.6; 4353 -1.4; 4788 -3.0; 5267 -2.5; 5793 -0.5; 6373 -0.7; 7010 -3.8; 7711 -9.3; 8482 -9.3; 9330 -6.1; 10263 -6.1; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFi BOY OS V3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFi BOY OS V3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 62 Hz   | 0.25 | -1.6 dB |
| Peaking | 185 Hz  | 0.53 | -4.1 dB |
| Peaking | 874 Hz  | 2.22 | 3.2 dB  |
| Peaking | 2236 Hz | 2.23 | 3.0 dB  |
| Peaking | 4485 Hz | 1.38 | 4.8 dB  |
| Peaking | 1294 Hz | 7.79 | -1.0 dB |
| Peaking | 3999 Hz | 6.33 | 1.5 dB  |
| Peaking | 4926 Hz | 3.4  | -3.2 dB |
| Peaking | 6262 Hz | 2.61 | 5.2 dB  |
| Peaking | 7951 Hz | 4.25 | -6.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/HiFi%20BOY%20OS%20V3/HiFi%20BOY%20OS%20V3.png)