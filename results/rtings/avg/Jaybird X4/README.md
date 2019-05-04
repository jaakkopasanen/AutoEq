# Jaybird X4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.3; 23 -8.3; 25 -8.2; 28 -8.1; 31 -8.1; 34 -8.0; 37 -8.0; 41 -8.0; 45 -8.0; 49 -7.9; 54 -7.8; 60 -7.7; 66 -7.6; 72 -7.6; 79 -7.4; 87 -7.4; 96 -7.2; 106 -7.0; 116 -7.3; 128 -8.0; 141 -8.4; 155 -8.4; 170 -7.9; 187 -7.4; 206 -6.9; 227 -6.4; 249 -6.0; 274 -5.5; 302 -5.0; 332 -4.5; 365 -4.0; 402 -3.5; 442 -3.0; 486 -2.6; 535 -2.0; 588 -1.5; 647 -1.1; 712 -0.8; 783 -0.5; 861 -0.7; 947 -1.6; 1042 -2.8; 1146 -4.0; 1261 -4.5; 1387 -4.8; 1526 -5.2; 1678 -5.5; 1846 -6.0; 2031 -6.8; 2234 -7.6; 2457 -8.1; 2703 -7.7; 2973 -5.9; 3270 -4.0; 3597 -2.7; 3957 -2.0; 4353 -1.9; 4788 -2.5; 5267 -3.2; 5793 -5.3; 6373 -10.7; 7010 -10.7; 7711 -5.1; 8482 -4.6; 9330 -4.6; 10263 -4.8; 11289 -10.3; 12418 -10.5; 13660 -8.6; 15026 -9.5; 16529 -7.3; 18182 -4.6; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird X4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird X4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.29 | -3.6 dB  |
| Peaking | 159 Hz   | 1.59 | -2.9 dB  |
| Peaking | 697 Hz   | 1.66 | 4.5 dB   |
| Peaking | 11958 Hz | 3.54 | -5.9 dB  |
| Peaking | 15092 Hz | 1.93 | -4.6 dB  |
| Peaking | 907 Hz   | 5.86 | 1.4 dB   |
| Peaking | 2559 Hz  | 1.46 | -6.1 dB  |
| Peaking | 3912 Hz  | 1.03 | 5.2 dB   |
| Peaking | 6694 Hz  | 4.4  | -10.0 dB |
| Peaking | 8170 Hz  | 2.12 | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | -5.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20X4/Jaybird%20X4.png)