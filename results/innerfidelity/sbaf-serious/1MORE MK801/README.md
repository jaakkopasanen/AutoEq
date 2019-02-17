# 1MORE MK801
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.1; 23 -1.8; 25 -2.5; 28 -3.4; 31 -4.1; 34 -4.6; 37 -5.1; 41 -5.6; 45 -6.0; 49 -6.3; 54 -6.7; 60 -7.0; 66 -7.3; 72 -7.6; 79 -8.0; 87 -8.4; 96 -8.6; 106 -8.8; 116 -8.7; 128 -9.0; 141 -9.3; 155 -9.5; 170 -9.1; 187 -9.4; 206 -9.6; 227 -9.5; 249 -9.4; 274 -9.1; 302 -8.5; 332 -7.8; 365 -7.1; 402 -6.5; 442 -5.5; 486 -4.6; 535 -4.2; 588 -4.1; 647 -4.4; 712 -5.2; 783 -4.8; 861 -4.3; 947 -5.9; 1042 -6.7; 1146 -6.5; 1261 -5.9; 1387 -5.3; 1526 -4.6; 1678 -3.8; 1846 -2.8; 2031 -2.0; 2234 -1.8; 2457 -1.6; 2703 -1.8; 2973 -2.1; 3270 -2.1; 3597 -1.4; 3957 -1.8; 4353 -4.1; 4788 -3.7; 5267 -1.3; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE MK801 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE MK801 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.96 | 6.1 dB  |
| Peaking | 459 Hz  | 0.22 | -5.3 dB |
| Peaking | 563 Hz  | 0.89 | 7.1 dB  |
| Peaking | 2464 Hz | 0.82 | 6.8 dB  |
| Peaking | 5917 Hz | 3.89 | 5.3 dB  |
| Peaking | 852 Hz  | 5.96 | 2.9 dB  |
| Peaking | 883 Hz  | 2.26 | -1.5 dB |
| Peaking | 3812 Hz | 8.18 | 2.3 dB  |
| Peaking | 4249 Hz | 7.51 | -1.4 dB |
| Peaking | 8397 Hz | 3.52 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/1MORE%20MK801/1MORE%20MK801.png)