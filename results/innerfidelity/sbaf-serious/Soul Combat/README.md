# Soul Combat
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -2.7; 25 -3.9; 28 -5.4; 31 -6.7; 34 -7.7; 37 -8.6; 41 -9.5; 45 -10.2; 49 -10.6; 54 -11.1; 60 -11.5; 66 -11.8; 72 -12.1; 79 -12.4; 87 -12.8; 96 -13.0; 106 -13.3; 116 -13.6; 128 -13.9; 141 -14.4; 155 -14.9; 170 -15.0; 187 -15.2; 206 -15.5; 227 -16.0; 249 -16.4; 274 -16.9; 302 -17.4; 332 -17.8; 365 -18.1; 402 -18.4; 442 -19.1; 486 -19.2; 535 -18.2; 588 -15.7; 647 -12.7; 712 -9.5; 783 -6.5; 861 -4.9; 947 -5.4; 1042 -7.5; 1146 -9.4; 1261 -9.8; 1387 -8.8; 1526 -8.1; 1678 -9.4; 1846 -10.5; 2031 -9.2; 2234 -6.7; 2457 -3.7; 2703 -1.9; 2973 -0.9; 3270 -1.1; 3597 -1.0; 3957 -0.7; 4353 -1.9; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -9.6; 10263 -10.7; 11289 -7.3; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Soul Combat GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Soul Combat ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 2.55 | 6.4 dB  |
| Peaking | 163 Hz  | 0.38 | -8.1 dB |
| Peaking | 442 Hz  | 1.71 | -9.0 dB |
| Peaking | 3255 Hz | 2.65 | 5.9 dB  |
| Peaking | 5369 Hz | 2.45 | 6.4 dB  |
| Peaking | 576 Hz  | 3.6  | -3.3 dB |
| Peaking | 870 Hz  | 2.05 | 5.8 dB  |
| Peaking | 1188 Hz | 3.2  | -3.8 dB |
| Peaking | 1857 Hz | 5.28 | -4.5 dB |
| Peaking | 9965 Hz | 4.67 | -5.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB   |
| Peaking | 62 Hz    | 1.41 | -4.8 dB  |
| Peaking | 125 Hz   | 1.41 | -5.1 dB  |
| Peaking | 250 Hz   | 1.41 | -7.9 dB  |
| Peaking | 500 Hz   | 1.41 | -11.3 dB |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Soul%20Combat/Soul%20Combat.png)