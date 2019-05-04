# Fitbit Flyer
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -8.3; 25 -8.9; 28 -8.7; 31 -7.3; 34 -5.3; 37 -3.9; 41 -4.6; 45 -8.4; 49 -12.5; 54 -15.7; 60 -17.5; 66 -18.4; 72 -18.4; 79 -17.4; 87 -16.0; 96 -14.5; 106 -13.2; 116 -12.4; 128 -11.3; 141 -9.6; 155 -8.5; 170 -8.1; 187 -7.8; 206 -7.6; 227 -7.2; 249 -7.0; 274 -7.0; 302 -7.1; 332 -7.2; 365 -7.5; 402 -7.2; 442 -6.5; 486 -5.9; 535 -5.3; 588 -4.7; 647 -4.1; 712 -3.6; 783 -3.1; 861 -3.7; 947 -4.5; 1042 -5.4; 1146 -6.4; 1261 -6.8; 1387 -6.9; 1526 -6.9; 1678 -7.2; 1846 -7.6; 2031 -8.0; 2234 -8.1; 2457 -7.8; 2703 -7.4; 2973 -6.5; 3270 -5.0; 3597 -3.5; 3957 -3.3; 4353 -3.7; 4788 -4.0; 5267 -3.8; 5793 -2.5; 6373 -0.5; 7010 -3.3; 7711 -5.6; 8482 -5.8; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -6.1; 16529 -9.7; 18182 -8.4; 20000 -7.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fitbit Flyer GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fitbit Flyer ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 74 Hz    | 1.25 | -12.9 dB |
| Peaking | 762 Hz   | 3.69 | 3.2 dB   |
| Peaking | 3989 Hz  | 4.7  | 2.7 dB   |
| Peaking | 6283 Hz  | 4.55 | 5.5 dB   |
| Peaking | 17282 Hz | 1.68 | -4.1 dB  |
| Peaking | 40 Hz    | 4.3  | 6.7 dB   |
| Peaking | 53 Hz    | 4.43 | -2.6 dB  |
| Peaking | 62 Hz    | 4.68 | -1.1 dB  |
| Peaking | 368 Hz   | 4.27 | -1.3 dB  |
| Peaking | 2098 Hz  | 2.02 | -2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB   |
| Peaking | 62 Hz    | 1.41 | -13.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB  |
| Peaking | 250 Hz   | 1.41 | -0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 16000 Hz | 1.41 | -2.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Fitbit%20Flyer/Fitbit%20Flyer.png)