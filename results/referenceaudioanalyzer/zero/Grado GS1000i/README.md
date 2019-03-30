# Grado GS1000i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -1.4; 49 -3.0; 54 -4.9; 60 -6.7; 66 -8.1; 72 -9.0; 79 -9.6; 87 -10.0; 96 -10.1; 106 -9.7; 116 -9.0; 128 -8.3; 141 -7.4; 155 -6.7; 170 -6.1; 187 -5.4; 206 -4.9; 227 -4.3; 249 -3.9; 274 -3.5; 302 -3.1; 332 -2.7; 365 -2.2; 402 -2.1; 442 -2.2; 486 -2.3; 535 -2.1; 588 -2.1; 647 -2.0; 712 -1.8; 783 -1.8; 861 -1.8; 947 -1.8; 1042 -1.9; 1146 -2.1; 1261 -2.3; 1387 -2.6; 1526 -3.3; 1678 -4.6; 1846 -5.6; 2031 -5.5; 2234 -5.3; 2457 -5.3; 2703 -5.4; 2973 -6.1; 3270 -7.8; 3597 -9.6; 3957 -10.0; 4353 -9.5; 4788 -10.4; 5267 -12.6; 5793 -13.9; 6373 -14.7; 7010 -17.9; 7711 -20.0; 8482 -19.2; 9330 -16.6; 10263 -14.6; 11289 -13.4; 12418 -12.9; 13660 -11.8; 15026 -8.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado GS1000i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GS1000i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.56 | 9.6 dB   |
| Peaking | 82 Hz    | 0.73 | -9.6 dB  |
| Peaking | 525 Hz   | 0.28 | 4.8 dB   |
| Peaking | 1118 Hz  | 2.05 | 1.0 dB   |
| Peaking | 8094 Hz  | 0.97 | -13.1 dB |
| Peaking | 1880 Hz  | 4.8  | -1.7 dB  |
| Peaking | 3139 Hz  | 1.39 | 1.7 dB   |
| Peaking | 3614 Hz  | 4.36 | -2.8 dB  |
| Peaking | 13565 Hz | 2.22 | -4.2 dB  |
| Peaking | 15066 Hz | 0.9  | 2.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 8.8 dB   |
| Peaking | 62 Hz    | 1.41 | -2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB  |
| Peaking | 250 Hz   | 1.41 | 3.0 dB   |
| Peaking | 500 Hz   | 1.41 | 3.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -14.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20GS1000i/Grado%20GS1000i.png)