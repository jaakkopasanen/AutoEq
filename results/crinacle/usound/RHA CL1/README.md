# RHA CL1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -1.7; 25 -1.8; 28 -2.0; 31 -2.1; 34 -2.2; 37 -2.3; 41 -2.4; 45 -2.5; 49 -2.6; 54 -2.7; 60 -2.8; 66 -3.0; 72 -3.2; 79 -3.5; 87 -3.8; 96 -4.2; 106 -4.5; 116 -4.8; 128 -5.0; 141 -5.3; 155 -5.5; 170 -5.6; 187 -5.6; 206 -5.7; 227 -5.6; 249 -5.6; 274 -5.4; 302 -5.3; 332 -5.2; 365 -4.9; 402 -4.7; 442 -4.4; 486 -4.1; 535 -3.7; 588 -3.2; 647 -2.7; 712 -2.2; 783 -1.5; 861 -1.0; 947 -0.7; 1042 -0.6; 1146 -0.9; 1261 -1.2; 1387 -1.4; 1526 -1.2; 1678 -0.8; 1846 -0.5; 2031 -0.7; 2234 -1.3; 2457 -2.6; 2703 -4.1; 2973 -4.7; 3270 -4.0; 3597 -3.2; 3957 -3.1; 4353 -4.1; 4788 -7.9; 5267 -12.5; 5793 -9.6; 6373 -6.9; 7010 -8.0; 7711 -13.7; 8482 -14.5; 9330 -10.4; 10263 -9.7; 11289 -11.7; 12418 -13.2; 13660 -17.0; 15026 -19.9; 16529 -18.3; 18182 -16.9; 20000 -18.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA CL1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA CL1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 946 Hz   | 1.7  | 3.6 dB   |
| Peaking | 1893 Hz  | 1.54 | 4.0 dB   |
| Peaking | 8103 Hz  | 5.7  | -6.7 dB  |
| Peaking | 15003 Hz | 2.34 | -6.1 dB  |
| Peaking | 20077 Hz | 0.14 | -12.7 dB |
| Peaking | 24 Hz    | 1.14 | 3.1 dB   |
| Peaking | 54 Hz    | 2.15 | 1.6 dB   |
| Peaking | 4128 Hz  | 3.57 | 3.4 dB   |
| Peaking | 5258 Hz  | 4.85 | -7.0 dB  |
| Peaking | 6513 Hz  | 5.34 | 2.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB   |
| Peaking | 62 Hz    | 1.41 | 1.5 dB   |
| Peaking | 125 Hz   | 1.41 | -0.6 dB  |
| Peaking | 250 Hz   | 1.41 | -1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 8000 Hz  | 1.41 | -6.2 dB  |
| Peaking | 16000 Hz | 1.41 | -20.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/RHA%20CL1/RHA%20CL1.png)