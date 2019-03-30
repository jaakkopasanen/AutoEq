# Sony XBA-2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.5; 23 -14.5; 25 -14.5; 28 -14.5; 31 -14.5; 34 -14.4; 37 -14.3; 41 -14.2; 45 -14.1; 49 -14.0; 54 -13.8; 60 -13.6; 66 -13.4; 72 -13.2; 79 -12.9; 87 -12.7; 96 -12.4; 106 -12.1; 116 -11.8; 128 -11.5; 141 -11.1; 155 -10.8; 170 -10.5; 187 -10.2; 206 -9.9; 227 -9.6; 249 -9.3; 274 -9.0; 302 -8.6; 332 -8.3; 365 -8.0; 402 -7.7; 442 -7.5; 486 -7.1; 535 -7.0; 588 -7.0; 647 -7.0; 712 -6.8; 783 -6.4; 861 -6.0; 947 -5.7; 1042 -5.3; 1146 -5.0; 1261 -4.7; 1387 -4.4; 1526 -4.5; 1678 -4.4; 1846 -4.5; 2031 -5.0; 2234 -5.9; 2457 -7.3; 2703 -9.5; 2973 -11.6; 3270 -12.3; 3597 -10.9; 3957 -7.9; 4353 -5.0; 4788 -3.2; 5267 -1.8; 5793 -0.5; 6373 -0.9; 7010 -3.8; 7711 -6.0; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.19 | -8.1 dB |
| Peaking | 207 Hz  | 0.45 | -1.2 dB |
| Peaking | 1680 Hz | 1    | 2.7 dB  |
| Peaking | 3193 Hz | 2.47 | -7.9 dB |
| Peaking | 5665 Hz | 2.41 | 6.7 dB  |
| Peaking | 4560 Hz | 5.26 | 1.6 dB  |
| Peaking | 6239 Hz | 6.5  | 1.9 dB  |
| Peaking | 6616 Hz | 1.65 | -2.3 dB |
| Peaking | 6702 Hz | 6.76 | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.6 dB |
| Peaking | 62 Hz    | 1.41 | -5.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB |
| Peaking | 8000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20XBA-2/Sony%20XBA-2.png)