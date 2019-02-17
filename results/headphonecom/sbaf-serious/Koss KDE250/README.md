# Koss KDE250
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.9; 170 -1.6; 187 -2.2; 206 -2.7; 227 -3.3; 249 -4.0; 274 -4.5; 302 -4.8; 332 -5.1; 365 -5.3; 402 -5.1; 442 -5.3; 486 -5.0; 535 -5.0; 588 -5.0; 647 -5.0; 712 -5.1; 783 -5.2; 861 -5.5; 947 -6.0; 1042 -6.7; 1146 -7.3; 1261 -8.3; 1387 -9.9; 1526 -12.1; 1678 -13.9; 1846 -15.3; 2031 -17.6; 2234 -20.9; 2457 -22.6; 2703 -20.7; 2973 -18.8; 3270 -13.6; 3597 -7.9; 3957 -4.8; 4353 -0.9; 4788 -1.2; 5267 -3.8; 5793 -3.8; 6373 -5.6; 7010 -10.3; 7711 -14.3; 8482 -14.8; 9330 -12.8; 10263 -11.5; 11289 -12.0; 12418 -12.0; 13660 -8.2; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss KDE250 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss KDE250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 53 Hz    | 0.23 | 6.5 dB   |
| Peaking | 981 Hz   | 0.97 | 4.7 dB   |
| Peaking | 2562 Hz  | 1.03 | -23.2 dB |
| Peaking | 4571 Hz  | 1.05 | 17.4 dB  |
| Peaking | 8575 Hz  | 1.14 | -10.2 dB |
| Peaking | 24 Hz    | 2.1  | 0.8 dB   |
| Peaking | 9916 Hz  | 5.14 | 2.4 dB   |
| Peaking | 12551 Hz | 2.17 | -3.7 dB  |
| Peaking | 14179 Hz | 3.42 | 2.2 dB   |
| Peaking | 15418 Hz | 1.27 | 1.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB   |
| Peaking | 62 Hz    | 1.41 | 4.2 dB   |
| Peaking | 125 Hz   | 1.41 | 5.5 dB   |
| Peaking | 250 Hz   | 1.41 | 1.4 dB   |
| Peaking | 500 Hz   | 1.41 | 0.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -16.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -6.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20KDE250/Koss%20KDE250.png)