# Grado SR60e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.8; 41 -1.7; 45 -2.7; 49 -3.6; 54 -4.4; 60 -5.1; 66 -5.5; 72 -5.8; 79 -5.9; 87 -6.1; 96 -5.9; 106 -5.9; 116 -5.7; 128 -5.5; 141 -5.3; 155 -5.1; 170 -4.9; 187 -4.6; 206 -4.5; 227 -4.2; 249 -4.0; 274 -3.9; 302 -3.7; 332 -3.6; 365 -3.6; 402 -3.7; 442 -4.1; 486 -4.2; 535 -3.9; 588 -3.9; 647 -3.7; 712 -3.6; 783 -3.6; 861 -3.6; 947 -3.9; 1042 -3.9; 1146 -4.1; 1261 -4.4; 1387 -4.9; 1526 -5.5; 1678 -7.1; 1846 -10.3; 2031 -12.4; 2234 -12.6; 2457 -11.9; 2703 -11.0; 2973 -9.6; 3270 -9.2; 3597 -10.3; 3957 -10.2; 4353 -8.3; 4788 -8.5; 5267 -11.2; 5793 -12.5; 6373 -12.8; 7010 -11.7; 7711 -8.0; 8482 -6.5; 9330 -6.5; 10263 -7.0; 11289 -7.4; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR60e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR60e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 1.08 | 6.8 dB  |
| Peaking | 801 Hz   | 0.3  | 3.6 dB  |
| Peaking | 2295 Hz  | 1.57 | -8.4 dB |
| Peaking | 6085 Hz  | 2.48 | -6.7 dB |
| Peaking | 22050 Hz | 2.38 | -4.4 dB |
| Peaking | 542 Hz   | 2.65 | -0.8 dB |
| Peaking | 1882 Hz  | 1.55 | 2.4 dB  |
| Peaking | 1949 Hz  | 4.1  | -3.7 dB |
| Peaking | 3741 Hz  | 7.04 | -2.6 dB |
| Peaking | 8428 Hz  | 6.88 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | 2.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | -3.1 dB |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20SR60e/Grado%20SR60e.png)