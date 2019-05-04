# Plantronics Backbeat Go 810
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -1.0; 25 -0.7; 28 -0.5; 31 -0.6; 34 -0.9; 37 -1.5; 41 -2.3; 45 -3.2; 49 -4.0; 54 -4.7; 60 -5.1; 66 -5.4; 72 -5.4; 79 -5.5; 87 -5.5; 96 -5.5; 106 -5.5; 116 -5.5; 128 -5.5; 141 -5.4; 155 -5.2; 170 -4.6; 187 -3.9; 206 -3.8; 227 -3.8; 249 -3.7; 274 -3.5; 302 -3.1; 332 -2.8; 365 -3.2; 402 -3.3; 442 -3.4; 486 -3.5; 535 -3.6; 588 -3.6; 647 -3.8; 712 -4.0; 783 -3.6; 861 -2.9; 947 -3.3; 1042 -3.9; 1146 -3.8; 1261 -3.5; 1387 -3.5; 1526 -3.5; 1678 -3.5; 1846 -4.8; 2031 -5.6; 2234 -5.5; 2457 -4.7; 2703 -4.1; 2973 -4.0; 3270 -4.3; 3597 -4.6; 3957 -4.5; 4353 -2.9; 4788 -2.4; 5267 -2.1; 5793 -2.0; 6373 -2.9; 7010 -4.5; 7711 -6.9; 8482 -6.8; 9330 -4.4; 10263 -4.0; 11289 -4.0; 12418 -4.8; 13660 -6.2; 15026 -7.4; 16529 -4.9; 18182 -4.0; 20000 -4.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics Backbeat Go 810 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics Backbeat Go 810 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 2.44 | 4.2 dB  |
| Peaking | 2134 Hz  | 5.45 | -1.9 dB |
| Peaking | 5616 Hz  | 2.59 | 2.5 dB  |
| Peaking | 7979 Hz  | 4.5  | -3.8 dB |
| Peaking | 14913 Hz | 2.65 | -3.7 dB |
| Peaking | 17 Hz    | 0.25 | 1.4 dB  |
| Peaking | 87 Hz    | 0.61 | -2.4 dB |
| Peaking | 303 Hz   | 1.09 | 1.3 dB  |
| Peaking | 1079 Hz  | 1.14 | 0.5 dB  |
| Peaking | 3719 Hz  | 7.72 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Plantronics%20Backbeat%20Go%20810/Plantronics%20Backbeat%20Go%20810.png)