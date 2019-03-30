# Sony MDR 1R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.5; 25 -2.4; 28 -3.5; 31 -4.4; 34 -5.1; 37 -5.7; 41 -6.2; 45 -6.4; 49 -6.5; 54 -6.9; 60 -8.1; 66 -9.3; 72 -10.1; 79 -10.4; 87 -10.6; 96 -10.7; 106 -11.0; 116 -11.0; 128 -10.9; 141 -10.3; 155 -9.2; 170 -8.2; 187 -7.7; 206 -8.0; 227 -8.4; 249 -8.3; 274 -7.7; 302 -6.9; 332 -5.9; 365 -4.9; 402 -4.0; 442 -3.4; 486 -2.9; 535 -3.0; 588 -3.6; 647 -4.3; 712 -4.7; 783 -4.8; 861 -5.0; 947 -5.4; 1042 -5.7; 1146 -6.0; 1261 -6.2; 1387 -6.4; 1526 -6.6; 1678 -6.8; 1846 -6.9; 2031 -7.2; 2234 -7.5; 2457 -7.7; 2703 -7.6; 2973 -6.5; 3270 -4.8; 3597 -3.9; 3957 -3.8; 4353 -3.9; 4788 -3.5; 5267 -2.6; 5793 -1.7; 6373 -2.5; 7010 -4.0; 7711 -5.8; 8482 -7.2; 9330 -8.7; 10263 -8.0; 11289 -6.2; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR 1R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR 1R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.85 | 8.3 dB  |
| Peaking | 102 Hz  | 0.72 | -5.2 dB |
| Peaking | 499 Hz  | 1.85 | 3.9 dB  |
| Peaking | 3971 Hz | 4.21 | 2.2 dB  |
| Peaking | 5800 Hz | 3.73 | 4.8 dB  |
| Peaking | 14 Hz   | 0.33 | 0.3 dB  |
| Peaking | 179 Hz  | 5.51 | 1.2 dB  |
| Peaking | 250 Hz  | 4.22 | -1.2 dB |
| Peaking | 2353 Hz | 2.88 | -2.0 dB |
| Peaking | 9497 Hz | 4.63 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 3.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20MDR%201R/Sony%20MDR%201R.png)