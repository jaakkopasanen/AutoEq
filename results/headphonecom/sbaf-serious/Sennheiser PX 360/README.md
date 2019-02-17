# Sennheiser PX 360
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -1.0; 87 -1.6; 96 -2.2; 106 -2.3; 116 -1.5; 128 -0.5; 141 -1.7; 155 -2.1; 170 -0.7; 187 -0.6; 206 -1.5; 227 -2.5; 249 -2.5; 274 -4.1; 302 -6.2; 332 -6.9; 365 -7.0; 402 -7.9; 442 -8.1; 486 -7.5; 535 -6.7; 588 -6.1; 647 -6.0; 712 -5.8; 783 -5.7; 861 -5.9; 947 -6.2; 1042 -6.7; 1146 -7.8; 1261 -9.3; 1387 -11.7; 1526 -14.1; 1678 -15.8; 1846 -16.3; 2031 -15.2; 2234 -12.7; 2457 -9.6; 2703 -7.2; 2973 -5.3; 3270 -3.0; 3597 -0.7; 3957 -0.5; 4353 -3.5; 4788 -4.9; 5267 -3.2; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.4; 10263 -9.4; 11289 -9.0; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PX 360 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 360 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.45 | 5.3 dB   |
| Peaking | 77 Hz    | 0.69 | 3.6 dB   |
| Peaking | 187 Hz   | 2.07 | 4.4 dB   |
| Peaking | 1870 Hz  | 1.93 | -12.2 dB |
| Peaking | 3847 Hz  | 1.09 | 6.3 dB   |
| Peaking | 417 Hz   | 2.95 | -2.4 dB  |
| Peaking | 835 Hz   | 2.1  | 1.8 dB   |
| Peaking | 4809 Hz  | 6.32 | -3.6 dB  |
| Peaking | 6050 Hz  | 4.24 | 4.4 dB   |
| Peaking | 10428 Hz | 2.94 | -3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB   |
| Peaking | 62 Hz    | 1.41 | 4.1 dB   |
| Peaking | 125 Hz   | 1.41 | 4.3 dB   |
| Peaking | 250 Hz   | 1.41 | 2.7 dB   |
| Peaking | 500 Hz   | 1.41 | -1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PX%20360/Sennheiser%20PX%20360.png)