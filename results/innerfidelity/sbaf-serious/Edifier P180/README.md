# Edifier P180
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.4; 54 -3.0; 60 -4.9; 66 -6.6; 72 -8.1; 79 -9.7; 87 -11.3; 96 -12.6; 106 -13.3; 116 -13.6; 128 -13.4; 141 -13.2; 155 -12.8; 170 -12.2; 187 -11.7; 206 -11.3; 227 -10.6; 249 -10.3; 274 -10.0; 302 -9.6; 332 -9.4; 365 -9.3; 402 -8.5; 442 -8.2; 486 -7.5; 535 -7.2; 588 -6.5; 647 -6.5; 712 -6.4; 783 -6.2; 861 -6.3; 947 -6.4; 1042 -6.6; 1146 -7.4; 1261 -8.9; 1387 -11.4; 1526 -14.6; 1678 -17.6; 1846 -20.1; 2031 -21.6; 2234 -21.6; 2457 -19.6; 2703 -17.3; 2973 -13.8; 3270 -10.7; 3597 -8.9; 3957 -9.3; 4353 -11.4; 4788 -12.9; 5267 -13.9; 5793 -16.2; 6373 -17.1; 7010 -15.8; 7711 -15.6; 8482 -15.2; 9330 -12.9; 10263 -9.2; 11289 -6.5; 12418 -6.5; 13660 -6.7; 15026 -8.6; 16529 -7.0; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Edifier P180 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Edifier P180 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 40 Hz    | 0.55 | 9.5 dB   |
| Peaking | 109 Hz   | 0.68 | -10.7 dB |
| Peaking | 2103 Hz  | 2.13 | -16.3 dB |
| Peaking | 6859 Hz  | 1.46 | -10.4 dB |
| Peaking | 15352 Hz | 6.46 | -1.7 dB  |
| Peaking | 1066 Hz  | 1.15 | 2.7 dB   |
| Peaking | 1602 Hz  | 4.48 | -3.5 dB  |
| Peaking | 3305 Hz  | 1.34 | -3.0 dB  |
| Peaking | 3565 Hz  | 3.67 | 5.8 dB   |
| Peaking | 8819 Hz  | 1.58 | 0.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 8.5 dB   |
| Peaking | 62 Hz    | 1.41 | 0.6 dB   |
| Peaking | 125 Hz   | 1.41 | -8.1 dB  |
| Peaking | 250 Hz   | 1.41 | -2.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -16.3 dB |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 8000 Hz  | 1.41 | -9.4 dB  |
| Peaking | 16000 Hz | 1.41 | 0.4 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Edifier%20P180/Edifier%20P180.png)