# Grado SR325i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.3; 54 -2.2; 60 -3.2; 66 -4.0; 72 -4.5; 79 -4.8; 87 -5.0; 96 -5.1; 106 -4.9; 116 -4.9; 128 -4.7; 141 -4.4; 155 -4.2; 170 -4.0; 187 -3.9; 206 -3.7; 227 -3.5; 249 -3.3; 274 -3.1; 302 -3.0; 332 -3.3; 365 -3.5; 402 -3.3; 442 -3.3; 486 -3.2; 535 -3.5; 588 -3.6; 647 -3.3; 712 -3.3; 783 -3.6; 861 -3.6; 947 -3.6; 1042 -3.9; 1146 -4.2; 1261 -4.6; 1387 -5.1; 1526 -5.8; 1678 -6.5; 1846 -8.6; 2031 -11.3; 2234 -12.3; 2457 -11.9; 2703 -11.0; 2973 -9.4; 3270 -7.4; 3597 -6.2; 3957 -9.8; 4353 -14.1; 4788 -15.2; 5267 -14.9; 5793 -15.3; 6373 -14.8; 7010 -11.0; 7711 -6.5; 8482 -6.5; 9330 -7.9; 10263 -10.4; 11289 -11.5; 12418 -11.0; 13660 -8.1; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR325i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR325i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.82 | 6.6 dB   |
| Peaking | 1809 Hz  | 0.09 | 3.7 dB   |
| Peaking | 2247 Hz  | 2.11 | -8.8 dB  |
| Peaking | 5386 Hz  | 1.69 | -12.8 dB |
| Peaking | 11661 Hz | 2.18 | -7.0 dB  |
| Peaking | 87 Hz    | 3.65 | -0.8 dB  |
| Peaking | 3594 Hz  | 7.73 | 3.2 dB   |
| Peaking | 4349 Hz  | 8.42 | -3.1 dB  |
| Peaking | 6606 Hz  | 8    | -3.2 dB  |
| Peaking | 7862 Hz  | 4.43 | 2.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.6 dB  |
| Peaking | 250 Hz   | 1.41 | 2.9 dB  |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | -4.9 dB |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20SR325i/Grado%20SR325i.png)