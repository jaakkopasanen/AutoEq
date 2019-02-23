# Skullcandy Hesh 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.8; 23 -13.4; 25 -12.9; 28 -12.3; 31 -11.7; 34 -11.0; 37 -10.3; 41 -9.5; 45 -8.8; 49 -8.1; 54 -7.3; 60 -6.8; 66 -6.8; 72 -7.1; 79 -7.7; 87 -8.7; 96 -9.6; 106 -10.1; 116 -10.3; 128 -10.1; 141 -9.6; 155 -8.8; 170 -8.0; 187 -7.1; 206 -5.9; 227 -4.7; 249 -3.5; 274 -2.6; 302 -1.9; 332 -1.3; 365 -0.8; 402 -0.5; 442 -0.5; 486 -0.7; 535 -0.9; 588 -1.2; 647 -1.6; 712 -2.0; 783 -2.2; 861 -2.3; 947 -2.3; 1042 -2.3; 1146 -2.0; 1261 -1.6; 1387 -1.0; 1526 -0.7; 1678 -1.0; 1846 -1.6; 2031 -2.6; 2234 -3.3; 2457 -3.9; 2703 -4.6; 2973 -5.6; 3270 -6.2; 3597 -6.2; 3957 -5.0; 4353 -5.5; 4788 -6.4; 5267 -6.9; 5793 -10.1; 6373 -11.3; 7010 -12.0; 7711 -11.5; 8482 -11.7; 9330 -10.3; 10263 -7.0; 11289 -5.3; 12418 -5.3; 13660 -8.0; 15026 -10.9; 16529 -8.4; 18182 -5.9; 20000 -14.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Hesh 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Hesh 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.63 | -10.0 dB |
| Peaking | 128 Hz   | 0.95 | -9.6 dB  |
| Peaking | 240 Hz   | 0.14 | 5.0 dB   |
| Peaking | 7305 Hz  | 1.52 | -7.8 dB  |
| Peaking | 15407 Hz | 2.5  | -6.2 dB  |
| Peaking | 407 Hz   | 2.08 | 1.3 dB   |
| Peaking | 906 Hz   | 0.95 | -1.6 dB  |
| Peaking | 1556 Hz  | 2.23 | 2.4 dB   |
| Peaking | 3164 Hz  | 4.86 | -1.9 dB  |
| Peaking | 11660 Hz | 5.02 | 2.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.2 dB |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -6.5 dB |
| Peaking | 250 Hz   | 1.41 | 2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 4.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | -6.8 dB |
| Peaking | 16000 Hz | 1.41 | -4.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Hesh%203/Skullcandy%20Hesh%203.png)