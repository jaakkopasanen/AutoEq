# Whizzer A15 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.6; 72 -1.0; 79 -1.4; 87 -1.8; 96 -2.4; 106 -2.9; 116 -3.4; 128 -3.9; 141 -4.3; 155 -4.8; 170 -5.1; 187 -5.4; 206 -5.7; 227 -5.9; 249 -6.1; 274 -6.2; 302 -6.3; 332 -6.4; 365 -6.5; 402 -6.4; 442 -6.3; 486 -6.3; 535 -6.4; 588 -6.4; 647 -6.4; 712 -6.2; 783 -6.0; 861 -5.8; 947 -5.8; 1042 -6.1; 1146 -6.9; 1261 -7.8; 1387 -8.5; 1526 -8.6; 1678 -8.4; 1846 -8.1; 2031 -8.0; 2234 -8.1; 2457 -8.3; 2703 -8.6; 2973 -8.7; 3270 -8.5; 3597 -8.1; 3957 -7.9; 4353 -7.9; 4788 -7.9; 5267 -7.1; 5793 -5.5; 6373 -3.9; 7010 -4.1; 7711 -7.3; 8482 -9.2; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.6; 15026 -11.3; 16529 -11.6; 18182 -12.0; 20000 -11.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Whizzer A15 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Whizzer A15 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.42 | 6.6 dB  |
| Peaking | 1510 Hz  | 3.84 | -1.8 dB |
| Peaking | 3103 Hz  | 1.02 | -2.1 dB |
| Peaking | 6504 Hz  | 5.29 | 4.1 dB  |
| Peaking | 18463 Hz | 0.65 | -6.3 dB |
| Peaking | 38 Hz    | 3.09 | -0.7 dB |
| Peaking | 917 Hz   | 4.3  | 1.1 dB  |
| Peaking | 8353 Hz  | 7.47 | -3.3 dB |
| Peaking | 13485 Hz | 1.11 | 2.8 dB  |
| Peaking | 14921 Hz | 2.38 | -4.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 5.0 dB  |
| Peaking | 125 Hz   | 1.41 | 1.8 dB  |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -6.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Whizzer%20A15%20Pro/Whizzer%20A15%20Pro.png)