# Street by 50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.9; 25 -3.7; 28 -4.8; 31 -5.7; 34 -6.6; 37 -7.3; 41 -8.2; 45 -9.0; 49 -9.7; 54 -10.5; 60 -11.2; 66 -11.8; 72 -12.3; 79 -12.7; 87 -13.1; 96 -13.5; 106 -13.6; 116 -13.6; 128 -13.7; 141 -13.6; 155 -13.4; 170 -13.0; 187 -12.6; 206 -11.9; 227 -11.5; 249 -12.8; 274 -12.2; 302 -11.4; 332 -10.8; 365 -10.0; 402 -9.6; 442 -9.2; 486 -8.8; 535 -7.2; 588 -3.3; 647 -1.4; 712 -0.5; 783 -0.6; 861 -1.8; 947 -2.6; 1042 -3.0; 1146 -3.6; 1261 -3.7; 1387 -2.4; 1526 -3.1; 1678 -5.0; 1846 -6.7; 2031 -7.9; 2234 -8.7; 2457 -8.6; 2703 -8.2; 2973 -7.2; 3270 -6.1; 3597 -4.4; 3957 -2.3; 4353 -0.6; 4788 -0.5; 5267 -0.5; 5793 -3.7; 6373 -1.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.9; 10263 -7.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Street by 50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Street by 50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 19 Hz   | 0.49 | 7.5 dB   |
| Peaking | 435 Hz  | 0.07 | -10.9 dB |
| Peaking | 444 Hz  | 1.16 | -4.7 dB  |
| Peaking | 751 Hz  | 0.51 | 18.1 dB  |
| Peaking | 4904 Hz | 1.33 | 10.3 dB  |
| Peaking | 676 Hz  | 3.81 | 2.3 dB   |
| Peaking | 925 Hz  | 1.03 | -1.6 dB  |
| Peaking | 1469 Hz | 3.49 | 4.0 dB   |
| Peaking | 2346 Hz | 2.22 | -1.5 dB  |
| Peaking | 3925 Hz | 4.42 | 1.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.6 dB  |
| Peaking | 62 Hz    | 1.41 | -5.0 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -5.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Street%20by%2050/Street%20by%2050.png)