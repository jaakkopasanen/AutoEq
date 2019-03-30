# Sony MDR-XB700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.7; 25 -6.2; 28 -6.6; 31 -6.8; 34 -6.9; 37 -6.8; 41 -6.8; 45 -7.1; 49 -7.7; 54 -8.5; 60 -9.1; 66 -9.5; 72 -9.8; 79 -10.1; 87 -10.4; 96 -10.8; 106 -11.1; 116 -11.2; 128 -10.9; 141 -10.2; 155 -9.9; 170 -10.0; 187 -10.3; 206 -10.5; 227 -10.1; 249 -9.6; 274 -8.9; 302 -8.2; 332 -7.5; 365 -7.0; 402 -6.5; 442 -5.7; 486 -4.5; 535 -3.5; 588 -2.6; 647 -1.2; 712 -0.5; 783 -0.5; 861 -0.5; 947 -0.7; 1042 -2.7; 1146 -4.8; 1261 -6.3; 1387 -7.3; 1526 -8.3; 1678 -9.1; 1846 -9.2; 2031 -8.8; 2234 -7.6; 2457 -6.0; 2703 -4.8; 2973 -4.1; 3270 -4.4; 3597 -5.5; 3957 -6.6; 4353 -6.3; 4788 -4.9; 5267 -4.0; 5793 -3.4; 6373 -4.2; 7010 -7.6; 7711 -9.5; 8482 -9.2; 9330 -8.3; 10263 -7.8; 11289 -6.8; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 102 Hz  | 0.97 | -4.4 dB |
| Peaking | 223 Hz  | 1.67 | -2.9 dB |
| Peaking | 751 Hz  | 1.9  | 7.1 dB  |
| Peaking | 6042 Hz | 2.27 | 5.5 dB  |
| Peaking | 7623 Hz | 1.92 | -5.1 dB |
| Peaking | 16 Hz   | 1.84 | 2.1 dB  |
| Peaking | 777 Hz  | 3.74 | -3.8 dB |
| Peaking | 895 Hz  | 1.53 | 4.8 dB  |
| Peaking | 1774 Hz | 0.91 | -4.6 dB |
| Peaking | 2846 Hz | 2.35 | 4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20MDR-XB700/Sony%20MDR-XB700.png)