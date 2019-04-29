# Acoustune HS1503
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.7; 23 -11.7; 25 -11.7; 28 -11.6; 31 -11.5; 34 -11.4; 37 -11.3; 41 -11.2; 45 -11.0; 49 -10.9; 54 -10.7; 60 -10.6; 66 -10.6; 72 -10.5; 79 -10.4; 87 -10.4; 96 -10.3; 106 -10.3; 116 -10.1; 128 -10.0; 141 -9.7; 155 -9.5; 170 -9.1; 187 -8.8; 206 -8.3; 227 -7.8; 249 -7.3; 274 -6.8; 302 -6.2; 332 -5.7; 365 -5.1; 402 -4.6; 442 -4.1; 486 -3.6; 535 -3.1; 588 -2.6; 647 -2.1; 712 -1.6; 783 -1.0; 861 -0.7; 947 -0.5; 1042 -0.7; 1146 -1.3; 1261 -1.9; 1387 -2.1; 1526 -1.9; 1678 -1.5; 1846 -1.0; 2031 -0.9; 2234 -1.2; 2457 -2.1; 2703 -3.7; 2973 -5.8; 3270 -7.4; 3597 -7.2; 3957 -6.4; 4353 -6.3; 4788 -7.4; 5267 -10.9; 5793 -14.0; 6373 -10.0; 7010 -8.1; 7711 -11.0; 8482 -11.3; 9330 -6.0; 10263 -5.6; 11289 -5.6; 12418 -6.3; 13660 -6.9; 15026 -5.6; 16529 -5.6; 18182 -7.1; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Acoustune HS1503 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Acoustune HS1503 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.41 | -5.6 dB  |
| Peaking | 134 Hz   | 0.43 | -4.0 dB  |
| Peaking | 1069 Hz  | 0.39 | 5.2 dB   |
| Peaking | 5956 Hz  | 1.27 | -6.9 dB  |
| Peaking | 18256 Hz | 2.73 | -1.5 dB  |
| Peaking | 2227 Hz  | 2.62 | 3.5 dB   |
| Peaking | 4681 Hz  | 2.54 | 9.9 dB   |
| Peaking | 5460 Hz  | 0.99 | -15.7 dB |
| Peaking | 7127 Hz  | 1.25 | 14.8 dB  |
| Peaking | 8038 Hz  | 4.39 | -9.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.8 dB |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Acoustune%20HS1503/Acoustune%20HS1503.png)