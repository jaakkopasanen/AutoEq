# Sony XBA-A1AP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -6.3; 25 -6.8; 28 -7.3; 31 -7.8; 34 -8.1; 37 -8.3; 41 -8.6; 45 -8.8; 49 -9.0; 54 -9.2; 60 -9.4; 66 -9.5; 72 -9.4; 79 -9.3; 87 -9.1; 96 -8.9; 106 -9.1; 116 -9.1; 128 -9.0; 141 -8.5; 155 -8.0; 170 -7.9; 187 -8.2; 206 -8.1; 227 -7.7; 249 -7.4; 274 -7.1; 302 -6.6; 332 -6.2; 365 -5.8; 402 -5.4; 442 -5.0; 486 -4.6; 535 -4.4; 588 -4.0; 647 -3.8; 712 -3.6; 783 -3.5; 861 -3.3; 947 -3.3; 1042 -3.3; 1146 -3.3; 1261 -3.4; 1387 -3.6; 1526 -3.6; 1678 -3.4; 1846 -2.9; 2031 -3.6; 2234 -5.1; 2457 -5.6; 2703 -5.3; 2973 -4.6; 3270 -3.4; 3597 -2.6; 3957 -2.9; 4353 -4.0; 4788 -5.0; 5267 -5.5; 5793 -4.2; 6373 -0.5; 7010 -1.6; 7711 -3.8; 8482 -4.1; 9330 -4.1; 10263 -4.1; 11289 -4.1; 12418 -4.1; 13660 -4.1; 15026 -4.1; 16529 -4.1; 18182 -4.1; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-A1AP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-A1AP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 53 Hz   | 0.6  | -4.8 dB |
| Peaking | 123 Hz  | 1.19 | -2.4 dB |
| Peaking | 237 Hz  | 1.56 | -2.5 dB |
| Peaking | 5292 Hz | 6.42 | -2.0 dB |
| Peaking | 6588 Hz | 6.84 | 4.8 dB  |
| Peaking | 387 Hz  | 1.91 | -0.7 dB |
| Peaking | 1118 Hz | 0.57 | 1.0 dB  |
| Peaking | 2532 Hz | 3.69 | -2.3 dB |
| Peaking | 3647 Hz | 5.68 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20XBA-A1AP/Sony%20XBA-A1AP.png)