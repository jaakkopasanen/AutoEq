# Ultrasone PRO 900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.3; 25 -2.0; 28 -3.0; 31 -3.9; 34 -4.6; 37 -5.2; 41 -5.7; 45 -5.7; 49 -5.6; 54 -5.9; 60 -6.4; 66 -7.0; 72 -7.9; 79 -8.5; 87 -9.1; 96 -9.6; 106 -10.0; 116 -10.3; 128 -10.1; 141 -10.1; 155 -9.9; 170 -9.2; 187 -8.8; 206 -7.3; 227 -5.4; 249 -3.2; 274 -0.5; 302 -1.6; 332 -4.3; 365 -5.5; 402 -6.1; 442 -5.9; 486 -4.7; 535 -1.9; 588 -3.3; 647 -4.4; 712 -4.2; 783 -4.0; 861 -3.9; 947 -3.4; 1042 -2.8; 1146 -1.9; 1261 -1.8; 1387 -3.2; 1526 -4.1; 1678 -5.0; 1846 -5.0; 2031 -2.9; 2234 -1.7; 2457 -5.6; 2703 -7.7; 2973 -8.3; 3270 -8.6; 3597 -9.3; 3957 -10.5; 4353 -11.4; 4788 -11.4; 5267 -10.0; 5793 -11.5; 6373 -10.5; 7010 -7.9; 7711 -5.4; 8482 -3.3; 9330 -3.1; 10263 -3.1; 11289 -3.1; 12418 -7.5; 13660 -12.3; 15026 -15.0; 16529 -13.7; 18182 -11.0; 20000 -11.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone PRO 900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 96 Hz    | 1.11 | -6.3 dB  |
| Peaking | 158 Hz   | 2.47 | -4.6 dB  |
| Peaking | 416 Hz   | 5.94 | -3.0 dB  |
| Peaking | 4548 Hz  | 1.34 | -8.7 dB  |
| Peaking | 16461 Hz | 1.01 | -12.3 dB |
| Peaking | 21 Hz    | 3.21 | 2.3 dB   |
| Peaking | 279 Hz   | 7.68 | 4.6 dB   |
| Peaking | 6393 Hz  | 3.91 | -4.4 dB  |
| Peaking | 10689 Hz | 1    | 4.7 dB   |
| Peaking | 13867 Hz | 2.38 | -5.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.3 dB   |
| Peaking | 62 Hz    | 1.41 | -2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -8.3 dB  |
| Peaking | 250 Hz   | 1.41 | 1.0 dB   |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -9.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB   |
| Peaking | 16000 Hz | 1.41 | -14.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20PRO%20900/Ultrasone%20PRO%20900.png)