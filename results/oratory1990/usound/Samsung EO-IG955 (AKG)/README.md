# Samsung EO-IG955 (AKG)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -4.8; 25 -5.1; 28 -5.4; 31 -5.7; 34 -5.9; 37 -6.1; 41 -6.4; 45 -6.6; 49 -6.8; 54 -7.0; 60 -7.2; 66 -7.4; 72 -7.6; 79 -7.8; 87 -8.0; 96 -8.2; 106 -8.3; 116 -8.4; 128 -8.4; 141 -8.3; 155 -8.1; 170 -7.8; 187 -7.0; 206 -7.2; 227 -7.1; 249 -6.6; 274 -6.1; 302 -5.6; 332 -5.1; 365 -4.6; 402 -4.1; 442 -3.5; 486 -3.0; 535 -2.5; 588 -2.1; 647 -1.6; 712 -1.1; 783 -0.7; 861 -0.5; 947 -0.5; 1042 -0.9; 1146 -1.3; 1261 -1.8; 1387 -2.1; 1526 -2.3; 1678 -2.3; 1846 -2.3; 2031 -2.4; 2234 -2.8; 2457 -3.2; 2703 -3.6; 2973 -4.2; 3270 -4.8; 3597 -4.8; 3957 -4.3; 4353 -3.5; 4788 -3.9; 5267 -4.9; 5793 -3.4; 6373 -1.0; 7010 -2.0; 7711 -7.0; 8482 -8.9; 9330 -8.1; 10263 -8.3; 11289 -8.1; 12418 -7.9; 13660 -11.2; 15026 -14.8; 16529 -14.7; 18182 -10.8; 20000 -4.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung EO-IG955 (AKG) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung EO-IG955 (AKG) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 116 Hz   | 0.75 | -1.4 dB |
| Peaking | 167 Hz   | 0.24 | -3.1 dB |
| Peaking | 778 Hz   | 0.58 | 4.9 dB  |
| Peaking | 15040 Hz | 0.65 | -3.2 dB |
| Peaking | 16210 Hz | 1.11 | -8.3 dB |
| Peaking | 15 Hz    | 1.7  | 0.9 dB  |
| Peaking | 3338 Hz  | 5.36 | -1.1 dB |
| Peaking | 6729 Hz  | 3.85 | 6.7 dB  |
| Peaking | 8127 Hz  | 2.28 | -4.4 dB |
| Peaking | 12391 Hz | 5.35 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.7 dB  |
| Peaking | 250 Hz   | 1.41 | -2.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -13.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Samsung%20EO-IG955%20(AKG)/Samsung%20EO-IG955%20(AKG).png)