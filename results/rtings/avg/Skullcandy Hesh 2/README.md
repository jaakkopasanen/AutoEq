# Skullcandy Hesh 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.4; 25 -5.0; 28 -5.7; 31 -6.2; 34 -6.6; 37 -6.8; 41 -7.0; 45 -7.2; 49 -7.5; 54 -7.8; 60 -8.2; 66 -8.7; 72 -9.1; 79 -9.6; 87 -10.2; 96 -10.8; 106 -11.3; 116 -11.7; 128 -11.8; 141 -11.7; 155 -11.5; 170 -11.4; 187 -11.0; 206 -10.0; 227 -8.8; 249 -7.6; 274 -6.5; 302 -5.4; 332 -4.3; 365 -3.7; 402 -3.7; 442 -4.2; 486 -4.5; 535 -5.0; 588 -6.7; 647 -9.0; 712 -10.4; 783 -10.9; 861 -10.8; 947 -10.9; 1042 -11.1; 1146 -10.4; 1261 -9.4; 1387 -8.6; 1526 -7.9; 1678 -7.3; 1846 -7.4; 2031 -6.8; 2234 -5.8; 2457 -4.5; 2703 -3.8; 2973 -4.1; 3270 -2.7; 3597 -0.6; 3957 -0.5; 4353 -5.1; 4788 -3.9; 5267 -1.0; 5793 -3.7; 6373 -3.8; 7010 -3.7; 7711 -5.9; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Hesh 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Hesh 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 2.81 | 3.0 dB  |
| Peaking | 124 Hz  | 1.18 | -6.2 dB |
| Peaking | 979 Hz  | 1.92 | -5.5 dB |
| Peaking | 3594 Hz | 3.06 | 5.5 dB  |
| Peaking | 5488 Hz | 3.69 | 3.9 dB  |
| Peaking | 18 Hz   | 0.3  | -0.6 dB |
| Peaking | 198 Hz  | 2.92 | -2.4 dB |
| Peaking | 404 Hz  | 1.3  | 3.8 dB  |
| Peaking | 707 Hz  | 3.91 | -3.2 dB |
| Peaking | 2582 Hz | 8.85 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -6.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -6.5 dB |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Hesh%202/Skullcandy%20Hesh%202.png)