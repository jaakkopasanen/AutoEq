# JBL Free
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -3.9; 25 -3.9; 28 -3.9; 31 -3.8; 34 -3.9; 37 -3.9; 41 -3.9; 45 -3.8; 49 -3.8; 54 -3.9; 60 -4.2; 66 -4.3; 72 -4.5; 79 -4.6; 87 -4.8; 96 -5.0; 106 -5.2; 116 -5.4; 128 -5.6; 141 -5.5; 155 -5.3; 170 -5.2; 187 -5.0; 206 -4.9; 227 -4.8; 249 -4.6; 274 -4.5; 302 -4.3; 332 -4.2; 365 -4.0; 402 -3.8; 442 -3.4; 486 -3.0; 535 -2.6; 588 -2.0; 647 -1.4; 712 -0.8; 783 -0.5; 861 -0.6; 947 -1.2; 1042 -1.9; 1146 -2.6; 1261 -3.2; 1387 -3.5; 1526 -3.6; 1678 -3.5; 1846 -3.4; 2031 -3.5; 2234 -3.1; 2457 -2.8; 2703 -3.3; 2973 -3.9; 3270 -3.8; 3597 -3.1; 3957 -2.4; 4353 -2.0; 4788 -1.0; 5267 -0.7; 5793 -1.0; 6373 -3.6; 7010 -6.2; 7711 -4.2; 8482 -3.3; 9330 -3.3; 10263 -3.3; 11289 -5.5; 12418 -7.8; 13660 -6.4; 15026 -6.0; 16529 -9.9; 18182 -10.7; 20000 -3.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Free GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Free ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 141 Hz   | 0.57 | -2.1 dB |
| Peaking | 774 Hz   | 2.08 | 3.2 dB  |
| Peaking | 5139 Hz  | 4.2  | 3.3 dB  |
| Peaking | 17541 Hz | 0.79 | -7.4 dB |
| Peaking | 22050 Hz | 1.35 | -6.1 dB |
| Peaking | 1517 Hz  | 3.18 | -0.7 dB |
| Peaking | 7105 Hz  | 6.22 | -3.9 dB |
| Peaking | 9879 Hz  | 1    | 1.7 dB  |
| Peaking | 12277 Hz | 3.15 | -3.9 dB |
| Peaking | 14728 Hz | 4    | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -7.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20Free/JBL%20Free.png)