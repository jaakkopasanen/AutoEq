# Sony SA3000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -1.0; 116 -1.4; 128 -1.7; 141 -1.7; 155 -1.7; 170 -1.8; 187 -2.1; 206 -2.1; 227 -2.1; 249 -2.1; 274 -2.2; 302 -2.6; 332 -3.1; 365 -3.4; 402 -3.4; 442 -3.7; 486 -4.1; 535 -4.7; 588 -5.3; 647 -5.9; 712 -6.6; 783 -7.3; 861 -7.7; 947 -8.0; 1042 -8.5; 1146 -8.6; 1261 -8.3; 1387 -7.7; 1526 -7.0; 1678 -6.3; 1846 -6.0; 2031 -6.2; 2234 -6.5; 2457 -7.2; 2703 -8.2; 2973 -8.6; 3270 -8.3; 3597 -7.9; 3957 -8.9; 4353 -10.9; 4788 -11.8; 5267 -9.5; 5793 -4.0; 6373 -5.9; 7010 -14.7; 7711 -20.0; 8482 -19.5; 9330 -14.9; 10263 -11.7; 11289 -12.7; 12418 -13.5; 13660 -10.5; 15026 -6.7; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony SA3000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony SA3000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 38 Hz    | 0.19 | 6.1 dB   |
| Peaking | 345 Hz   | 0.69 | 2.2 dB   |
| Peaking | 992 Hz   | 1.31 | -2.7 dB  |
| Peaking | 8152 Hz  | 3.21 | -14.6 dB |
| Peaking | 12145 Hz | 2.58 | -6.3 dB  |
| Peaking | 1890 Hz  | 3.41 | 1.3 dB   |
| Peaking | 2906 Hz  | 4.5  | -1.6 dB  |
| Peaking | 4796 Hz  | 3.21 | -5.5 dB  |
| Peaking | 6047 Hz  | 4.68 | 8.5 dB   |
| Peaking | 7216 Hz  | 7.2  | -4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB   |
| Peaking | 62 Hz    | 1.41 | 4.8 dB   |
| Peaking | 125 Hz   | 1.41 | 3.7 dB   |
| Peaking | 250 Hz   | 1.41 | 3.6 dB   |
| Peaking | 500 Hz   | 1.41 | 2.0 dB   |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -10.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20SA3000/Sony%20SA3000.png)