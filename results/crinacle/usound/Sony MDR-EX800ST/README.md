# Sony MDR-EX800ST
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.3; 28 -1.8; 31 -2.1; 34 -2.3; 37 -2.5; 41 -2.8; 45 -3.1; 49 -3.4; 54 -3.6; 60 -4.0; 66 -4.3; 72 -4.7; 79 -5.2; 87 -5.7; 96 -6.1; 106 -6.6; 116 -7.0; 128 -7.4; 141 -7.8; 155 -8.1; 170 -8.4; 187 -8.6; 206 -8.8; 227 -8.9; 249 -8.9; 274 -9.0; 302 -9.0; 332 -9.0; 365 -8.9; 402 -8.8; 442 -8.8; 486 -8.6; 535 -8.3; 588 -8.1; 647 -7.7; 712 -7.2; 783 -7.0; 861 -6.1; 947 -5.8; 1042 -6.3; 1146 -6.9; 1261 -7.9; 1387 -8.8; 1526 -9.1; 1678 -9.0; 1846 -8.4; 2031 -7.5; 2234 -6.3; 2457 -4.7; 2703 -3.1; 2973 -1.7; 3270 -0.8; 3597 -0.7; 3957 -0.7; 4353 -1.9; 4788 -4.9; 5267 -9.4; 5793 -7.7; 6373 -3.6; 7010 -4.2; 7711 -7.0; 8482 -7.4; 9330 -6.7; 10263 -6.7; 11289 -6.7; 12418 -6.7; 13660 -6.7; 15026 -6.7; 16529 -6.7; 18182 -6.7; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX800ST GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX800ST ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.66 | 6.4 dB  |
| Peaking | 61 Hz    | 1.23 | 2.6 dB  |
| Peaking | 390 Hz   | 0.07 | -1.8 dB |
| Peaking | 3468 Hz  | 1.89 | 8.1 dB  |
| Peaking | 21197 Hz | 2.21 | 0.7 dB  |
| Peaking | 943 Hz   | 2.69 | 2.7 dB  |
| Peaking | 1599 Hz  | 2.97 | -2.0 dB |
| Peaking | 4430 Hz  | 5.09 | 2.5 dB  |
| Peaking | 5382 Hz  | 4.71 | -5.1 dB |
| Peaking | 6553 Hz  | 6.23 | 4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.5 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20MDR-EX800ST/Sony%20MDR-EX800ST.png)