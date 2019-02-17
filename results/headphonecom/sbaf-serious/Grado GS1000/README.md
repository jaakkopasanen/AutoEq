# Grado GS1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.9; 37 -1.8; 41 -2.7; 45 -3.7; 49 -5.2; 54 -7.0; 60 -8.5; 66 -9.9; 72 -11.1; 79 -12.3; 87 -13.3; 96 -14.0; 106 -14.2; 116 -14.1; 128 -13.7; 141 -13.2; 155 -12.7; 170 -11.9; 187 -11.2; 206 -10.5; 227 -9.8; 249 -9.1; 274 -8.9; 302 -8.9; 332 -8.4; 365 -8.0; 402 -7.6; 442 -7.4; 486 -7.3; 535 -7.1; 588 -6.8; 647 -6.4; 712 -6.2; 783 -6.3; 861 -6.3; 947 -6.4; 1042 -6.5; 1146 -6.6; 1261 -6.7; 1387 -7.1; 1526 -7.8; 1678 -7.0; 1846 -7.8; 2031 -7.8; 2234 -7.8; 2457 -7.6; 2703 -7.7; 2973 -7.8; 3270 -7.3; 3597 -10.0; 3957 -11.7; 4353 -9.7; 4788 -12.2; 5267 -13.5; 5793 -14.3; 6373 -16.5; 7010 -16.7; 7711 -16.0; 8482 -14.6; 9330 -13.6; 10263 -11.2; 11289 -7.7; 12418 -6.7; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.6; 20000 -7.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado GS1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.6  | 8.5 dB   |
| Peaking | 98 Hz    | 0.65 | -9.9 dB  |
| Peaking | 789 Hz   | 1.15 | 0.8 dB   |
| Peaking | 1675 Hz  | 1.81 | -0.7 dB  |
| Peaking | 6917 Hz  | 1.21 | -10.7 dB |
| Peaking | 3395 Hz  | 5.12 | 1.9 dB   |
| Peaking | 3759 Hz  | 9.22 | -4.0 dB  |
| Peaking | 9687 Hz  | 2.87 | -3.6 dB  |
| Peaking | 11403 Hz | 1.27 | 2.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 8.6 dB   |
| Peaking | 62 Hz    | 1.41 | -3.7 dB  |
| Peaking | 125 Hz   | 1.41 | -7.9 dB  |
| Peaking | 250 Hz   | 1.41 | -1.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -10.1 dB |
| Peaking | 16000 Hz | 1.41 | 1.5 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20GS1000/Grado%20GS1000.png)