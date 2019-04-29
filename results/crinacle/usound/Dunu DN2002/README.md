# Dunu DN2002
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.3; 23 -8.4; 25 -8.5; 28 -8.6; 31 -8.7; 34 -8.8; 37 -9.0; 41 -9.1; 45 -9.2; 49 -9.3; 54 -9.4; 60 -9.6; 66 -9.8; 72 -10.0; 79 -10.2; 87 -10.5; 96 -10.7; 106 -10.9; 116 -11.1; 128 -11.2; 141 -11.2; 155 -11.3; 170 -11.2; 187 -11.1; 206 -11.0; 227 -10.8; 249 -10.6; 274 -10.4; 302 -10.2; 332 -10.0; 365 -9.8; 402 -9.6; 442 -9.3; 486 -9.1; 535 -8.8; 588 -8.5; 647 -8.2; 712 -7.7; 783 -7.2; 861 -6.6; 947 -6.2; 1042 -5.8; 1146 -6.1; 1261 -6.5; 1387 -6.5; 1526 -5.9; 1678 -4.8; 1846 -3.4; 2031 -2.2; 2234 -1.2; 2457 -0.5; 2703 -0.5; 2973 -1.6; 3270 -3.4; 3597 -3.0; 3957 -1.8; 4353 -3.7; 4788 -5.6; 5267 -2.9; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -8.1; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu DN2002 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN2002 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.48 | -1.4 dB |
| Peaking | 166 Hz  | 0.37 | -4.7 dB |
| Peaking | 2304 Hz | 2.6  | 2.7 dB  |
| Peaking | 2817 Hz | 1.25 | 4.0 dB  |
| Peaking | 6005 Hz | 4.48 | 5.9 dB  |
| Peaking | 1008 Hz | 3.92 | 1.0 dB  |
| Peaking | 1383 Hz | 4.95 | -1.0 dB |
| Peaking | 3322 Hz | 8.9  | -1.4 dB |
| Peaking | 3932 Hz | 9.37 | 2.3 dB  |
| Peaking | 8544 Hz | 6.45 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Dunu%20DN2002/Dunu%20DN2002.png)