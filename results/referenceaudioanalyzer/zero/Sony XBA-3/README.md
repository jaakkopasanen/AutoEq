# Sony XBA-3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.6; 23 -13.7; 25 -13.9; 28 -14.0; 31 -14.1; 34 -14.2; 37 -14.1; 41 -14.0; 45 -13.9; 49 -13.8; 54 -13.6; 60 -13.3; 66 -13.0; 72 -12.8; 79 -12.4; 87 -12.1; 96 -11.9; 106 -11.7; 116 -11.2; 128 -10.7; 141 -10.2; 155 -9.6; 170 -9.0; 187 -8.7; 206 -8.7; 227 -8.7; 249 -8.3; 274 -7.8; 302 -7.3; 332 -6.9; 365 -6.5; 402 -6.1; 442 -5.7; 486 -5.4; 535 -5.1; 588 -4.8; 647 -4.5; 712 -4.2; 783 -3.9; 861 -3.7; 947 -3.5; 1042 -3.4; 1146 -3.2; 1261 -3.1; 1387 -2.9; 1526 -2.8; 1678 -2.8; 1846 -2.9; 2031 -4.4; 2234 -6.7; 2457 -8.3; 2703 -9.8; 2973 -11.3; 3270 -11.8; 3597 -11.7; 3957 -11.7; 4353 -9.2; 4788 -6.2; 5267 -3.5; 5793 -1.1; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -7.3; 12418 -8.2; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 33 Hz    |  0.23 | -8.1 dB  |
| Peaking | 1907 Hz  |  0.59 | 9.1 dB   |
| Peaking | 3246 Hz  |  0.78 | -13.4 dB |
| Peaking | 5958 Hz  |  2.21 | 9.5 dB   |
| Peaking | 12057 Hz |  6.44 | -2.4 dB  |
| Peaking | 171 Hz   |  7.56 | 0.4 dB   |
| Peaking | 1277 Hz  |  3.59 | -0.5 dB  |
| Peaking | 1873 Hz  |  9.98 | 1.0 dB   |
| Peaking | 4844 Hz  |  8.4  | 1.0 dB   |
| Peaking | 7626 Hz  | 11.3  | -0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.5 dB |
| Peaking | 62 Hz    | 1.41 | -5.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.1 dB |
| Peaking | 8000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20XBA-3/Sony%20XBA-3.png)