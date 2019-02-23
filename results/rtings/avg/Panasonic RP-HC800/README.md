# Panasonic RP-HC800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.2; 23 -12.1; 25 -12.0; 28 -11.8; 31 -11.7; 34 -11.6; 37 -11.4; 41 -11.3; 45 -11.1; 49 -11.0; 54 -10.8; 60 -10.8; 66 -10.8; 72 -10.9; 79 -11.0; 87 -11.1; 96 -11.3; 106 -11.4; 116 -11.6; 128 -11.8; 141 -11.9; 155 -12.0; 170 -12.1; 187 -11.9; 206 -11.7; 227 -11.4; 249 -11.2; 274 -11.0; 302 -10.7; 332 -10.4; 365 -10.0; 402 -9.6; 442 -9.1; 486 -8.3; 535 -7.1; 588 -5.7; 647 -3.4; 712 -0.9; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -1.0; 1261 -1.9; 1387 -1.4; 1526 -1.0; 1678 -1.1; 1846 -2.7; 2031 -3.7; 2234 -5.2; 2457 -5.3; 2703 -2.4; 2973 -0.5; 3270 -1.7; 3597 -2.7; 3957 -3.9; 4353 -6.5; 4788 -7.3; 5267 -6.8; 5793 -9.7; 6373 -13.4; 7010 -8.9; 7711 -6.1; 8482 -8.4; 9330 -10.0; 10263 -9.8; 11289 -11.3; 12418 -11.5; 13660 -9.9; 15026 -10.6; 16529 -11.0; 18182 -9.9; 20000 -13.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.5  | -5.2 dB |
| Peaking | 968 Hz  | 0.63 | 12.4 dB |
| Peaking | 3246 Hz | 2.16 | 6.8 dB  |
| Peaking | 4473 Hz | 0.02 | -9.2 dB |
| Peaking | 7763 Hz | 0.1  | 5.3 dB  |
| Peaking | 1518 Hz | 5.28 | 2.4 dB  |
| Peaking | 1600 Hz | 1.92 | -3.0 dB |
| Peaking | 1715 Hz | 4.41 | 3.8 dB  |
| Peaking | 6396 Hz | 8.43 | -5.4 dB |
| Peaking | 7666 Hz | 5.57 | 4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB |
| Peaking | 16000 Hz | 1.41 | -6.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Panasonic%20RP-HC800/Panasonic%20RP-HC800.png)