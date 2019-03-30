# Sony XBA-C10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.2; 25 -9.2; 28 -9.2; 31 -9.2; 34 -9.2; 37 -9.2; 41 -9.2; 45 -9.2; 49 -9.2; 54 -9.0; 60 -8.9; 66 -8.9; 72 -8.9; 79 -8.7; 87 -8.5; 96 -8.6; 106 -8.4; 116 -8.2; 128 -8.2; 141 -7.9; 155 -7.9; 170 -7.9; 187 -8.0; 206 -8.2; 227 -8.2; 249 -8.2; 274 -8.0; 302 -7.7; 332 -7.5; 365 -7.2; 402 -7.0; 442 -6.7; 486 -6.4; 535 -6.1; 588 -5.9; 647 -5.5; 712 -5.2; 783 -4.9; 861 -4.6; 947 -4.2; 1042 -3.9; 1146 -3.5; 1261 -3.2; 1387 -2.9; 1526 -2.5; 1678 -2.3; 1846 -2.0; 2031 -2.1; 2234 -2.6; 2457 -3.6; 2703 -4.7; 2973 -5.9; 3270 -7.0; 3597 -7.7; 3957 -7.7; 4353 -7.1; 4788 -5.7; 5267 -3.9; 5793 -2.2; 6373 -0.5; 7010 -2.4; 7711 -4.6; 8482 -4.9; 9330 -4.9; 10263 -4.9; 11289 -4.9; 12418 -4.9; 13660 -4.9; 15026 -4.9; 16529 -4.9; 18182 -4.9; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-C10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-C10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.23 | -4.3 dB |
| Peaking | 285 Hz  | 0.7  | -2.3 dB |
| Peaking | 2012 Hz | 0.88 | 4.1 dB  |
| Peaking | 3608 Hz | 1.34 | -4.9 dB |
| Peaking | 6268 Hz | 3.54 | 5.3 dB  |
| Peaking | 5258 Hz | 9.28 | 0.7 dB  |
| Peaking | 7944 Hz | 5.75 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.9 dB |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20XBA-C10/Sony%20XBA-C10.png)