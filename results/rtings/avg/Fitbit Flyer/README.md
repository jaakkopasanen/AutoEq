# Fitbit Flyer
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.0; 45 -4.0; 49 -7.7; 54 -11.0; 60 -13.8; 66 -15.1; 72 -15.2; 79 -14.4; 87 -13.4; 96 -12.4; 106 -11.6; 116 -11.1; 128 -10.3; 141 -9.2; 155 -8.5; 170 -8.4; 187 -8.4; 206 -8.3; 227 -8.1; 249 -8.0; 274 -7.9; 302 -8.0; 332 -8.1; 365 -8.4; 402 -8.1; 442 -7.4; 486 -6.7; 535 -6.1; 588 -5.5; 647 -4.9; 712 -4.4; 783 -3.8; 861 -4.5; 947 -5.2; 1042 -6.1; 1146 -7.1; 1261 -7.5; 1387 -7.6; 1526 -7.6; 1678 -7.8; 1846 -8.1; 2031 -8.4; 2234 -8.1; 2457 -7.7; 2703 -7.7; 2973 -7.3; 3270 -6.0; 3597 -4.7; 3957 -4.4; 4353 -5.0; 4788 -4.5; 5267 -4.3; 5793 -3.5; 6373 -1.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.0; 16529 -10.7; 18182 -9.5; 20000 -8.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fitbit Flyer GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fitbit Flyer ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 40 Hz    | 0.54 | 17.1 dB  |
| Peaking | 64 Hz    | 0.8  | -20.9 dB |
| Peaking | 753 Hz   | 3.49 | 3.2 dB   |
| Peaking | 6159 Hz  | 2.73 | 4.3 dB   |
| Peaking | 17432 Hz | 1.48 | -4.4 dB  |
| Peaking | 371 Hz   | 4.81 | -1.3 dB  |
| Peaking | 1868 Hz  | 1.76 | -1.4 dB  |
| Peaking | 3156 Hz  | 1.25 | -1.8 dB  |
| Peaking | 3746 Hz  | 2.65 | 3.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 11.1 dB  |
| Peaking | 62 Hz    | 1.41 | -10.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB  |
| Peaking | 250 Hz   | 1.41 | -1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 16000 Hz | 1.41 | -3.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Fitbit%20Flyer/Fitbit%20Flyer.png)