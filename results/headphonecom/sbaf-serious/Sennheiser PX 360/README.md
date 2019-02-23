# Sennheiser PX 360
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.6; 66 -1.2; 72 -1.7; 79 -2.3; 87 -2.9; 96 -3.5; 106 -3.6; 116 -2.8; 128 -1.6; 141 -3.0; 155 -3.4; 170 -1.5; 187 -1.6; 206 -2.8; 227 -3.8; 249 -3.8; 274 -5.4; 302 -7.5; 332 -8.2; 365 -8.3; 402 -9.2; 442 -9.4; 486 -8.8; 535 -8.0; 588 -7.4; 647 -7.3; 712 -7.1; 783 -7.1; 861 -7.2; 947 -7.5; 1042 -8.0; 1146 -9.1; 1261 -10.6; 1387 -13.0; 1526 -15.5; 1678 -17.1; 1846 -17.6; 2031 -16.5; 2234 -14.0; 2457 -10.9; 2703 -8.5; 2973 -6.6; 3270 -4.3; 3597 -1.6; 3957 -1.0; 4353 -4.8; 4788 -6.2; 5267 -4.5; 5793 -0.9; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.6; 10263 -10.7; 11289 -10.3; 12418 -7.1; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PX 360 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 360 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 36 Hz    | 0.43 | 6.5 dB   |
| Peaking | 182 Hz   | 3.09 | 4.1 dB   |
| Peaking | 1814 Hz  | 1.76 | -12.0 dB |
| Peaking | 3673 Hz  | 3.5  | 7.4 dB   |
| Peaking | 6133 Hz  | 5.21 | 6.7 dB   |
| Peaking | 127 Hz   | 7.82 | 2.5 dB   |
| Peaking | 249 Hz   | 3.13 | 3.1 dB   |
| Peaking | 392 Hz   | 0.91 | -3.5 dB  |
| Peaking | 777 Hz   | 1.27 | 1.9 dB   |
| Peaking | 10512 Hz | 3.7  | -5.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 3.6 dB   |
| Peaking | 125 Hz   | 1.41 | 3.2 dB   |
| Peaking | 250 Hz   | 1.41 | 1.9 dB   |
| Peaking | 500 Hz   | 1.41 | -2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -12.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PX%20360/Sennheiser%20PX%20360.png)