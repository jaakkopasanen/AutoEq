# Panasonic RP-HC200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.8; 116 -1.4; 128 -1.9; 141 -2.0; 155 -2.1; 170 -2.1; 187 -2.2; 206 -1.9; 227 -1.9; 249 -1.8; 274 -1.8; 302 -1.3; 332 -0.9; 365 -0.9; 402 -0.9; 442 -1.1; 486 -1.6; 535 -2.4; 588 -3.5; 647 -4.8; 712 -5.9; 783 -6.7; 861 -7.1; 947 -6.5; 1042 -6.4; 1146 -6.0; 1261 -4.8; 1387 -4.8; 1526 -4.2; 1678 -2.9; 1846 -1.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.6; 6373 -1.8; 7010 -4.0; 7711 -6.2; 8482 -9.4; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.1; 15026 -11.4; 16529 -8.7; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 43 Hz    | 0.2  | 6.2 dB  |
| Peaking | 381 Hz   | 1.7  | 4.5 dB  |
| Peaking | 3864 Hz  | 0.64 | 7.5 dB  |
| Peaking | 12603 Hz | 0.42 | -2.9 dB |
| Peaking | 22050 Hz | 1.65 | -2.1 dB |
| Peaking | 909 Hz   | 2.44 | -2.4 dB |
| Peaking | 2025 Hz  | 4.38 | 2.2 dB  |
| Peaking | 6091 Hz  | 4.43 | 1.8 dB  |
| Peaking | 8393 Hz  | 6.05 | -4.0 dB |
| Peaking | 11774 Hz | 3.26 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.9 dB  |
| Peaking | 125 Hz   | 1.41 | 3.3 dB  |
| Peaking | 250 Hz   | 1.41 | 3.7 dB  |
| Peaking | 500 Hz   | 1.41 | 4.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB |
| Peaking | 2000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -3.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Panasonic%20RP-HC200/Panasonic%20RP-HC200.png)