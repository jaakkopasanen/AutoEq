# Acoustune HS1004 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.4; 25 -5.9; 28 -6.4; 31 -6.9; 34 -7.2; 37 -7.6; 41 -8.0; 45 -8.3; 49 -8.6; 54 -8.8; 60 -9.1; 66 -9.5; 72 -9.8; 79 -10.0; 87 -10.3; 96 -10.6; 106 -10.8; 116 -10.9; 128 -11.0; 141 -11.1; 155 -11.0; 170 -10.9; 187 -10.7; 206 -10.3; 227 -10.0; 249 -9.7; 274 -9.3; 302 -8.9; 332 -8.4; 365 -8.0; 402 -7.6; 442 -7.2; 486 -6.8; 535 -6.4; 588 -6.1; 647 -5.7; 712 -5.2; 783 -4.8; 861 -4.5; 947 -4.6; 1042 -5.1; 1146 -6.1; 1261 -7.0; 1387 -7.7; 1526 -7.8; 1678 -7.4; 1846 -6.5; 2031 -5.5; 2234 -4.2; 2457 -2.6; 2703 -1.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.3; 4788 -3.7; 5267 -4.4; 5793 -5.7; 6373 -7.3; 7010 -7.4; 7711 -8.5; 8482 -10.5; 9330 -8.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.3; 15026 -9.6; 16529 -7.7; 18182 -8.9; 20000 -14.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Acoustune HS1004 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Acoustune HS1004 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 101 Hz   | 0.77 | -3.8 dB |
| Peaking | 204 Hz   | 1.27 | -2.5 dB |
| Peaking | 3442 Hz  | 1.57 | 7.0 dB  |
| Peaking | 8309 Hz  | 3.5  | -4.3 dB |
| Peaking | 20436 Hz | 0.59 | -7.4 dB |
| Peaking | 19 Hz    | 2.35 | 1.8 dB  |
| Peaking | 885 Hz   | 1.82 | 2.7 dB  |
| Peaking | 1477 Hz  | 1.75 | -2.6 dB |
| Peaking | 2618 Hz  | 4.85 | 1.7 dB  |
| Peaking | 21273 Hz | 3.14 | -0.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Acoustune%20HS1004%20sample%202/Acoustune%20HS1004%20sample%202.png)