# Grado SR225e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.9; 41 -1.8; 45 -2.7; 49 -3.3; 54 -4.0; 60 -4.5; 66 -4.9; 72 -5.2; 79 -5.5; 87 -5.4; 96 -5.2; 106 -5.0; 116 -4.8; 128 -4.6; 141 -4.3; 155 -4.1; 170 -3.9; 187 -3.5; 206 -3.3; 227 -3.2; 249 -3.3; 274 -3.8; 302 -4.0; 332 -3.9; 365 -3.7; 402 -3.5; 442 -3.3; 486 -3.3; 535 -3.3; 588 -3.6; 647 -3.6; 712 -3.6; 783 -3.6; 861 -3.7; 947 -3.9; 1042 -4.2; 1146 -4.5; 1261 -4.8; 1387 -5.4; 1526 -6.0; 1678 -6.9; 1846 -9.6; 2031 -11.7; 2234 -12.1; 2457 -11.4; 2703 -10.7; 2973 -9.4; 3270 -7.8; 3597 -9.0; 3957 -11.7; 4353 -12.3; 4788 -11.8; 5267 -12.9; 5793 -13.9; 6373 -13.5; 7010 -11.5; 7711 -8.1; 8482 -6.5; 9330 -6.5; 10263 -8.1; 11289 -9.5; 12418 -9.1; 13660 -6.8; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.91 | 6.5 dB  |
| Peaking | 197 Hz   | 1.39 | 1.9 dB  |
| Peaking | 791 Hz   | 0.35 | 3.2 dB  |
| Peaking | 2195 Hz  | 2.15 | -7.1 dB |
| Peaking | 5477 Hz  | 1.48 | -7.5 dB |
| Peaking | 3405 Hz  | 9.57 | 1.6 dB  |
| Peaking | 4047 Hz  | 5.5  | -2.6 dB |
| Peaking | 6667 Hz  | 3.3  | -4.2 dB |
| Peaking | 8371 Hz  | 0.94 | 4.1 dB  |
| Peaking | 11342 Hz | 2.15 | -4.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | 1.2 dB  |
| Peaking | 250 Hz   | 1.41 | 2.6 dB  |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | -4.8 dB |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20SR225e/Grado%20SR225e.png)