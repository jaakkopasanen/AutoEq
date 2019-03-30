# Sony SA1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.7; 66 -1.5; 72 -2.3; 79 -3.0; 87 -3.6; 96 -4.0; 106 -4.3; 116 -4.5; 128 -4.4; 141 -4.1; 155 -3.8; 170 -3.6; 187 -3.5; 206 -3.5; 227 -3.7; 249 -3.8; 274 -4.1; 302 -4.2; 332 -4.4; 365 -4.5; 402 -4.8; 442 -4.8; 486 -5.0; 535 -5.3; 588 -6.0; 647 -6.6; 712 -7.2; 783 -7.7; 861 -8.0; 947 -8.2; 1042 -8.4; 1146 -8.1; 1261 -7.1; 1387 -5.6; 1526 -4.2; 1678 -3.2; 1846 -3.1; 2031 -3.4; 2234 -3.9; 2457 -4.7; 2703 -6.0; 2973 -7.1; 3270 -7.7; 3597 -7.3; 3957 -7.7; 4353 -9.6; 4788 -10.4; 5267 -8.0; 5793 -2.8; 6373 -6.2; 7010 -14.4; 7711 -19.2; 8482 -18.3; 9330 -14.0; 10263 -12.1; 11289 -14.3; 12418 -15.5; 13660 -12.3; 15026 -7.7; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony SA1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony SA1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 5091 Hz  | 1.33 | -15.6 dB |
| Peaking | 5886 Hz  | 1.31 | 28.0 dB  |
| Peaking | 7732 Hz  | 1.53 | -22.1 dB |
| Peaking | 12452 Hz | 2.5  | -8.4 dB  |
| Peaking | 34 Hz    | 0.53 | 6.5 dB   |
| Peaking | 276 Hz   | 0.69 | 2.4 dB   |
| Peaking | 1097 Hz  | 1.21 | -4.5 dB  |
| Peaking | 1694 Hz  | 1.36 | 4.1 dB   |
| Peaking | 3021 Hz  | 4.13 | -2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 3.9 dB   |
| Peaking | 125 Hz   | 1.41 | 0.8 dB   |
| Peaking | 250 Hz   | 1.41 | 2.6 dB   |
| Peaking | 500 Hz   | 1.41 | 1.1 dB   |
| Peaking | 1000 Hz  | 1.41 | -2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -10.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20SA1000/Sony%20SA1000.png)