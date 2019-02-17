# Monster Turbine
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -18.6; 23 -18.4; 25 -18.2; 28 -18.0; 31 -17.7; 34 -17.5; 37 -17.2; 41 -16.9; 45 -16.6; 49 -16.4; 54 -16.1; 60 -15.8; 66 -15.6; 72 -15.4; 79 -15.1; 87 -14.8; 96 -14.4; 106 -14.1; 116 -13.6; 128 -13.3; 141 -12.9; 155 -12.7; 170 -12.4; 187 -11.9; 206 -11.3; 227 -10.7; 249 -10.2; 274 -9.6; 302 -9.0; 332 -8.4; 365 -7.7; 402 -7.2; 442 -6.7; 486 -6.2; 535 -5.8; 588 -5.3; 647 -4.9; 712 -4.7; 783 -4.6; 861 -4.7; 947 -5.1; 1042 -5.7; 1146 -6.4; 1261 -7.2; 1387 -7.5; 1526 -8.3; 1678 -9.4; 1846 -10.6; 2031 -11.4; 2234 -12.1; 2457 -12.7; 2703 -13.0; 2973 -12.1; 3270 -10.3; 3597 -9.5; 3957 -10.9; 4353 -13.0; 4788 -12.1; 5267 -7.5; 5793 -2.9; 6373 -0.5; 7010 -2.9; 7711 -5.2; 8482 -6.3; 9330 -8.8; 10263 -5.9; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -7.4; 16529 -5.8; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Turbine GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Turbine ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.2  | -12.7 dB |
| Peaking | 165 Hz   | 0.94 | -3.1 dB  |
| Peaking | 2459 Hz  | 1.54 | -7.5 dB  |
| Peaking | 4543 Hz  | 3.65 | -7.2 dB  |
| Peaking | 6258 Hz  | 4.47 | 7.0 dB   |
| Peaking | 290 Hz   | 3.01 | -0.7 dB  |
| Peaking | 747 Hz   | 1.55 | 1.9 dB   |
| Peaking | 1708 Hz  | 3.74 | -1.1 dB  |
| Peaking | 9285 Hz  | 7.29 | -3.7 dB  |
| Peaking | 15494 Hz | 6.06 | -2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -13.4 dB |
| Peaking | 62 Hz    | 1.41 | -7.0 dB  |
| Peaking | 125 Hz   | 1.41 | -6.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 16000 Hz | 1.41 | -1.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Turbine/Monster%20Turbine.png)