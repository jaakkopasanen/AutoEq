# Samsung EO-IG955 (AKG)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -7.0; 25 -7.3; 28 -7.6; 31 -7.9; 34 -8.1; 37 -8.3; 41 -8.6; 45 -8.8; 49 -8.9; 54 -9.1; 60 -9.4; 66 -9.6; 72 -9.8; 79 -10.0; 87 -10.2; 96 -10.4; 106 -10.5; 116 -10.6; 128 -10.5; 141 -10.4; 155 -10.3; 170 -9.9; 187 -9.2; 206 -9.4; 227 -9.2; 249 -8.8; 274 -8.3; 302 -7.7; 332 -7.1; 365 -6.4; 402 -5.9; 442 -5.4; 486 -4.8; 535 -4.3; 588 -3.8; 647 -3.3; 712 -2.8; 783 -2.4; 861 -2.2; 947 -2.4; 1042 -2.7; 1146 -3.1; 1261 -3.3; 1387 -3.3; 1526 -3.2; 1678 -3.2; 1846 -3.1; 2031 -2.9; 2234 -2.7; 2457 -2.6; 2703 -2.6; 2973 -3.0; 3270 -3.5; 3597 -3.8; 3957 -3.8; 4353 -3.4; 4788 -4.0; 5267 -5.1; 5793 -3.3; 6373 -0.5; 7010 -0.7; 7711 -5.0; 8482 -8.2; 9330 -10.1; 10263 -11.6; 11289 -10.5; 12418 -11.4; 13660 -21.1; 15026 -32.2; 16529 -34.6; 18182 -28.3; 20000 -15.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung EO-IG955 (AKG) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung EO-IG955 (AKG) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 46 Hz    | 0.36 | -5.3 dB  |
| Peaking | 132 Hz   | 0.77 | -4.5 dB  |
| Peaking | 275 Hz   | 1.2  | -3.1 dB  |
| Peaking | 15656 Hz | 1.79 | -22.0 dB |
| Peaking | 17999 Hz | 0.85 | -22.0 dB |
| Peaking | 824 Hz   | 4.25 | 1.1 dB   |
| Peaking | 5361 Hz  | 4.29 | -2.1 dB  |
| Peaking | 6682 Hz  | 3.55 | 6.2 dB   |
| Peaking | 9094 Hz  | 3.71 | -2.9 dB  |
| Peaking | 19886 Hz | 2.29 | -2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB  |
| Peaking | 62 Hz    | 1.41 | -5.3 dB  |
| Peaking | 125 Hz   | 1.41 | -6.7 dB  |
| Peaking | 250 Hz   | 1.41 | -5.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 8.1 dB   |
| Peaking | 16000 Hz | 1.41 | -43.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Samsung%20EO-IG955%20(AKG)/Samsung%20EO-IG955%20(AKG).png)