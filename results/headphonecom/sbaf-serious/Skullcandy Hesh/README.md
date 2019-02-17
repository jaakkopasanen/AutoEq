# Skullcandy Hesh
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.7; 72 -1.7; 79 -3.6; 87 -5.2; 96 -6.2; 106 -6.7; 116 -6.9; 128 -6.9; 141 -7.1; 155 -7.0; 170 -6.9; 187 -7.1; 206 -7.1; 227 -6.8; 249 -6.6; 274 -6.4; 302 -6.2; 332 -6.2; 365 -6.3; 402 -6.4; 442 -6.6; 486 -6.9; 535 -7.1; 588 -7.5; 647 -7.4; 712 -6.8; 783 -6.0; 861 -6.2; 947 -5.9; 1042 -7.5; 1146 -9.7; 1261 -11.8; 1387 -11.4; 1526 -11.9; 1678 -9.2; 1846 -6.4; 2031 -3.3; 2234 -0.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Hesh GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Hesh ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 51 Hz   | 0.38 | 8.4 dB   |
| Peaking | 115 Hz  | 0.77 | -6.1 dB  |
| Peaking | 584 Hz  | 3.39 | -1.6 dB  |
| Peaking | 1450 Hz | 1.82 | -11.4 dB |
| Peaking | 2677 Hz | 0.54 | 8.3 dB   |
| Peaking | 69 Hz   | 6.55 | 1.2 dB   |
| Peaking | 946 Hz  | 7.95 | 1.2 dB   |
| Peaking | 3255 Hz | 4.19 | -0.9 dB  |
| Peaking | 6204 Hz | 2    | 5.6 dB   |
| Peaking | 7515 Hz | 1.39 | -4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 4.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Skullcandy%20Hesh/Skullcandy%20Hesh.png)