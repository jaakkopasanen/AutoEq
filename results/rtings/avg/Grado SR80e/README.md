# Grado SR80e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.9; 49 -1.6; 54 -2.2; 60 -2.9; 66 -3.5; 72 -3.9; 79 -4.3; 87 -4.7; 96 -4.9; 106 -5.2; 116 -5.3; 128 -5.4; 141 -5.4; 155 -5.4; 170 -5.3; 187 -5.3; 206 -5.1; 227 -4.9; 249 -4.7; 274 -4.7; 302 -4.8; 332 -4.9; 365 -4.8; 402 -4.9; 442 -4.9; 486 -5.0; 535 -4.9; 588 -4.7; 647 -4.5; 712 -4.2; 783 -4.0; 861 -3.8; 947 -3.8; 1042 -3.8; 1146 -3.9; 1261 -4.2; 1387 -4.7; 1526 -5.4; 1678 -6.7; 1846 -10.6; 2031 -13.1; 2234 -11.9; 2457 -10.1; 2703 -8.6; 2973 -7.4; 3270 -6.8; 3597 -7.6; 3957 -9.4; 4353 -7.2; 4788 -4.6; 5267 -6.0; 5793 -6.8; 6373 -9.0; 7010 -11.2; 7711 -10.7; 8482 -12.1; 9330 -12.5; 10263 -8.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR80e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR80e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.57 | 6.4 dB  |
| Peaking | 1050 Hz  | 0.48 | 3.2 dB  |
| Peaking | 2102 Hz  | 2.59 | -8.8 dB |
| Peaking | 7046 Hz  | 4.98 | -4.1 dB |
| Peaking | 8961 Hz  | 4    | -6.6 dB |
| Peaking | 252 Hz   | 2.98 | 0.9 dB  |
| Peaking | 3472 Hz  | 4.67 | 1.0 dB  |
| Peaking | 4026 Hz  | 4.24 | -3.9 dB |
| Peaking | 4799 Hz  | 5.1  | 3.2 dB  |
| Peaking | 11054 Hz | 6.54 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | 1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Grado%20SR80e/Grado%20SR80e.png)