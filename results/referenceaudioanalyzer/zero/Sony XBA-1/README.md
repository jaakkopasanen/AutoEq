# Sony XBA-1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.7; 25 -5.9; 28 -6.2; 31 -6.4; 34 -6.5; 37 -6.6; 41 -6.7; 45 -6.7; 49 -6.7; 54 -6.8; 60 -7.0; 66 -7.0; 72 -6.8; 79 -6.7; 87 -6.7; 96 -6.7; 106 -6.7; 116 -6.7; 128 -6.5; 141 -6.4; 155 -6.3; 170 -6.1; 187 -6.3; 206 -6.6; 227 -6.7; 249 -6.5; 274 -6.4; 302 -6.2; 332 -6.1; 365 -5.9; 402 -5.7; 442 -5.5; 486 -5.4; 535 -5.2; 588 -5.0; 647 -4.8; 712 -4.5; 783 -4.2; 861 -4.0; 947 -3.7; 1042 -3.4; 1146 -3.2; 1261 -2.9; 1387 -2.7; 1526 -2.5; 1678 -2.4; 1846 -2.1; 2031 -2.3; 2234 -4.7; 2457 -7.0; 2703 -8.5; 2973 -10.2; 3270 -11.6; 3597 -11.7; 3957 -9.6; 4353 -6.7; 4788 -4.4; 5267 -2.8; 5793 -1.7; 6373 -0.5; 7010 -2.5; 7711 -4.8; 8482 -5.0; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 61 Hz   |  0.48 | -1.8 dB |
| Peaking | 267 Hz  |  1.11 | -1.1 dB |
| Peaking | 1882 Hz |  0.93 | 5.1 dB  |
| Peaking | 3285 Hz |  1.43 | -9.7 dB |
| Peaking | 5810 Hz |  2.09 | 5.9 dB  |
| Peaking | 2053 Hz |  6.83 | 1.9 dB  |
| Peaking | 2206 Hz |  3.88 | -1.2 dB |
| Peaking | 6602 Hz | 10.35 | 2.0 dB  |
| Peaking | 6975 Hz |  6.79 | 1.0 dB  |
| Peaking | 7375 Hz |  2.78 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.8 dB |
| Peaking | 8000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20XBA-1/Sony%20XBA-1.png)