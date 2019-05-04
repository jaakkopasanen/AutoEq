# Logitech G430
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -4.0; 25 -4.8; 28 -5.9; 31 -6.8; 34 -7.6; 37 -8.1; 41 -8.7; 45 -9.1; 49 -9.3; 54 -9.4; 60 -9.4; 66 -9.3; 72 -9.1; 79 -9.0; 87 -9.1; 96 -9.4; 106 -9.6; 116 -9.6; 128 -9.4; 141 -9.2; 155 -9.1; 170 -8.7; 187 -8.3; 206 -7.9; 227 -7.5; 249 -7.6; 274 -7.3; 302 -6.3; 332 -5.5; 365 -4.7; 402 -3.9; 442 -3.3; 486 -3.7; 535 -4.7; 588 -5.4; 647 -5.6; 712 -5.6; 783 -5.5; 861 -5.3; 947 -5.1; 1042 -5.0; 1146 -5.1; 1261 -4.8; 1387 -4.6; 1526 -5.4; 1678 -5.7; 1846 -6.3; 2031 -6.5; 2234 -5.8; 2457 -4.1; 2703 -2.7; 2973 -2.2; 3270 -1.5; 3597 -0.5; 3957 -1.4; 4353 -5.2; 4788 -6.8; 5267 -6.8; 5793 -7.7; 6373 -7.9; 7010 -3.9; 7711 -5.1; 8482 -5.4; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.8; 13660 -5.4; 15026 -5.4; 16529 -5.7; 18182 -7.2; 20000 -12.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G430 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G430 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 20 Hz    |  1.41 | 5.4 dB  |
| Peaking | 67 Hz    |  0.24 | -4.3 dB |
| Peaking | 425 Hz   |  2.1  | 3.4 dB  |
| Peaking | 3617 Hz  |  2.34 | 6.4 dB  |
| Peaking | 4981 Hz  |  2.01 | -3.7 dB |
| Peaking | 1382 Hz  |  2.04 | 1.4 dB  |
| Peaking | 2136 Hz  |  1.45 | -2.4 dB |
| Peaking | 2602 Hz  |  3.58 | 2.6 dB  |
| Peaking | 7110 Hz  | 11.9  | 2.4 dB  |
| Peaking | 19842 Hz |  1.47 | -6.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Logitech%20G430/Logitech%20G430.png)