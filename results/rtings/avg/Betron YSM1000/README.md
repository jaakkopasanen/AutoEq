# Betron YSM1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.6; 23 -5.7; 25 -5.8; 28 -6.0; 31 -6.1; 34 -6.2; 37 -6.3; 41 -6.4; 45 -6.5; 49 -6.7; 54 -7.0; 60 -7.5; 66 -8.0; 72 -8.4; 79 -8.9; 87 -9.5; 96 -10.2; 106 -10.8; 116 -11.5; 128 -12.1; 141 -12.5; 155 -12.9; 170 -13.0; 187 -13.0; 206 -13.1; 227 -13.0; 249 -12.8; 274 -12.4; 302 -11.8; 332 -11.3; 365 -10.6; 402 -10.0; 442 -9.2; 486 -8.4; 535 -7.4; 588 -6.4; 647 -5.3; 712 -4.4; 783 -3.6; 861 -3.0; 947 -2.8; 1042 -2.7; 1146 -2.4; 1261 -1.8; 1387 -1.0; 1526 -2.6; 1678 -4.5; 1846 -4.5; 2031 -3.8; 2234 -2.3; 2457 -1.0; 2703 -0.7; 2973 -1.5; 3270 -2.9; 3597 -4.7; 3957 -6.4; 4353 -8.7; 4788 -10.9; 5267 -11.3; 5793 -6.5; 6373 -2.5; 7010 -0.5; 7711 -2.5; 8482 -2.7; 9330 -3.4; 10263 -2.8; 11289 -2.8; 12418 -2.8; 13660 -2.8; 15026 -3.1; 16529 -5.6; 18182 -5.0; 20000 -8.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Betron YSM1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Betron YSM1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 36 Hz    | 0.18 | -2.5 dB  |
| Peaking | 160 Hz   | 0.66 | -7.1 dB  |
| Peaking | 345 Hz   | 0.84 | -5.5 dB  |
| Peaking | 1640 Hz  | 0.16 | 1.3 dB   |
| Peaking | 4874 Hz  | 3.16 | -10.5 dB |
| Peaking | 1412 Hz  | 2.8  | 2.7 dB   |
| Peaking | 1742 Hz  | 2.49 | -4.0 dB  |
| Peaking | 2614 Hz  | 4.11 | 2.3 dB   |
| Peaking | 6856 Hz  | 5.24 | 3.4 dB   |
| Peaking | 21148 Hz | 0.07 | -2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -7.7 dB |
| Peaking | 250 Hz   | 1.41 | -9.1 dB |
| Peaking | 500 Hz   | 1.41 | -3.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.0 dB |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -2.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Betron%20YSM1000/Betron%20YSM1000.png)