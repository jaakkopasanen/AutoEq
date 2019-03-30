# Echo TDS 16
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.2; 28 -1.6; 31 -1.9; 34 -2.4; 37 -3.3; 41 -4.6; 45 -5.7; 49 -6.2; 54 -6.5; 60 -6.9; 66 -7.3; 72 -7.5; 79 -7.9; 87 -8.2; 96 -8.5; 106 -8.4; 116 -8.2; 128 -8.1; 141 -7.8; 155 -7.8; 170 -7.8; 187 -7.5; 206 -7.5; 227 -7.3; 249 -7.5; 274 -7.5; 302 -7.8; 332 -8.0; 365 -8.2; 402 -8.4; 442 -8.6; 486 -8.8; 535 -9.0; 588 -9.3; 647 -9.7; 712 -10.0; 783 -10.2; 861 -10.4; 947 -10.3; 1042 -9.8; 1146 -8.9; 1261 -7.7; 1387 -6.2; 1526 -4.4; 1678 -2.4; 1846 -1.1; 2031 -0.8; 2234 -1.7; 2457 -2.6; 2703 -2.5; 2973 -1.6; 3270 -0.7; 3597 -1.0; 3957 -2.0; 4353 -3.2; 4788 -4.4; 5267 -5.2; 5793 -5.0; 6373 -3.5; 7010 -3.2; 7711 -5.4; 8482 -5.7; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Echo TDS 16 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Echo TDS 16 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.69 | 6.2 dB  |
| Peaking | 73 Hz   | 0.49 | -3.4 dB |
| Peaking | 930 Hz  | 0.64 | -5.4 dB |
| Peaking | 1849 Hz | 1.78 | 7.0 dB  |
| Peaking | 3453 Hz | 1.78 | 4.8 dB  |
| Peaking | 6453 Hz | 1.77 | -1.5 dB |
| Peaking | 6703 Hz | 5.19 | 4.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | -5.4 dB |
| Peaking | 2000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Echo%20TDS%2016/Echo%20TDS%2016.png)