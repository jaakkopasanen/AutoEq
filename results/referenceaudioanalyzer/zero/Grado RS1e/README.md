# Grado RS1e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -1.1; 87 -2.8; 96 -4.6; 106 -6.2; 116 -7.6; 128 -8.7; 141 -9.3; 155 -9.5; 170 -9.2; 187 -8.6; 206 -7.8; 227 -6.8; 249 -6.0; 274 -5.6; 302 -5.2; 332 -4.8; 365 -4.3; 402 -4.0; 442 -3.7; 486 -3.5; 535 -3.3; 588 -3.1; 647 -3.1; 712 -2.9; 783 -2.8; 861 -2.8; 947 -2.9; 1042 -3.1; 1146 -3.3; 1261 -3.5; 1387 -3.9; 1526 -4.9; 1678 -8.3; 1846 -11.8; 2031 -13.4; 2234 -13.8; 2457 -13.7; 2703 -13.0; 2973 -11.4; 3270 -9.6; 3597 -7.5; 3957 -5.4; 4353 -6.4; 4788 -9.1; 5267 -9.8; 5793 -8.0; 6373 -6.1; 7010 -6.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS1e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 78 Hz    | 0.25 | 9.2 dB   |
| Peaking | 145 Hz   | 0.9  | -11.6 dB |
| Peaking | 1371 Hz  | 0.61 | 6.9 dB   |
| Peaking | 2200 Hz  | 1.37 | -13.3 dB |
| Peaking | 22050 Hz | 2.24 | -1.2 dB  |
| Peaking | 19 Hz    | 2.58 | 1.1 dB   |
| Peaking | 75 Hz    | 7.14 | 1.2 dB   |
| Peaking | 3155 Hz  | 2.1  | -3.3 dB  |
| Peaking | 4174 Hz  | 1.48 | 5.9 dB   |
| Peaking | 5007 Hz  | 3.37 | -6.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 6.9 dB  |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.4 dB |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20RS1e/Grado%20RS1e.png)