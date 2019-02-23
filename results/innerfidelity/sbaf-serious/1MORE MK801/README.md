# 1MORE MK801
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.7; 25 -3.4; 28 -4.3; 31 -5.0; 34 -5.5; 37 -6.0; 41 -6.5; 45 -6.9; 49 -7.2; 54 -7.6; 60 -7.9; 66 -8.2; 72 -8.5; 79 -8.9; 87 -9.3; 96 -9.5; 106 -9.7; 116 -9.6; 128 -9.9; 141 -10.1; 155 -10.4; 170 -10.0; 187 -10.3; 206 -10.5; 227 -10.4; 249 -10.3; 274 -10.0; 302 -9.4; 332 -8.7; 365 -8.0; 402 -7.4; 442 -6.4; 486 -5.5; 535 -5.1; 588 -5.0; 647 -5.3; 712 -6.1; 783 -5.7; 861 -5.2; 947 -6.8; 1042 -7.6; 1146 -7.4; 1261 -6.8; 1387 -6.2; 1526 -5.5; 1678 -4.7; 1846 -3.7; 2031 -2.9; 2234 -2.7; 2457 -2.5; 2703 -2.7; 2973 -3.0; 3270 -3.0; 3597 -2.3; 3957 -2.7; 4353 -5.0; 4788 -4.6; 5267 -2.2; 5793 -0.5; 6373 -0.6; 7010 -3.5; 7711 -5.8; 8482 -7.4; 9330 -6.3; 10263 -6.1; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE MK801 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE MK801 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.69 | 4.4 dB  |
| Peaking | 115 Hz  | 0.7  | -3.6 dB |
| Peaking | 242 Hz  | 1.75 | -3.1 dB |
| Peaking | 2739 Hz | 1.33 | 3.8 dB  |
| Peaking | 6025 Hz | 4.28 | 6.0 dB  |
| Peaking | 566 Hz  | 2.84 | 1.7 dB  |
| Peaking | 1135 Hz | 3.32 | -2.1 dB |
| Peaking | 1974 Hz | 5.57 | 1.1 dB  |
| Peaking | 6640 Hz | 8.52 | 1.2 dB  |
| Peaking | 8377 Hz | 4.56 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/1MORE%20MK801/1MORE%20MK801.png)