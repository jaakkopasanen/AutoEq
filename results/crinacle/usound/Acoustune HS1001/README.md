# Acoustune HS1001
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.8; 23 -11.9; 25 -12.0; 28 -12.1; 31 -12.1; 34 -12.1; 37 -12.2; 41 -12.2; 45 -12.2; 49 -12.2; 54 -12.1; 60 -12.1; 66 -12.1; 72 -12.2; 79 -12.3; 87 -12.3; 96 -12.4; 106 -12.4; 116 -12.3; 128 -12.2; 141 -12.0; 155 -11.8; 170 -11.5; 187 -11.1; 206 -10.7; 227 -10.2; 249 -9.6; 274 -9.0; 302 -8.4; 332 -7.8; 365 -7.1; 402 -6.5; 442 -5.9; 486 -5.1; 535 -4.4; 588 -3.7; 647 -3.0; 712 -2.2; 783 -1.4; 861 -0.8; 947 -0.5; 1042 -0.6; 1146 -1.2; 1261 -2.0; 1387 -2.5; 1526 -2.6; 1678 -2.3; 1846 -2.0; 2031 -1.8; 2234 -1.9; 2457 -2.4; 2703 -3.1; 2973 -3.7; 3270 -3.7; 3597 -3.3; 3957 -3.0; 4353 -3.3; 4788 -4.7; 5267 -7.7; 5793 -10.9; 6373 -8.9; 7010 -7.3; 7711 -9.5; 8482 -9.6; 9330 -6.0; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -6.0; 15026 -8.9; 16529 -8.9; 18182 -6.1; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Acoustune HS1001 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Acoustune HS1001 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 98 Hz    | 0.11 | -7.0 dB |
| Peaking | 840 Hz   | 0.47 | 8.1 dB  |
| Peaking | 4658 Hz  | 1.57 | 7.3 dB  |
| Peaking | 5606 Hz  | 1.57 | -9.4 dB |
| Peaking | 15930 Hz | 2.71 | -3.9 dB |
| Peaking | 1431 Hz  | 4.81 | -1.3 dB |
| Peaking | 2169 Hz  | 4.18 | 1.2 dB  |
| Peaking | 6915 Hz  | 7.47 | 2.7 dB  |
| Peaking | 8262 Hz  | 3.36 | -4.5 dB |
| Peaking | 9325 Hz  | 2.4  | 2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Acoustune%20HS1001/Acoustune%20HS1001.png)