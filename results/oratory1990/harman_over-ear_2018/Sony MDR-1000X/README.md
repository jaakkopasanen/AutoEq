# Sony MDR-1000X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -8.0; 25 -8.2; 28 -8.4; 31 -8.4; 34 -8.4; 37 -8.2; 41 -8.0; 45 -7.8; 49 -7.7; 54 -7.6; 60 -7.6; 66 -7.8; 72 -8.0; 79 -8.4; 87 -8.9; 96 -9.3; 106 -9.7; 116 -10.0; 128 -10.2; 141 -10.3; 155 -10.2; 170 -10.1; 187 -9.7; 206 -9.3; 227 -8.9; 249 -8.8; 274 -8.7; 302 -8.2; 332 -7.2; 365 -6.3; 402 -6.0; 442 -6.4; 486 -6.6; 535 -6.3; 588 -5.1; 647 -5.1; 712 -5.7; 783 -2.8; 861 -1.0; 947 -0.9; 1042 -0.5; 1146 -0.5; 1261 -0.9; 1387 -2.8; 1526 -5.3; 1678 -7.0; 1846 -8.0; 2031 -7.9; 2234 -6.3; 2457 -5.9; 2703 -6.9; 2973 -7.8; 3270 -6.3; 3597 -6.1; 3957 -8.9; 4353 -9.4; 4788 -8.0; 5267 -9.4; 5793 -13.9; 6373 -7.1; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 1.45 | -1.7 dB |
| Peaking | 147 Hz  | 0.78 | -3.9 dB |
| Peaking | 1096 Hz | 1.46 | 7.2 dB  |
| Peaking | 1796 Hz | 2.33 | -3.6 dB |
| Peaking | 5705 Hz | 7.65 | -8.0 dB |
| Peaking | 382 Hz  | 1.13 | -1.9 dB |
| Peaking | 385 Hz  | 3.37 | 2.5 dB  |
| Peaking | 411 Hz  | 0.35 | 0.5 dB  |
| Peaking | 4227 Hz | 6.53 | -3.2 dB |
| Peaking | 6857 Hz | 8.86 | 3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | -2.2 dB |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sony%20MDR-1000X/Sony%20MDR-1000X.png)