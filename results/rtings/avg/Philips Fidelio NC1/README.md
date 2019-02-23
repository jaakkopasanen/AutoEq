# Philips Fidelio NC1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -3.8; 25 -3.6; 28 -3.3; 31 -2.9; 34 -2.6; 37 -2.3; 41 -1.9; 45 -1.7; 49 -1.6; 54 -1.5; 60 -1.4; 66 -1.3; 72 -1.0; 79 -0.7; 87 -0.5; 96 -0.6; 106 -1.0; 116 -1.4; 128 -1.9; 141 -2.4; 155 -2.8; 170 -3.1; 187 -3.4; 206 -3.6; 227 -3.8; 249 -4.1; 274 -4.0; 302 -3.8; 332 -3.7; 365 -3.6; 402 -3.6; 442 -3.6; 486 -3.6; 535 -3.5; 588 -3.3; 647 -3.2; 712 -3.0; 783 -2.8; 861 -2.5; 947 -2.2; 1042 -2.0; 1146 -1.7; 1261 -1.5; 1387 -2.3; 1526 -2.6; 1678 -2.5; 1846 -3.2; 2031 -4.0; 2234 -4.4; 2457 -4.9; 2703 -6.1; 2973 -7.8; 3270 -9.6; 3597 -10.8; 3957 -10.7; 4353 -9.3; 4788 -6.4; 5267 -4.1; 5793 -5.0; 6373 -7.9; 7010 -6.2; 7711 -4.1; 8482 -4.0; 9330 -4.0; 10263 -4.0; 11289 -4.0; 12418 -4.0; 13660 -4.0; 15026 -4.0; 16529 -6.8; 18182 -12.2; 20000 -10.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio NC1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio NC1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 44 Hz    | 1.55 | 1.5 dB  |
| Peaking | 90 Hz    | 1.13 | 3.3 dB  |
| Peaking | 3737 Hz  | 2.65 | -7.6 dB |
| Peaking | 17867 Hz | 2.9  | -5.4 dB |
| Peaking | 19350 Hz | 1.47 | -8.0 dB |
| Peaking | 1196 Hz  | 1.15 | 2.4 dB  |
| Peaking | 3048 Hz  | 4.78 | -1.3 dB |
| Peaking | 5404 Hz  | 7.44 | 2.2 dB  |
| Peaking | 6432 Hz  | 6.25 | -3.6 dB |
| Peaking | 14501 Hz | 1.61 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | 2.0 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -6.5 dB |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Philips%20Fidelio%20NC1/Philips%20Fidelio%20NC1.png)