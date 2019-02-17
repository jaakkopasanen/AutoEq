# AKG K1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.9; 66 -2.7; 72 -4.4; 79 -5.9; 87 -7.1; 96 -7.9; 106 -8.2; 116 -8.3; 128 -8.4; 141 -7.7; 155 -7.6; 170 -7.2; 187 -7.1; 206 -7.0; 227 -6.7; 249 -6.6; 274 -6.3; 302 -6.2; 332 -6.1; 365 -6.0; 402 -6.0; 442 -5.7; 486 -5.8; 535 -5.8; 588 -5.6; 647 -5.6; 712 -5.8; 783 -5.6; 861 -5.9; 947 -6.2; 1042 -6.5; 1146 -7.2; 1261 -8.6; 1387 -10.3; 1526 -11.1; 1678 -11.3; 1846 -13.3; 2031 -13.1; 2234 -12.2; 2457 -9.4; 2703 -6.4; 2973 -4.1; 3270 -3.8; 3597 -5.3; 3957 -8.3; 4353 -9.2; 4788 -9.2; 5267 -9.3; 5793 -10.9; 6373 -11.7; 7010 -10.4; 7711 -10.6; 8482 -11.2; 9330 -10.4; 10263 -7.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.8; 20000 -8.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 72 Hz    | 0.27 | 17.7 dB  |
| Peaking | 103 Hz   | 0.49 | -18.4 dB |
| Peaking | 1948 Hz  | 1.81 | -7.4 dB  |
| Peaking | 3113 Hz  | 3.25 | 5.9 dB   |
| Peaking | 6702 Hz  | 1.09 | -4.9 dB  |
| Peaking | 82 Hz    | 6.24 | -0.7 dB  |
| Peaking | 912 Hz   | 1.8  | 0.9 dB   |
| Peaking | 1404 Hz  | 7.06 | -1.6 dB  |
| Peaking | 9062 Hz  | 3.82 | -3.1 dB  |
| Peaking | 10574 Hz | 1.55 | 2.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 3.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.9 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K1000/AKG%20K1000.png)