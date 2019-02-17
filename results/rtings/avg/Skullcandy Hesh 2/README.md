# Skullcandy Hesh 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.9; 28 -1.5; 31 -2.0; 34 -2.4; 37 -2.6; 41 -2.7; 45 -2.9; 49 -3.1; 54 -3.5; 60 -4.0; 66 -4.4; 72 -5.0; 79 -5.5; 87 -6.1; 96 -6.6; 106 -7.2; 116 -7.5; 128 -7.6; 141 -7.5; 155 -7.3; 170 -7.2; 187 -6.8; 206 -5.7; 227 -4.5; 249 -3.3; 274 -2.2; 302 -1.0; 332 -0.5; 365 -0.5; 402 -0.5; 442 -0.5; 486 -0.5; 535 -0.6; 588 -2.2; 647 -4.5; 712 -5.9; 783 -6.3; 861 -6.4; 947 -6.4; 1042 -6.5; 1146 -6.0; 1261 -4.7; 1387 -4.0; 1526 -3.2; 1678 -2.7; 1846 -2.7; 2031 -2.0; 2234 -0.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.3; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Hesh 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Hesh 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.83 | 5.8 dB  |
| Peaking | 52 Hz   | 1.13 | 2.0 dB  |
| Peaking | 139 Hz  | 1.16 | -2.5 dB |
| Peaking | 372 Hz  | 1.28 | 7.0 dB  |
| Peaking | 3492 Hz | 0.74 | 6.7 dB  |
| Peaking | 541 Hz  | 4.09 | 3.3 dB  |
| Peaking | 905 Hz  | 1    | -2.8 dB |
| Peaking | 1655 Hz | 1.01 | 2.0 dB  |
| Peaking | 6014 Hz | 2.21 | 7.1 dB  |
| Peaking | 6453 Hz | 0.96 | -4.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.3 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | 3.0 dB  |
| Peaking | 500 Hz   | 1.41 | 6.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Hesh%202/Skullcandy%20Hesh%202.png)