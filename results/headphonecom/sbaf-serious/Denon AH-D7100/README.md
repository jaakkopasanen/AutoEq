# Denon AH-D7100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.7; 23 -14.8; 25 -14.7; 28 -14.7; 31 -14.6; 34 -14.4; 37 -14.3; 41 -14.0; 45 -13.7; 49 -13.5; 54 -13.1; 60 -12.1; 66 -12.0; 72 -12.6; 79 -13.1; 87 -14.0; 96 -15.2; 106 -15.4; 116 -15.4; 128 -15.3; 141 -15.0; 155 -14.3; 170 -12.8; 187 -12.6; 206 -10.7; 227 -8.2; 249 -5.2; 274 -2.2; 302 -0.6; 332 -0.5; 365 -1.0; 402 -1.8; 442 -2.5; 486 -3.4; 535 -4.3; 588 -5.1; 647 -6.1; 712 -6.6; 783 -6.9; 861 -7.2; 947 -7.7; 1042 -8.0; 1146 -8.4; 1261 -8.8; 1387 -9.7; 1526 -10.7; 1678 -11.4; 1846 -11.2; 2031 -10.5; 2234 -9.1; 2457 -6.8; 2703 -5.4; 2973 -5.2; 3270 -4.4; 3597 -1.0; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -3.1; 6373 -4.4; 7010 -4.0; 7711 -6.2; 8482 -9.8; 9330 -12.8; 10263 -7.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -9.0; 18182 -15.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D7100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 2.11 | -4.4 dB  |
| Peaking | 245 Hz   | 0.19 | -20.6 dB |
| Peaking | 344 Hz   | 0.59 | 26.9 dB  |
| Peaking | 4333 Hz  | 1.81 | 8.5 dB   |
| Peaking | 18217 Hz | 2.03 | -9.8 dB  |
| Peaking | 67 Hz    | 2.62 | 2.9 dB   |
| Peaking | 135 Hz   | 1.29 | -2.3 dB  |
| Peaking | 1784 Hz  | 2.35 | -4.3 dB  |
| Peaking | 2421 Hz  | 0.08 | 1.1 dB   |
| Peaking | 9106 Hz  | 5.48 | -8.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -9.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -10.8 dB |
| Peaking | 250 Hz   | 1.41 | 3.4 dB   |
| Peaking | 500 Hz   | 1.41 | 4.4 dB   |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB   |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -2.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D7100/Denon%20AH-D7100.png)