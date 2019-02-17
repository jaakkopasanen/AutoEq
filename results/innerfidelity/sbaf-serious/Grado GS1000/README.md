# Grado GS1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.8; 34 -1.5; 37 -2.3; 41 -3.4; 45 -4.7; 49 -6.0; 54 -7.3; 60 -8.8; 66 -10.1; 72 -11.1; 79 -12.2; 87 -13.1; 96 -13.8; 106 -13.9; 116 -13.7; 128 -13.3; 141 -12.8; 155 -12.2; 170 -11.5; 187 -10.9; 206 -10.3; 227 -9.6; 249 -9.1; 274 -8.5; 302 -8.4; 332 -8.5; 365 -8.1; 402 -7.8; 442 -7.3; 486 -7.2; 535 -7.2; 588 -6.8; 647 -6.7; 712 -6.8; 783 -6.4; 861 -6.6; 947 -6.5; 1042 -6.5; 1146 -6.9; 1261 -7.2; 1387 -7.8; 1526 -8.2; 1678 -7.2; 1846 -8.4; 2031 -8.1; 2234 -7.8; 2457 -7.7; 2703 -7.9; 2973 -7.7; 3270 -7.3; 3597 -9.4; 3957 -11.8; 4353 -16.4; 4788 -13.2; 5267 -14.9; 5793 -17.0; 6373 -17.8; 7010 -15.5; 7711 -12.4; 8482 -13.2; 9330 -16.9; 10263 -16.2; 11289 -11.3; 12418 -8.7; 13660 -8.2; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado GS1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 28 Hz   | 0.64 | 7.9 dB   |
| Peaking | 98 Hz   | 0.66 | -9.0 dB  |
| Peaking | 262 Hz  | 2.43 | 0.2 dB   |
| Peaking | 5839 Hz | 1.34 | -10.4 dB |
| Peaking | 9885 Hz | 3.5  | -8.8 dB  |
| Peaking | 997 Hz  | 1.19 | 1.5 dB   |
| Peaking | 1446 Hz | 0.91 | -1.6 dB  |
| Peaking | 3471 Hz | 2.23 | 2.6 dB   |
| Peaking | 4306 Hz | 5.73 | -5.9 dB  |
| Peaking | 4924 Hz | 7.29 | 3.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 8.1 dB   |
| Peaking | 62 Hz    | 1.41 | -3.9 dB  |
| Peaking | 125 Hz   | 1.41 | -7.3 dB  |
| Peaking | 250 Hz   | 1.41 | -1.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 4000 Hz  | 1.41 | -4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -10.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20GS1000/Grado%20GS1000.png)