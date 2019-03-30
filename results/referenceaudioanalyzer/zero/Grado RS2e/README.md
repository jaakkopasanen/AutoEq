# Grado RS2e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.3; 49 -2.2; 54 -3.1; 60 -3.9; 66 -4.5; 72 -4.9; 79 -5.4; 87 -5.5; 96 -5.5; 106 -5.5; 116 -5.5; 128 -5.3; 141 -5.2; 155 -4.9; 170 -4.6; 187 -4.2; 206 -3.9; 227 -3.9; 249 -3.9; 274 -3.9; 302 -3.8; 332 -3.6; 365 -3.5; 402 -3.3; 442 -3.3; 486 -3.5; 535 -3.6; 588 -3.6; 647 -3.6; 712 -3.6; 783 -3.6; 861 -3.6; 947 -3.6; 1042 -3.8; 1146 -4.1; 1261 -4.4; 1387 -4.9; 1526 -5.4; 1678 -5.9; 1846 -7.8; 2031 -10.3; 2234 -11.8; 2457 -12.0; 2703 -11.4; 2973 -10.1; 3270 -9.5; 3597 -9.2; 3957 -9.3; 4353 -10.5; 4788 -12.0; 5267 -13.8; 5793 -14.8; 6373 -14.8; 7010 -12.7; 7711 -8.3; 8482 -6.5; 9330 -6.5; 10263 -6.9; 11289 -8.8; 12418 -9.6; 13660 -8.3; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS2e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS2e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.9  | 6.7 dB  |
| Peaking | 741 Hz   | 0.28 | 3.4 dB  |
| Peaking | 2387 Hz  | 1.9  | -7.5 dB |
| Peaking | 4689 Hz  | 2.16 | -3.1 dB |
| Peaking | 6144 Hz  | 2.68 | -7.7 dB |
| Peaking | 45 Hz    | 3.52 | 1.2 dB  |
| Peaking | 86 Hz    | 2.24 | -0.7 dB |
| Peaking | 7143 Hz  | 4.08 | -2.8 dB |
| Peaking | 8054 Hz  | 2.47 | 3.1 dB  |
| Peaking | 12259 Hz | 2.94 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | 2.4 dB  |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | -4.7 dB |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20RS2e/Grado%20RS2e.png)