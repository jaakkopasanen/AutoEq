# Skullcandy Hesh 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -4.5; 25 -5.1; 28 -5.9; 31 -6.4; 34 -6.7; 37 -6.9; 41 -7.1; 45 -7.3; 49 -7.5; 54 -7.9; 60 -8.3; 66 -8.8; 72 -9.3; 79 -9.8; 87 -10.4; 96 -11.0; 106 -11.6; 116 -11.9; 128 -12.0; 141 -11.9; 155 -11.7; 170 -11.5; 187 -11.2; 206 -10.1; 227 -8.8; 249 -7.7; 274 -6.5; 302 -5.4; 332 -4.4; 365 -3.7; 402 -3.7; 442 -4.2; 486 -4.4; 535 -5.0; 588 -6.6; 647 -8.9; 712 -10.3; 783 -10.7; 861 -10.7; 947 -10.7; 1042 -10.9; 1146 -10.3; 1261 -9.1; 1387 -8.3; 1526 -7.6; 1678 -7.1; 1846 -7.1; 2031 -6.4; 2234 -5.0; 2457 -3.5; 2703 -3.1; 2973 -4.1; 3270 -2.8; 3597 -1.0; 3957 -0.6; 4353 -5.7; 4788 -3.7; 5267 -0.5; 5793 -3.7; 6373 -4.8; 7010 -3.7; 7711 -5.9; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Hesh 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Hesh 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 123 Hz  | 1.16 | -6.4 dB |
| Peaking | 967 Hz  | 6.41 | 3.7 dB  |
| Peaking | 969 Hz  | 2.47 | -8.1 dB |
| Peaking | 3515 Hz | 1.94 | 4.7 dB  |
| Peaking | 5314 Hz | 7.46 | 4.8 dB  |
| Peaking | 20 Hz   | 3.06 | 2.6 dB  |
| Peaking | 202 Hz  | 2.23 | -2.9 dB |
| Peaking | 413 Hz  | 0.9  | 3.8 dB  |
| Peaking | 689 Hz  | 3.37 | -3.7 dB |
| Peaking | 1459 Hz | 2.47 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -6.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -6.5 dB |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Hesh%202/Skullcandy%20Hesh%202.png)