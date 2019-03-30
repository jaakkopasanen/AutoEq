# Sony MDR-V700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -2.0; 45 -3.7; 49 -5.1; 54 -6.7; 60 -8.2; 66 -9.2; 72 -9.8; 79 -10.2; 87 -10.7; 96 -10.9; 106 -10.9; 116 -10.9; 128 -10.8; 141 -10.5; 155 -10.3; 170 -10.0; 187 -9.8; 206 -9.5; 227 -9.1; 249 -8.6; 274 -7.9; 302 -7.0; 332 -6.0; 365 -4.7; 402 -3.7; 442 -3.8; 486 -4.5; 535 -5.6; 588 -6.7; 647 -7.3; 712 -7.1; 783 -6.4; 861 -5.9; 947 -6.0; 1042 -6.6; 1146 -7.4; 1261 -8.0; 1387 -8.3; 1526 -8.1; 1678 -7.4; 1846 -7.0; 2031 -7.4; 2234 -8.3; 2457 -9.0; 2703 -9.1; 2973 -8.6; 3270 -7.8; 3597 -6.2; 3957 -3.5; 4353 -0.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.1; 9330 -7.6; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-V700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.61 | 12.0 dB |
| Peaking | 71 Hz   | 0.42 | -8.9 dB |
| Peaking | 409 Hz  | 2.49 | 4.3 dB  |
| Peaking | 2966 Hz | 1.11 | -4.1 dB |
| Peaking | 4887 Hz | 1.68 | 8.6 dB  |
| Peaking | 15 Hz   | 1.99 | 1.3 dB  |
| Peaking | 907 Hz  | 6.38 | 1.1 dB  |
| Peaking | 1328 Hz | 5.22 | -1.3 dB |
| Peaking | 6387 Hz | 6.16 | 2.8 dB  |
| Peaking | 8610 Hz | 2.12 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.6 dB  |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20MDR-V700/Sony%20MDR-V700.png)