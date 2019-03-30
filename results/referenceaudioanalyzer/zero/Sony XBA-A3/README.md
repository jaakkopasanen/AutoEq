# Sony XBA-A3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.8; 23 -10.9; 25 -10.9; 28 -11.0; 31 -11.1; 34 -11.1; 37 -11.2; 41 -11.1; 45 -11.0; 49 -10.9; 54 -10.8; 60 -10.8; 66 -10.8; 72 -10.8; 79 -10.6; 87 -10.5; 96 -10.4; 106 -10.2; 116 -10.0; 128 -9.8; 141 -9.6; 155 -9.5; 170 -9.5; 187 -9.2; 206 -9.1; 227 -8.9; 249 -8.6; 274 -8.3; 302 -7.7; 332 -6.9; 365 -6.3; 402 -6.4; 442 -6.6; 486 -6.4; 535 -6.2; 588 -6.0; 647 -6.0; 712 -5.9; 783 -5.6; 861 -5.6; 947 -5.6; 1042 -5.3; 1146 -5.3; 1261 -5.1; 1387 -5.0; 1526 -4.9; 1678 -4.5; 1846 -4.1; 2031 -5.3; 2234 -6.9; 2457 -7.3; 2703 -7.2; 2973 -7.3; 3270 -7.1; 3597 -6.9; 3957 -7.2; 4353 -8.6; 4788 -9.0; 5267 -6.8; 5793 -3.0; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -6.8; 12418 -8.0; 13660 -6.3; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-A3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-A3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.19 | -5.2 dB |
| Peaking | 1545 Hz  | 0.98 | 2.5 dB  |
| Peaking | 4143 Hz  | 0.39 | -2.3 dB |
| Peaking | 4816 Hz  | 4.79 | -2.9 dB |
| Peaking | 6303 Hz  | 3.23 | 7.6 dB  |
| Peaking | 375 Hz   | 5.94 | 1.0 dB  |
| Peaking | 1910 Hz  | 5.4  | 1.9 dB  |
| Peaking | 2208 Hz  | 3.04 | -1.3 dB |
| Peaking | 10138 Hz | 3.15 | 1.0 dB  |
| Peaking | 12296 Hz | 4.82 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.3 dB |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20XBA-A3/Sony%20XBA-A3.png)