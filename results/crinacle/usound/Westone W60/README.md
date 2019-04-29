# Westone W60
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -7.8; 25 -7.9; 28 -8.1; 31 -8.2; 34 -8.3; 37 -8.5; 41 -8.6; 45 -8.7; 49 -8.9; 54 -9.1; 60 -9.3; 66 -9.6; 72 -9.9; 79 -10.3; 87 -10.7; 96 -11.1; 106 -11.5; 116 -11.7; 128 -12.0; 141 -12.3; 155 -12.5; 170 -12.6; 187 -12.6; 206 -12.6; 227 -12.5; 249 -12.3; 274 -12.1; 302 -11.8; 332 -11.5; 365 -11.1; 402 -10.7; 442 -10.3; 486 -9.8; 535 -9.2; 588 -8.6; 647 -8.0; 712 -7.2; 783 -6.5; 861 -5.8; 947 -5.4; 1042 -5.5; 1146 -6.1; 1261 -6.8; 1387 -7.3; 1526 -7.1; 1678 -6.1; 1846 -4.4; 2031 -2.1; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.7; 3270 -1.4; 3597 -1.2; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.4; 8482 -9.7; 9330 -6.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.0; 15026 -9.8; 16529 -9.4; 18182 -9.5; 20000 -12.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W60 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 102 Hz   | 0.43 | -3.0 dB |
| Peaking | 243 Hz   | 0.65 | -4.3 dB |
| Peaking | 2582 Hz  | 1.81 | 5.8 dB  |
| Peaking | 5001 Hz  | 1.63 | 6.3 dB  |
| Peaking | 19918 Hz | 0.27 | -4.1 dB |
| Peaking | 941 Hz   | 3.11 | 1.9 dB  |
| Peaking | 1464 Hz  | 4.08 | -2.1 dB |
| Peaking | 6418 Hz  | 6.23 | 2.5 dB  |
| Peaking | 8267 Hz  | 5.33 | -4.7 dB |
| Peaking | 12360 Hz | 2.96 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -5.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -3.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Westone%20W60/Westone%20W60.png)