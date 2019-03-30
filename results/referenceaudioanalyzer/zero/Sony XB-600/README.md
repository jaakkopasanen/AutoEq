# Sony XB-600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.4; 23 -14.7; 25 -14.9; 28 -15.1; 31 -15.3; 34 -15.3; 37 -15.3; 41 -15.3; 45 -15.3; 49 -15.5; 54 -15.6; 60 -15.6; 66 -15.6; 72 -15.6; 79 -15.5; 87 -15.6; 96 -15.6; 106 -15.6; 116 -15.5; 128 -15.2; 141 -15.0; 155 -15.0; 170 -14.6; 187 -13.7; 206 -12.6; 227 -11.7; 249 -10.9; 274 -9.9; 302 -8.6; 332 -7.2; 365 -5.8; 402 -4.3; 442 -2.9; 486 -1.8; 535 -1.2; 588 -1.1; 647 -1.4; 712 -2.0; 783 -2.5; 861 -2.9; 947 -3.0; 1042 -2.8; 1146 -2.4; 1261 -2.3; 1387 -2.3; 1526 -2.1; 1678 -2.0; 1846 -2.1; 2031 -2.4; 2234 -2.6; 2457 -2.9; 2703 -2.9; 2973 -1.8; 3270 -0.5; 3597 -0.5; 3957 -2.1; 4353 -8.2; 4788 -11.3; 5267 -11.6; 5793 -11.4; 6373 -11.9; 7010 -12.0; 7711 -10.7; 8482 -8.0; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.6; 13660 -7.5; 15026 -6.8; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XB-600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XB-600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 101 Hz  | 0.1  | -9.3 dB  |
| Peaking | 283 Hz  | 0.3  | -12.9 dB |
| Peaking | 474 Hz  | 0.35 | 23.5 dB  |
| Peaking | 3639 Hz | 2.35 | 9.0 dB   |
| Peaking | 5138 Hz | 1.18 | -9.9 dB  |
| Peaking | 914 Hz  | 3.99 | -0.9 dB  |
| Peaking | 1717 Hz | 3.26 | 0.6 dB   |
| Peaking | 5768 Hz | 4.33 | 2.8 dB   |
| Peaking | 7446 Hz | 1.45 | -3.8 dB  |
| Peaking | 9004 Hz | 2.04 | 3.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.6 dB |
| Peaking | 62 Hz    | 1.41 | -6.6 dB |
| Peaking | 125 Hz   | 1.41 | -7.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | 6.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20XB-600/Sony%20XB-600.png)