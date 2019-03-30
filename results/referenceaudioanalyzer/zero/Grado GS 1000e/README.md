# Grado GS 1000e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.7; 87 -2.4; 96 -4.4; 106 -6.4; 116 -8.3; 128 -9.8; 141 -10.6; 155 -10.5; 170 -9.7; 187 -8.6; 206 -7.3; 227 -6.1; 249 -5.1; 274 -4.2; 302 -3.8; 332 -3.6; 365 -3.3; 402 -2.7; 442 -2.3; 486 -2.0; 535 -1.9; 588 -1.9; 647 -1.7; 712 -1.5; 783 -1.5; 861 -1.3; 947 -1.2; 1042 -1.5; 1146 -1.7; 1261 -1.9; 1387 -2.2; 1526 -4.4; 1678 -6.8; 1846 -7.6; 2031 -7.0; 2234 -6.7; 2457 -7.1; 2703 -8.0; 2973 -8.9; 3270 -9.6; 3597 -9.6; 3957 -8.3; 4353 -8.2; 4788 -11.0; 5267 -14.0; 5793 -17.2; 6373 -18.7; 7010 -16.4; 7711 -10.2; 8482 -6.5; 9330 -6.5; 10263 -7.5; 11289 -8.4; 12418 -6.6; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado GS 1000e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GS 1000e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 90 Hz   | 0.24 | 10.1 dB  |
| Peaking | 145 Hz  | 0.99 | -14.2 dB |
| Peaking | 1186 Hz | 0.68 | 8.6 dB   |
| Peaking | 1843 Hz | 0.68 | -6.3 dB  |
| Peaking | 6206 Hz | 3    | -13.0 dB |
| Peaking | 19 Hz   | 2.39 | 1.3 dB   |
| Peaking | 1764 Hz | 7.94 | -1.6 dB  |
| Peaking | 2286 Hz | 6.15 | 1.4 dB   |
| Peaking | 7159 Hz | 7.42 | -3.1 dB  |
| Peaking | 8435 Hz | 4.33 | 3.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.5 dB  |
| Peaking | 62 Hz    | 1.41 | 7.5 dB  |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 4.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | -4.1 dB |
| Peaking | 8000 Hz  | 1.41 | -5.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20GS%201000e/Grado%20GS%201000e.png)