# Grado SR325
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.2; 66 -2.0; 72 -2.7; 79 -3.3; 87 -3.8; 96 -4.3; 106 -4.5; 116 -4.4; 128 -4.4; 141 -4.5; 155 -4.5; 170 -4.4; 187 -4.3; 206 -4.3; 227 -4.3; 249 -4.1; 274 -4.0; 302 -3.9; 332 -3.7; 365 -3.6; 402 -3.4; 442 -3.3; 486 -3.5; 535 -3.3; 588 -3.3; 647 -3.2; 712 -3.2; 783 -3.3; 861 -3.4; 947 -3.6; 1042 -4.0; 1146 -4.3; 1261 -4.8; 1387 -5.7; 1526 -6.9; 1678 -7.9; 1846 -9.7; 2031 -12.1; 2234 -11.3; 2457 -9.8; 2703 -8.2; 2973 -6.7; 3270 -5.1; 3597 -4.5; 3957 -7.4; 4353 -15.7; 4788 -14.8; 5267 -10.2; 5793 -8.0; 6373 -9.0; 7010 -10.1; 7711 -10.9; 8482 -13.6; 9330 -16.2; 10263 -15.0; 11289 -12.1; 12418 -8.0; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR325 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR325 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.52 | 6.5 dB   |
| Peaking | 607 Hz   | 0.48 | 3.5 dB   |
| Peaking | 2074 Hz  | 2.8  | -6.6 dB  |
| Peaking | 9287 Hz  | 1.41 | -9.0 dB  |
| Peaking | 22050 Hz | 2.18 | -7.6 dB  |
| Peaking | 3686 Hz  | 3.84 | 5.6 dB   |
| Peaking | 4511 Hz  | 4.21 | -12.5 dB |
| Peaking | 6177 Hz  | 1.22 | 2.4 dB   |
| Peaking | 10579 Hz | 2.11 | -2.6 dB  |
| Peaking | 13063 Hz | 1.68 | 2.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | 0.6 dB  |
| Peaking | 250 Hz   | 1.41 | 1.8 dB  |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB |
| Peaking | 8000 Hz  | 1.41 | -7.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20SR325/Grado%20SR325.png)