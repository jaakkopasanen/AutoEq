# Ultrasone PRO 900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.9; 25 -8.7; 28 -9.8; 31 -10.6; 34 -11.3; 37 -11.9; 41 -12.4; 45 -12.8; 49 -12.9; 54 -13.2; 60 -12.1; 66 -10.3; 72 -10.9; 79 -12.6; 87 -13.5; 96 -13.2; 106 -12.8; 116 -13.1; 128 -13.1; 141 -12.2; 155 -12.1; 170 -11.1; 187 -10.6; 206 -8.8; 227 -6.2; 249 -3.0; 274 -0.5; 302 -1.9; 332 -3.8; 365 -4.9; 402 -5.8; 442 -6.0; 486 -6.0; 535 -2.3; 588 -2.3; 647 -4.8; 712 -5.0; 783 -4.8; 861 -5.3; 947 -5.3; 1042 -4.8; 1146 -4.0; 1261 -3.9; 1387 -5.0; 1526 -6.2; 1678 -6.3; 1846 -5.5; 2031 -4.1; 2234 -4.4; 2457 -6.5; 2703 -10.8; 2973 -9.5; 3270 -9.4; 3597 -9.6; 3957 -9.6; 4353 -9.8; 4788 -5.0; 5267 -1.7; 5793 -6.8; 6373 -14.1; 7010 -11.2; 7711 -5.4; 8482 -5.1; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -6.3; 13660 -11.0; 15026 -14.3; 16529 -13.9; 18182 -11.5; 20000 -9.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone PRO 900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 47 Hz    |  0.81 | -7.3 dB  |
| Peaking | 122 Hz   |  1.58 | -7.0 dB  |
| Peaking | 3421 Hz  |  1.87 | -5.1 dB  |
| Peaking | 15334 Hz |  2.21 | -7.4 dB  |
| Peaking | 18322 Hz |  0.79 | -6.1 dB  |
| Peaking | 187 Hz   |  3.51 | -3.1 dB  |
| Peaking | 274 Hz   |  4.03 | 6.5 dB   |
| Peaking | 563 Hz   | 11.22 | 5.2 dB   |
| Peaking | 6228 Hz  |  1.6  | 6.3 dB   |
| Peaking | 6532 Hz  |  4.92 | -15.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB  |
| Peaking | 62 Hz    | 1.41 | -4.9 dB  |
| Peaking | 125 Hz   | 1.41 | -8.8 dB  |
| Peaking | 250 Hz   | 1.41 | 2.8 dB   |
| Peaking | 500 Hz   | 1.41 | 0.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -10.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20PRO%20900/Ultrasone%20PRO%20900.png)