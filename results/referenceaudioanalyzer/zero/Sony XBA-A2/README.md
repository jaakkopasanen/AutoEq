# Sony XBA-A2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.7; 23 -12.9; 25 -13.0; 28 -13.2; 31 -13.4; 34 -13.5; 37 -13.5; 41 -13.6; 45 -13.5; 49 -13.4; 54 -13.3; 60 -13.2; 66 -13.1; 72 -12.9; 79 -12.7; 87 -12.4; 96 -12.2; 106 -11.9; 116 -11.9; 128 -11.8; 141 -11.4; 155 -11.0; 170 -10.7; 187 -10.4; 206 -10.0; 227 -9.6; 249 -9.1; 274 -8.7; 302 -8.2; 332 -7.8; 365 -7.3; 402 -6.9; 442 -6.6; 486 -6.2; 535 -5.8; 588 -5.4; 647 -5.1; 712 -4.8; 783 -4.5; 861 -4.2; 947 -3.9; 1042 -3.6; 1146 -3.4; 1261 -3.2; 1387 -3.0; 1526 -2.7; 1678 -2.2; 1846 -1.7; 2031 -3.2; 2234 -4.9; 2457 -5.4; 2703 -5.7; 2973 -5.6; 3270 -5.7; 3597 -6.6; 3957 -7.8; 4353 -8.1; 4788 -7.1; 5267 -5.5; 5793 -3.5; 6373 -0.5; 7010 -2.8; 7711 -5.1; 8482 -5.3; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.5; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-A2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-A2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.55 | -4.4 dB |
| Peaking | 81 Hz   | 0.31 | -6.4 dB |
| Peaking | 1555 Hz | 0.73 | 3.5 dB  |
| Peaking | 4318 Hz | 0.93 | -3.6 dB |
| Peaking | 6368 Hz | 3.68 | 6.6 dB  |
| Peaking | 1361 Hz | 3.33 | -0.5 dB |
| Peaking | 1884 Hz | 3.92 | 2.1 dB  |
| Peaking | 2282 Hz | 2.62 | -1.8 dB |
| Peaking | 3321 Hz | 2.94 | 1.2 dB  |
| Peaking | 4114 Hz | 5.92 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20XBA-A2/Sony%20XBA-A2.png)