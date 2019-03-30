# JBL Free X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -4.5; 25 -4.5; 28 -4.5; 31 -4.5; 34 -4.4; 37 -4.3; 41 -4.2; 45 -4.1; 49 -4.0; 54 -4.0; 60 -4.2; 66 -4.3; 72 -4.4; 79 -4.4; 87 -4.5; 96 -4.6; 106 -4.7; 116 -4.8; 128 -4.8; 141 -4.7; 155 -4.5; 170 -4.3; 187 -4.1; 206 -4.0; 227 -3.9; 249 -3.7; 274 -3.5; 302 -3.3; 332 -3.2; 365 -3.0; 402 -2.8; 442 -2.5; 486 -2.1; 535 -1.6; 588 -1.1; 647 -0.7; 712 -0.5; 783 -0.5; 861 -0.6; 947 -1.1; 1042 -1.9; 1146 -2.7; 1261 -3.2; 1387 -3.5; 1526 -3.6; 1678 -3.9; 1846 -4.2; 2031 -4.6; 2234 -4.4; 2457 -4.5; 2703 -5.2; 2973 -5.8; 3270 -5.2; 3597 -4.0; 3957 -3.0; 4353 -2.3; 4788 -1.3; 5267 -0.7; 5793 -0.9; 6373 -2.9; 7010 -5.8; 7711 -5.8; 8482 -3.9; 9330 -3.4; 10263 -4.4; 11289 -7.5; 12418 -10.2; 13660 -8.3; 15026 -6.9; 16529 -10.2; 18182 -11.4; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Free X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Free X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 687 Hz   | 0.73 | 4.9 dB  |
| Peaking | 806 Hz   | 0.08 | -2.2 dB |
| Peaking | 5188 Hz  | 2.8  | 4.8 dB  |
| Peaking | 12465 Hz | 3.78 | -5.6 dB |
| Peaking | 17852 Hz | 1.1  | -8.8 dB |
| Peaking | 23 Hz    | 1.55 | -1.2 dB |
| Peaking | 3091 Hz  | 4.1  | -1.7 dB |
| Peaking | 3798 Hz  | 2.85 | 1.0 dB  |
| Peaking | 7314 Hz  | 6.86 | -2.6 dB |
| Peaking | 9250 Hz  | 4.28 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -8.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20Free%20X/JBL%20Free%20X.png)