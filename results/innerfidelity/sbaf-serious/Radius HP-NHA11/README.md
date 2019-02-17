# Radius HP-NHA11
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.0; 23 -15.9; 25 -15.7; 28 -15.5; 31 -15.3; 34 -15.2; 37 -15.0; 41 -14.8; 45 -14.6; 49 -14.4; 54 -14.2; 60 -14.0; 66 -13.8; 72 -13.7; 79 -13.5; 87 -13.4; 96 -13.2; 106 -12.9; 116 -12.6; 128 -12.3; 141 -11.9; 155 -11.5; 170 -11.0; 187 -10.5; 206 -10.0; 227 -9.3; 249 -8.7; 274 -8.1; 302 -7.5; 332 -6.8; 365 -6.2; 402 -5.7; 442 -5.0; 486 -4.4; 535 -4.0; 588 -3.3; 647 -2.9; 712 -2.6; 783 -2.2; 861 -2.4; 947 -2.7; 1042 -3.1; 1146 -3.5; 1261 -4.0; 1387 -5.0; 1526 -6.1; 1678 -7.0; 1846 -7.5; 2031 -7.8; 2234 -7.9; 2457 -7.0; 2703 -6.5; 2973 -4.7; 3270 -3.2; 3597 -2.8; 3957 -4.6; 4353 -8.6; 4788 -11.6; 5267 -8.6; 5793 -3.6; 6373 -0.7; 7010 -0.5; 7711 -2.6; 8482 -3.4; 9330 -3.8; 10263 -2.9; 11289 -2.9; 12418 -2.9; 13660 -2.9; 15026 -2.9; 16529 -2.9; 18182 -2.9; 20000 -2.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Radius HP-NHA11 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Radius HP-NHA11 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 0.19 | -12.6 dB |
| Peaking | 161 Hz  | 0.73 | -4.1 dB  |
| Peaking | 2038 Hz | 2.11 | -5.3 dB  |
| Peaking | 4845 Hz | 4.69 | -9.5 dB  |
| Peaking | 6559 Hz | 4.53 | 4.1 dB   |
| Peaking | 794 Hz  | 2.11 | 1.7 dB   |
| Peaking | 1533 Hz | 5.67 | -1.2 dB  |
| Peaking | 2680 Hz | 6.89 | -1.4 dB  |
| Peaking | 3489 Hz | 6.24 | 2.2 dB   |
| Peaking | 9050 Hz | 6.49 | -1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -13.3 dB |
| Peaking | 62 Hz    | 1.41 | -7.5 dB  |
| Peaking | 125 Hz   | 1.41 | -7.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 16000 Hz | 1.41 | -0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Radius%20HP-NHA11/Radius%20HP-NHA11.png)