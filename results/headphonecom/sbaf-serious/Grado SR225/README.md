# Grado SR225
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.6; 66 -1.5; 72 -2.4; 79 -3.1; 87 -3.7; 96 -4.2; 106 -4.6; 116 -4.9; 128 -4.9; 141 -4.9; 155 -4.9; 170 -4.9; 187 -4.8; 206 -4.8; 227 -4.6; 249 -4.5; 274 -4.5; 302 -4.4; 332 -3.9; 365 -3.5; 402 -3.4; 442 -3.6; 486 -3.4; 535 -3.3; 588 -3.3; 647 -3.1; 712 -3.1; 783 -3.2; 861 -3.4; 947 -3.6; 1042 -4.0; 1146 -4.3; 1261 -4.8; 1387 -5.7; 1526 -6.9; 1678 -7.9; 1846 -8.6; 2031 -9.1; 2234 -9.3; 2457 -8.6; 2703 -8.4; 2973 -8.1; 3270 -8.0; 3597 -9.1; 3957 -13.1; 4353 -14.7; 4788 -12.1; 5267 -11.2; 5793 -11.9; 6373 -9.6; 7010 -6.2; 7711 -6.2; 8482 -9.6; 9330 -15.1; 10263 -15.1; 11289 -10.1; 12418 -7.0; 13660 -7.4; 15026 -7.3; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 35 Hz   |  0.57 | 6.7 dB   |
| Peaking | 949 Hz  |  0.34 | 3.9 dB   |
| Peaking | 1944 Hz |  1.43 | -5.1 dB  |
| Peaking | 4435 Hz |  2.3  | -8.2 dB  |
| Peaking | 9881 Hz |  4.03 | -10.3 dB |
| Peaking | 59 Hz   |  5.51 | 1.2 dB   |
| Peaking | 3423 Hz | 10.08 | 1.3 dB   |
| Peaking | 5908 Hz |  6.25 | -2.8 dB  |
| Peaking | 7524 Hz |  4.72 | 3.2 dB   |
| Peaking | 9020 Hz |  9.29 | -2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | -4.7 dB |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20SR225/Grado%20SR225.png)