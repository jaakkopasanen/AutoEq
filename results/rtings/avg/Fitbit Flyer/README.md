# Fitbit Flyer
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.2; 45 -4.8; 49 -8.4; 54 -11.8; 60 -14.5; 66 -15.9; 72 -16.0; 79 -15.1; 87 -14.2; 96 -13.2; 106 -12.4; 116 -11.9; 128 -11.1; 141 -10.0; 155 -9.2; 170 -9.2; 187 -9.2; 206 -9.1; 227 -8.9; 249 -8.7; 274 -8.7; 302 -8.7; 332 -8.9; 365 -9.2; 402 -8.9; 442 -8.2; 486 -7.5; 535 -6.9; 588 -6.3; 647 -5.7; 712 -5.2; 783 -4.6; 861 -5.2; 947 -6.0; 1042 -6.9; 1146 -7.9; 1261 -8.3; 1387 -8.4; 1526 -8.4; 1678 -8.6; 1846 -8.9; 2031 -9.2; 2234 -8.9; 2457 -8.5; 2703 -8.5; 2973 -8.1; 3270 -6.8; 3597 -5.5; 3957 -5.2; 4353 -5.8; 4788 -5.3; 5267 -5.1; 5793 -4.2; 6373 -2.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.4; 16529 -11.5; 18182 -10.3; 20000 -9.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fitbit Flyer GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fitbit Flyer ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.7  | 15.1 dB  |
| Peaking | 65 Hz    | 0.85 | -18.1 dB |
| Peaking | 359 Hz   | 3.04 | -1.9 dB  |
| Peaking | 6413 Hz  | 4.1  | 4.4 dB   |
| Peaking | 17566 Hz | 1.33 | -5.3 dB  |
| Peaking | 50 Hz    | 5.31 | -0.8 dB  |
| Peaking | 784 Hz   | 2.25 | 3.1 dB   |
| Peaking | 2287 Hz  | 0.57 | -3.2 dB  |
| Peaking | 3942 Hz  | 1.58 | 3.2 dB   |
| Peaking | 13849 Hz | 3.23 | 1.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 11.3 dB  |
| Peaking | 62 Hz    | 1.41 | -11.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB  |
| Peaking | 250 Hz   | 1.41 | -1.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 16000 Hz | 1.41 | -3.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Fitbit%20Flyer/Fitbit%20Flyer.png)