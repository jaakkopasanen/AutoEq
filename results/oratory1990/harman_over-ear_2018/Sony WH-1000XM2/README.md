# Sony WH-1000XM2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.3; 25 -7.5; 28 -7.9; 31 -8.1; 34 -8.2; 37 -8.4; 41 -8.4; 45 -8.4; 49 -8.4; 54 -8.3; 60 -8.2; 66 -8.2; 72 -8.2; 79 -8.4; 87 -8.6; 96 -8.8; 106 -9.1; 116 -9.4; 128 -9.6; 141 -9.8; 155 -9.8; 170 -9.8; 187 -9.8; 206 -9.6; 227 -9.3; 249 -8.9; 274 -8.3; 302 -7.7; 332 -7.0; 365 -6.4; 402 -5.8; 442 -5.3; 486 -4.9; 535 -4.5; 588 -4.1; 647 -3.7; 712 -3.2; 783 -0.6; 861 -0.5; 947 -0.5; 1042 -1.1; 1146 -3.4; 1261 -6.1; 1387 -7.7; 1526 -8.7; 1678 -8.6; 1846 -7.7; 2031 -7.3; 2234 -7.2; 2457 -7.2; 2703 -8.0; 2973 -7.4; 3270 -5.1; 3597 -5.0; 3957 -7.2; 4353 -7.2; 4788 -5.9; 5267 -8.5; 5793 -11.2; 6373 -6.2; 7010 -5.4; 7711 -7.3; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.7; 12418 -11.1; 13660 -9.7; 15026 -6.4; 16529 -6.4; 18182 -6.6; 20000 -9.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-1000XM2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-1000XM2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 163 Hz   |  0.42 | -3.7 dB  |
| Peaking | 1052 Hz  |  0.86 | 15.1 dB  |
| Peaking | 1369 Hz  |  1.06 | -12.9 dB |
| Peaking | 5656 Hz  | 10.38 | -5.9 dB  |
| Peaking | 12830 Hz |  4.05 | -5.3 dB  |
| Peaking | 35 Hz    |  2.06 | -1.2 dB  |
| Peaking | 669 Hz   |  6.58 | -1.2 dB  |
| Peaking | 2807 Hz  |  7.85 | -1.8 dB  |
| Peaking | 3384 Hz  |  7.58 | 2.2 dB   |
| Peaking | 10826 Hz |  5.79 | 1.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sony%20WH-1000XM2/Sony%20WH-1000XM2.png)