# Monster Turbine
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.0; 23 -15.8; 25 -15.6; 28 -15.4; 31 -15.1; 34 -14.9; 37 -14.6; 41 -14.3; 45 -14.0; 49 -13.8; 54 -13.5; 60 -13.2; 66 -13.0; 72 -12.7; 79 -12.5; 87 -12.2; 96 -11.8; 106 -11.5; 116 -11.0; 128 -10.7; 141 -10.3; 155 -10.0; 170 -9.8; 187 -9.3; 206 -8.7; 227 -8.1; 249 -7.6; 274 -7.0; 302 -6.4; 332 -5.8; 365 -5.1; 402 -4.6; 442 -4.1; 486 -3.6; 535 -3.2; 588 -2.7; 647 -2.3; 712 -2.1; 783 -2.0; 861 -2.1; 947 -2.5; 1042 -3.1; 1146 -3.8; 1261 -4.6; 1387 -4.9; 1526 -5.7; 1678 -6.8; 1846 -8.0; 2031 -8.8; 2234 -9.5; 2457 -10.1; 2703 -10.4; 2973 -9.5; 3270 -7.6; 3597 -6.9; 3957 -8.3; 4353 -10.4; 4788 -9.5; 5267 -4.9; 5793 -0.5; 6373 -0.6; 7010 -3.5; 7711 -5.7; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Turbine GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Turbine ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 62 Hz   | 0.23 | -5.6 dB |
| Peaking | 967 Hz  | 0.46 | 7.6 dB  |
| Peaking | 2214 Hz | 0.54 | -7.4 dB |
| Peaking | 6134 Hz | 4.02 | 8.5 dB  |
| Peaking | 17 Hz   | 0.77 | -5.5 dB |
| Peaking | 36 Hz   | 0.62 | -1.2 dB |
| Peaking | 2744 Hz | 2.19 | -3.3 dB |
| Peaking | 3599 Hz | 1.4  | 4.7 dB  |
| Peaking | 4444 Hz | 4.18 | -5.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB  |
| Peaking | 250 Hz   | 1.41 | -1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 2.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 16000 Hz | 1.41 | -0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Turbine/Monster%20Turbine.png)