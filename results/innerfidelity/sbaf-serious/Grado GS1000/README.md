# Grado GS1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -1.2; 49 -2.5; 54 -3.8; 60 -5.3; 66 -6.6; 72 -7.6; 79 -8.7; 87 -9.6; 96 -10.3; 106 -10.4; 116 -10.2; 128 -9.8; 141 -9.3; 155 -8.7; 170 -8.0; 187 -7.4; 206 -6.8; 227 -6.1; 249 -5.6; 274 -5.0; 302 -4.9; 332 -5.0; 365 -4.6; 402 -4.3; 442 -3.8; 486 -3.7; 535 -3.7; 588 -3.3; 647 -3.2; 712 -3.3; 783 -2.9; 861 -3.1; 947 -3.0; 1042 -3.0; 1146 -3.4; 1261 -3.7; 1387 -4.3; 1526 -4.7; 1678 -3.7; 1846 -4.9; 2031 -4.6; 2234 -4.3; 2457 -4.2; 2703 -4.4; 2973 -4.2; 3270 -3.8; 3597 -5.9; 3957 -8.3; 4353 -12.8; 4788 -9.7; 5267 -11.3; 5793 -13.5; 6373 -14.3; 7010 -12.0; 7711 -8.9; 8482 -9.7; 9330 -13.4; 10263 -12.7; 11289 -7.8; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado GS1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 36 Hz   | 0.51 | 8.3 dB   |
| Peaking | 98 Hz   | 0.71 | -8.5 dB  |
| Peaking | 1424 Hz | 0.1  | 3.5 dB   |
| Peaking | 5812 Hz | 1.36 | -10.0 dB |
| Peaking | 9846 Hz | 4.23 | -7.7 dB  |
| Peaking | 1037 Hz | 1.1  | 1.3 dB   |
| Peaking | 1477 Hz | 1.04 | -1.7 dB  |
| Peaking | 3482 Hz | 2.31 | 2.6 dB   |
| Peaking | 4315 Hz | 5.71 | -5.8 dB  |
| Peaking | 4930 Hz | 7.37 | 3.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.9 dB |
| Peaking | 8000 Hz  | 1.41 | -6.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20GS1000/Grado%20GS1000.png)