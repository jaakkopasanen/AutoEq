# Acoustune HS1003
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.7; 23 -8.8; 25 -8.8; 28 -8.9; 31 -9.0; 34 -9.0; 37 -9.0; 41 -9.0; 45 -9.0; 49 -9.0; 54 -9.0; 60 -9.0; 66 -9.0; 72 -9.1; 79 -9.1; 87 -9.1; 96 -9.2; 106 -9.2; 116 -9.2; 128 -9.0; 141 -8.9; 155 -8.7; 170 -8.4; 187 -8.1; 206 -7.7; 227 -7.3; 249 -6.8; 274 -6.3; 302 -5.8; 332 -5.4; 365 -4.9; 402 -4.4; 442 -4.0; 486 -3.6; 535 -3.1; 588 -2.6; 647 -2.1; 712 -1.6; 783 -1.0; 861 -0.6; 947 -0.5; 1042 -0.8; 1146 -1.4; 1261 -2.1; 1387 -2.5; 1526 -2.4; 1678 -2.1; 1846 -1.8; 2031 -1.8; 2234 -2.3; 2457 -3.2; 2703 -4.6; 2973 -5.8; 3270 -6.0; 3597 -5.3; 3957 -4.7; 4353 -4.9; 4788 -6.6; 5267 -9.7; 5793 -11.0; 6373 -7.6; 7010 -5.2; 7711 -7.1; 8482 -9.7; 9330 -6.9; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -6.0; 20000 -11.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Acoustune HS1003 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Acoustune HS1003 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.28 | -3.6 dB |
| Peaking | 145 Hz  | 0.77 | -2.5 dB |
| Peaking | 875 Hz  | 0.95 | 4.6 dB  |
| Peaking | 1996 Hz | 3.25 | 2.6 dB  |
| Peaking | 5665 Hz | 3.75 | -6.2 dB |
| Peaking | 3146 Hz | 5.51 | -1.6 dB |
| Peaking | 4242 Hz | 4.62 | 1.3 dB  |
| Peaking | 7039 Hz | 5.58 | 2.5 dB  |
| Peaking | 8588 Hz | 3.55 | -5.4 dB |
| Peaking | 9772 Hz | 3.55 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.5 dB |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Acoustune%20HS1003/Acoustune%20HS1003.png)