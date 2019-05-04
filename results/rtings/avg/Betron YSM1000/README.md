# Betron YSM1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.8; 25 -9.9; 28 -10.1; 31 -10.2; 34 -10.3; 37 -10.4; 41 -10.5; 45 -10.7; 49 -10.8; 54 -11.0; 60 -11.2; 66 -11.5; 72 -11.7; 79 -12.0; 87 -12.3; 96 -12.5; 106 -12.8; 116 -13.0; 128 -13.1; 141 -13.1; 155 -13.0; 170 -12.8; 187 -12.7; 206 -12.4; 227 -12.2; 249 -12.0; 274 -11.6; 302 -11.0; 332 -10.5; 365 -9.8; 402 -9.2; 442 -8.5; 486 -7.7; 535 -6.7; 588 -5.7; 647 -4.7; 712 -3.8; 783 -3.0; 861 -2.4; 947 -2.1; 1042 -2.0; 1146 -1.9; 1261 -1.2; 1387 -0.5; 1526 -2.1; 1678 -4.0; 1846 -4.1; 2031 -3.5; 2234 -2.5; 2457 -1.2; 2703 -0.6; 2973 -0.8; 3270 -2.0; 3597 -3.6; 3957 -5.3; 4353 -7.5; 4788 -10.6; 5267 -10.8; 5793 -5.7; 6373 -1.0; 7010 -3.5; 7711 -5.7; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -7.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Betron YSM1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Betron YSM1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.14 | -3.2 dB |
| Peaking | 198 Hz  | 0.38 | -6.0 dB |
| Peaking | 995 Hz  | 0.77 | 5.7 dB  |
| Peaking | 2860 Hz | 2.46 | 4.8 dB  |
| Peaking | 4932 Hz | 6.47 | -6.9 dB |
| Peaking | 1409 Hz | 7.08 | 2.1 dB  |
| Peaking | 1732 Hz | 4.98 | -1.7 dB |
| Peaking | 5474 Hz | 7.9  | -2.7 dB |
| Peaking | 6438 Hz | 4.41 | 6.8 dB  |
| Peaking | 6713 Hz | 1.41 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Betron%20YSM1000/Betron%20YSM1000.png)