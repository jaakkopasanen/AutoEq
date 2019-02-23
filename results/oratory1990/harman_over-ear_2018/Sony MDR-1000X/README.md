# Sony MDR-1000X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.8; 25 -8.0; 28 -8.3; 31 -8.4; 34 -8.4; 37 -8.4; 41 -8.3; 45 -8.2; 49 -8.1; 54 -8.0; 60 -8.0; 66 -8.2; 72 -8.4; 79 -8.7; 87 -9.1; 96 -9.5; 106 -9.9; 116 -10.2; 128 -10.3; 141 -10.4; 155 -10.4; 170 -10.2; 187 -9.9; 206 -9.5; 227 -9.0; 249 -8.9; 274 -8.9; 302 -8.4; 332 -7.3; 365 -6.2; 402 -6.0; 442 -6.5; 486 -6.6; 535 -6.4; 588 -5.1; 647 -5.4; 712 -6.5; 783 -3.0; 861 -1.9; 947 -1.2; 1042 -0.6; 1146 -0.5; 1261 -1.1; 1387 -3.1; 1526 -5.9; 1678 -7.9; 1846 -8.8; 2031 -8.2; 2234 -6.4; 2457 -5.6; 2703 -5.5; 2973 -5.1; 3270 -5.0; 3597 -5.4; 3957 -8.3; 4353 -9.0; 4788 -7.3; 5267 -9.0; 5793 -13.3; 6373 -6.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.0; 13660 -6.9; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 31 Hz   |  1.24 | -1.7 dB |
| Peaking | 148 Hz  |  0.75 | -4.0 dB |
| Peaking | 1122 Hz |  1.42 | 6.9 dB  |
| Peaking | 1766 Hz |  3.26 | -5.0 dB |
| Peaking | 5674 Hz |  9.13 | -7.7 dB |
| Peaking | 384 Hz  |  3.47 | 2.8 dB  |
| Peaking | 387 Hz  |  1.61 | -1.6 dB |
| Peaking | 3316 Hz |  2.86 | 1.9 dB  |
| Peaking | 4177 Hz |  5.21 | -3.4 dB |
| Peaking | 6820 Hz | 10.5  | 4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sony%20MDR-1000X/Sony%20MDR-1000X.png)