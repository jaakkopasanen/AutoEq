# Sony MDR-XB950
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.5; 23 -14.9; 25 -15.2; 28 -15.5; 31 -15.7; 34 -15.7; 37 -15.7; 41 -15.7; 45 -16.0; 49 -16.3; 54 -16.3; 60 -16.0; 66 -15.9; 72 -16.0; 79 -16.2; 87 -16.4; 96 -16.6; 106 -16.6; 116 -16.7; 128 -16.6; 141 -16.5; 155 -16.2; 170 -15.8; 187 -15.2; 206 -14.4; 227 -13.4; 249 -12.2; 274 -10.8; 302 -9.4; 332 -8.3; 365 -7.4; 402 -6.9; 442 -7.2; 486 -7.6; 535 -8.2; 588 -8.6; 647 -8.8; 712 -8.8; 783 -8.5; 861 -8.1; 947 -7.7; 1042 -7.3; 1146 -6.7; 1261 -6.1; 1387 -5.6; 1526 -4.9; 1678 -4.2; 1846 -3.4; 2031 -2.7; 2234 -2.0; 2457 -1.3; 2703 -1.5; 2973 -1.9; 3270 -1.1; 3597 -0.5; 3957 -0.5; 4353 -0.7; 4788 -3.0; 5267 -4.4; 5793 -5.1; 6373 -4.8; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB950 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB950 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 51 Hz   | 0.35 | -8.7 dB |
| Peaking | 156 Hz  | 1.04 | -5.4 dB |
| Peaking | 2315 Hz | 2.01 | 4.0 dB  |
| Peaking | 3880 Hz | 1.83 | 5.7 dB  |
| Peaking | 22 Hz   | 1.16 | -2.2 dB |
| Peaking | 233 Hz  | 3.28 | -1.1 dB |
| Peaking | 382 Hz  | 1.99 | 2.0 dB  |
| Peaking | 648 Hz  | 2.33 | -1.9 dB |
| Peaking | 880 Hz  | 3.16 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.1 dB |
| Peaking | 62 Hz    | 1.41 | -6.5 dB |
| Peaking | 125 Hz   | 1.41 | -9.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB |
| Peaking | 2000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20MDR-XB950/Sony%20MDR-XB950.png)