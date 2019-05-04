# Philips Fidelio NC1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -3.8; 25 -3.6; 28 -3.3; 31 -3.0; 34 -2.7; 37 -2.4; 41 -2.1; 45 -1.8; 49 -1.7; 54 -1.5; 60 -1.5; 66 -1.3; 72 -1.1; 79 -0.7; 87 -0.5; 96 -0.6; 106 -1.0; 116 -1.4; 128 -1.9; 141 -2.4; 155 -2.8; 170 -3.1; 187 -3.4; 206 -3.6; 227 -3.9; 249 -4.3; 274 -4.2; 302 -4.0; 332 -3.9; 365 -3.7; 402 -3.7; 442 -3.7; 486 -3.8; 535 -3.7; 588 -3.7; 647 -3.6; 712 -3.4; 783 -3.1; 861 -2.8; 947 -2.6; 1042 -2.4; 1146 -2.1; 1261 -2.0; 1387 -2.7; 1526 -3.1; 1678 -2.9; 1846 -3.8; 2031 -4.8; 2234 -5.5; 2457 -6.0; 2703 -6.9; 2973 -8.1; 3270 -9.6; 3597 -10.8; 3957 -10.6; 4353 -9.1; 4788 -7.0; 5267 -4.7; 5793 -5.2; 6373 -7.0; 7010 -6.6; 7711 -5.0; 8482 -4.2; 9330 -4.2; 10263 -4.2; 11289 -4.2; 12418 -4.2; 13660 -4.2; 15026 -4.2; 16529 -7.0; 18182 -12.3; 20000 -10.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio NC1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio NC1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 44 Hz    | 1.39 | 1.5 dB  |
| Peaking | 90 Hz    | 1.06 | 3.4 dB  |
| Peaking | 3682 Hz  | 2.57 | -7.2 dB |
| Peaking | 6686 Hz  | 6.03 | -2.2 dB |
| Peaking | 18856 Hz | 1.33 | -9.5 dB |
| Peaking | 1208 Hz  | 1.14 | 2.3 dB  |
| Peaking | 2526 Hz  | 2.53 | -1.2 dB |
| Peaking | 4455 Hz  | 6.71 | -1.1 dB |
| Peaking | 5302 Hz  | 8.2  | 1.6 dB  |
| Peaking | 14602 Hz | 2.12 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | 2.2 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -6.1 dB |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -2.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Philips%20Fidelio%20NC1/Philips%20Fidelio%20NC1.png)