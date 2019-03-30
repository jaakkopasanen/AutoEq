# Grado SR225i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.7; 60 -1.7; 66 -2.5; 72 -3.2; 79 -3.7; 87 -4.1; 96 -4.2; 106 -4.2; 116 -4.2; 128 -3.9; 141 -3.8; 155 -3.6; 170 -3.5; 187 -3.2; 206 -3.2; 227 -3.2; 249 -3.2; 274 -3.2; 302 -3.2; 332 -3.2; 365 -3.2; 402 -3.2; 442 -3.2; 486 -3.2; 535 -3.1; 588 -2.9; 647 -2.9; 712 -3.2; 783 -3.2; 861 -3.2; 947 -3.5; 1042 -3.7; 1146 -4.0; 1261 -4.4; 1387 -5.0; 1526 -5.6; 1678 -6.6; 1846 -9.5; 2031 -11.9; 2234 -12.6; 2457 -12.0; 2703 -11.2; 2973 -10.1; 3270 -8.9; 3597 -9.5; 3957 -11.3; 4353 -13.3; 4788 -14.3; 5267 -14.6; 5793 -14.9; 6373 -14.8; 7010 -12.3; 7711 -7.9; 8482 -6.5; 9330 -7.2; 10263 -10.0; 11289 -11.0; 12418 -10.2; 13660 -7.7; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.61 | 6.5 dB  |
| Peaking | 736 Hz   | 0.21 | 3.7 dB  |
| Peaking | 2215 Hz  | 2.13 | -8.1 dB |
| Peaking | 5382 Hz  | 1.36 | -9.6 dB |
| Peaking | 21164 Hz | 1.89 | -3.0 dB |
| Peaking | 53 Hz    | 4.13 | 1.1 dB  |
| Peaking | 89 Hz    | 3.13 | -0.7 dB |
| Peaking | 6708 Hz  | 4.47 | -3.3 dB |
| Peaking | 8209 Hz  | 2.15 | 4.6 dB  |
| Peaking | 11246 Hz | 2.28 | -4.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | 1.1 dB  |
| Peaking | 250 Hz   | 1.41 | 2.8 dB  |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | -5.8 dB |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20SR225i/Grado%20SR225i.png)