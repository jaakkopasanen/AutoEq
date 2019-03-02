# JBL Endurance Peak
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -4.8; 25 -4.8; 28 -4.8; 31 -4.8; 34 -4.8; 37 -4.7; 41 -4.6; 45 -4.6; 49 -4.4; 54 -4.4; 60 -4.5; 66 -4.5; 72 -4.4; 79 -4.3; 87 -4.2; 96 -4.2; 106 -4.1; 116 -4.3; 128 -4.4; 141 -4.3; 155 -3.8; 170 -3.1; 187 -2.5; 206 -1.9; 227 -1.6; 249 -1.4; 274 -1.5; 302 -1.7; 332 -1.8; 365 -1.9; 402 -1.9; 442 -1.8; 486 -1.7; 535 -1.4; 588 -1.2; 647 -1.0; 712 -0.7; 783 -0.5; 861 -0.7; 947 -1.4; 1042 -2.3; 1146 -2.9; 1261 -3.2; 1387 -3.3; 1526 -3.3; 1678 -3.1; 1846 -3.0; 2031 -2.9; 2234 -2.8; 2457 -3.5; 2703 -4.0; 2973 -4.5; 3270 -5.0; 3597 -5.4; 3957 -5.7; 4353 -6.0; 4788 -5.8; 5267 -5.9; 5793 -6.7; 6373 -6.2; 7010 -6.3; 7711 -5.8; 8482 -3.2; 9330 -3.1; 10263 -3.1; 11289 -3.1; 12418 -3.1; 13660 -3.5; 15026 -9.9; 16529 -12.3; 18182 -8.9; 20000 -3.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Endurance Peak GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Endurance Peak ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.1  | -1.6 dB  |
| Peaking | 257 Hz   | 1.31 | 2.6 dB   |
| Peaking | 717 Hz   | 1.52 | 2.7 dB   |
| Peaking | 5108 Hz  | 1.21 | -3.4 dB  |
| Peaking | 16725 Hz | 1.76 | -10.2 dB |
| Peaking | 4994 Hz  | 4.49 | 2.4 dB   |
| Peaking | 5223 Hz  | 1.74 | -1.6 dB  |
| Peaking | 7332 Hz  | 8.52 | -2.0 dB  |
| Peaking | 12495 Hz | 0.91 | 2.1 dB   |
| Peaking | 15241 Hz | 4.39 | -3.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | 1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.1 dB |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -8.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20Endurance%20Peak/JBL%20Endurance%20Peak.png)