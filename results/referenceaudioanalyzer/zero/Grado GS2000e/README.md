# Grado GS2000e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.2; 72 -2.3; 79 -3.5; 87 -4.5; 96 -5.3; 106 -5.8; 116 -6.2; 128 -6.4; 141 -6.4; 155 -6.2; 170 -5.9; 187 -5.5; 206 -5.1; 227 -4.7; 249 -4.2; 274 -3.4; 302 -3.2; 332 -3.5; 365 -3.3; 402 -2.8; 442 -2.5; 486 -2.5; 535 -2.4; 588 -2.2; 647 -2.2; 712 -2.2; 783 -2.2; 861 -2.2; 947 -2.4; 1042 -2.9; 1146 -3.4; 1261 -3.6; 1387 -4.0; 1526 -4.5; 1678 -5.0; 1846 -5.1; 2031 -4.9; 2234 -5.1; 2457 -5.3; 2703 -5.9; 2973 -6.7; 3270 -7.3; 3597 -7.5; 3957 -11.2; 4353 -15.6; 4788 -18.1; 5267 -20.5; 5793 -21.0; 6373 -18.1; 7010 -13.6; 7711 -12.3; 8482 -10.9; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado GS2000e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GS2000e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 35 Hz   | 0.74 | 7.0 dB   |
| Peaking | 339 Hz  | 1.68 | 1.8 dB   |
| Peaking | 768 Hz  | 0.74 | 4.4 dB   |
| Peaking | 2912 Hz | 1.43 | 2.6 dB   |
| Peaking | 5456 Hz | 1.87 | -16.3 dB |
| Peaking | 37 Hz   | 3.09 | -1.1 dB  |
| Peaking | 61 Hz   | 2.79 | 2.1 dB   |
| Peaking | 120 Hz  | 1.93 | -1.5 dB  |
| Peaking | 8462 Hz | 1.97 | -3.5 dB  |
| Peaking | 9550 Hz | 1.92 | 4.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | 1.8 dB  |
| Peaking | 500 Hz   | 1.41 | 3.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -7.8 dB |
| Peaking | 8000 Hz  | 1.41 | -6.2 dB |
| Peaking | 16000 Hz | 1.41 | 1.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20GS2000e/Grado%20GS2000e.png)