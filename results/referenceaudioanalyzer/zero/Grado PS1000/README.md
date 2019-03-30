# Grado PS1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.8; 49 -3.1; 54 -4.7; 60 -6.4; 66 -8.0; 72 -9.3; 79 -10.4; 87 -11.2; 96 -11.5; 106 -11.1; 116 -10.5; 128 -9.6; 141 -8.6; 155 -7.7; 170 -6.9; 187 -6.1; 206 -5.5; 227 -4.9; 249 -4.4; 274 -3.9; 302 -3.4; 332 -3.0; 365 -2.7; 402 -2.3; 442 -1.9; 486 -2.0; 535 -2.2; 588 -2.1; 647 -2.1; 712 -2.1; 783 -2.2; 861 -2.5; 947 -2.5; 1042 -2.8; 1146 -3.0; 1261 -3.5; 1387 -4.1; 1526 -4.3; 1678 -4.0; 1846 -3.8; 2031 -3.6; 2234 -3.4; 2457 -3.7; 2703 -4.2; 2973 -4.4; 3270 -4.5; 3597 -8.4; 3957 -12.4; 4353 -13.5; 4788 -14.5; 5267 -17.6; 5793 -21.3; 6373 -21.8; 7010 -17.4; 7711 -10.0; 8482 -6.4; 9330 -8.1; 10263 -10.5; 11289 -10.8; 12418 -9.6; 13660 -7.0; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado PS1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.57 | 8.3 dB   |
| Peaking | 91 Hz    | 0.82 | -10.3 dB |
| Peaking | 610 Hz   | 0.17 | 4.6 dB   |
| Peaking | 5889 Hz  | 2    | -17.3 dB |
| Peaking | 21974 Hz | 2.16 | -2.2 dB  |
| Peaking | 1446 Hz  | 3.35 | -1.6 dB  |
| Peaking | 3334 Hz  | 2.34 | 3.8 dB   |
| Peaking | 3940 Hz  | 3.84 | -5.4 dB  |
| Peaking | 8467 Hz  | 5.71 | 5.7 dB   |
| Peaking | 11197 Hz | 2.82 | -3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | 2.6 dB  |
| Peaking | 500 Hz   | 1.41 | 4.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -6.5 dB |
| Peaking | 8000 Hz  | 1.41 | -7.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20PS1000/Grado%20PS1000.png)