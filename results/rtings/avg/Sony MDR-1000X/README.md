# Sony MDR-1000X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -7.9; 25 -7.6; 28 -7.2; 31 -6.9; 34 -6.7; 37 -6.5; 41 -6.2; 45 -6.1; 49 -6.1; 54 -6.2; 60 -6.5; 66 -6.7; 72 -7.0; 79 -7.3; 87 -7.7; 96 -8.1; 106 -8.4; 116 -8.6; 128 -8.8; 141 -8.9; 155 -8.8; 170 -8.6; 187 -8.1; 206 -7.5; 227 -6.9; 249 -6.8; 274 -7.1; 302 -6.8; 332 -5.9; 365 -5.0; 402 -5.4; 442 -5.9; 486 -6.1; 535 -5.7; 588 -4.5; 647 -5.1; 712 -6.6; 783 -5.7; 861 -4.0; 947 -3.8; 1042 -2.2; 1146 -0.5; 1261 -1.0; 1387 -2.6; 1526 -4.8; 1678 -6.3; 1846 -7.2; 2031 -7.1; 2234 -6.1; 2457 -4.2; 2703 -3.3; 2973 -3.4; 3270 -2.9; 3597 -3.2; 3957 -5.6; 4353 -7.2; 4788 -7.4; 5267 -8.5; 5793 -8.4; 6373 -5.2; 7010 -4.0; 7711 -6.4; 8482 -6.5; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.54 | -2.4 dB |
| Peaking | 134 Hz  | 1.1  | -3.3 dB |
| Peaking | 1195 Hz | 2.29 | 7.0 dB  |
| Peaking | 2677 Hz | 0.67 | -5.7 dB |
| Peaking | 2984 Hz | 1.73 | 8.6 dB  |
| Peaking | 376 Hz  | 6.69 | 1.2 dB  |
| Peaking | 3605 Hz | 6.23 | 2.9 dB  |
| Peaking | 3718 Hz | 2.39 | -1.4 dB |
| Peaking | 5563 Hz | 5.38 | -2.5 dB |
| Peaking | 6742 Hz | 6    | 3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-1000X/Sony%20MDR-1000X.png)