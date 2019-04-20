# Sony WH-1000XM2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.3; 25 -7.6; 28 -7.9; 31 -8.1; 34 -8.3; 37 -8.4; 41 -8.5; 45 -8.5; 49 -8.4; 54 -8.4; 60 -8.3; 66 -8.3; 72 -8.3; 79 -8.4; 87 -8.6; 96 -8.9; 106 -9.2; 116 -9.4; 128 -9.7; 141 -9.8; 155 -9.9; 170 -9.9; 187 -9.8; 206 -9.7; 227 -9.4; 249 -8.9; 274 -8.4; 302 -7.7; 332 -7.1; 365 -6.4; 402 -5.8; 442 -5.3; 486 -4.9; 535 -4.5; 588 -4.1; 647 -3.7; 712 -3.1; 783 -0.7; 861 -0.5; 947 -0.6; 1042 -1.2; 1146 -3.5; 1261 -6.1; 1387 -7.7; 1526 -8.8; 1678 -8.6; 1846 -7.7; 2031 -7.4; 2234 -7.2; 2457 -7.2; 2703 -8.1; 2973 -7.3; 3270 -5.1; 3597 -5.1; 3957 -7.1; 4353 -7.3; 4788 -5.9; 5267 -8.6; 5793 -11.1; 6373 -6.2; 7010 -5.4; 7711 -7.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.7; 12418 -11.2; 13660 -9.7; 15026 -6.5; 16529 -6.5; 18182 -6.7; 20000 -9.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-1000XM2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-1000XM2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 154 Hz   | 0.45 | -3.6 dB  |
| Peaking | 1040 Hz  | 0.94 | 12.5 dB  |
| Peaking | 1382 Hz  | 1.18 | -10.4 dB |
| Peaking | 5668 Hz  | 9.6  | -5.4 dB  |
| Peaking | 12944 Hz | 4.71 | -5.7 dB  |
| Peaking | 33 Hz    | 2.11 | -1.3 dB  |
| Peaking | 2831 Hz  | 4.52 | -2.6 dB  |
| Peaking | 3386 Hz  | 4.18 | 1.8 dB   |
| Peaking | 3805 Hz  | 1.38 | 1.2 dB   |
| Peaking | 4099 Hz  | 5.73 | -2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
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