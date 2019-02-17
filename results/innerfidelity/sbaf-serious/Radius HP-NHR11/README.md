# Radius HP-NHR11
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.0; 23 -14.9; 25 -14.9; 28 -14.7; 31 -14.6; 34 -14.4; 37 -14.3; 41 -14.2; 45 -14.0; 49 -13.9; 54 -13.7; 60 -13.6; 66 -13.4; 72 -13.4; 79 -13.3; 87 -13.2; 96 -13.1; 106 -12.8; 116 -12.5; 128 -12.2; 141 -11.8; 155 -11.5; 170 -11.0; 187 -10.5; 206 -10.0; 227 -9.3; 249 -8.8; 274 -8.1; 302 -7.4; 332 -6.8; 365 -6.1; 402 -5.5; 442 -4.8; 486 -4.2; 535 -3.7; 588 -2.9; 647 -2.6; 712 -2.4; 783 -2.1; 861 -2.2; 947 -2.4; 1042 -2.8; 1146 -3.1; 1261 -3.7; 1387 -4.7; 1526 -5.6; 1678 -6.4; 1846 -6.8; 2031 -6.9; 2234 -6.9; 2457 -6.2; 2703 -5.5; 2973 -4.0; 3270 -2.5; 3597 -2.1; 3957 -3.4; 4353 -6.7; 4788 -9.5; 5267 -9.9; 5793 -6.1; 6373 -2.4; 7010 -0.5; 7711 -2.4; 8482 -2.7; 9330 -2.9; 10263 -4.6; 11289 -2.8; 12418 -2.7; 13660 -2.7; 15026 -2.7; 16529 -2.7; 18182 -2.7; 20000 -2.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Radius HP-NHR11 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Radius HP-NHR11 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.18 | -11.9 dB |
| Peaking | 161 Hz   | 0.73 | -4.3 dB  |
| Peaking | 2003 Hz  | 2.22 | -4.6 dB  |
| Peaking | 5098 Hz  | 4.01 | -8.3 dB  |
| Peaking | 6827 Hz  | 4.87 | 3.2 dB   |
| Peaking | 778 Hz   | 1.81 | 1.6 dB   |
| Peaking | 1515 Hz  | 5.66 | -1.2 dB  |
| Peaking | 2625 Hz  | 5.58 | -1.3 dB  |
| Peaking | 3500 Hz  | 5.67 | 2.4 dB   |
| Peaking | 10244 Hz | 7.72 | -2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -12.6 dB |
| Peaking | 62 Hz    | 1.41 | -7.5 dB  |
| Peaking | 125 Hz   | 1.41 | -7.8 dB  |
| Peaking | 250 Hz   | 1.41 | -4.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Radius%20HP-NHR11/Radius%20HP-NHR11.png)