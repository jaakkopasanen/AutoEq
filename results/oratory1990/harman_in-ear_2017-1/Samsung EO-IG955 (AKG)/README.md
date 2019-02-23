# Samsung EO-IG955 (AKG)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -6.9; 25 -7.2; 28 -7.6; 31 -7.8; 34 -8.1; 37 -8.3; 41 -8.5; 45 -8.7; 49 -8.9; 54 -9.1; 60 -9.3; 66 -9.5; 72 -9.7; 79 -9.9; 87 -10.1; 96 -10.3; 106 -10.4; 116 -10.5; 128 -10.5; 141 -10.4; 155 -10.2; 170 -9.9; 187 -9.1; 206 -9.3; 227 -9.2; 249 -8.7; 274 -8.2; 302 -7.6; 332 -7.0; 365 -6.4; 402 -5.9; 442 -5.3; 486 -4.8; 535 -4.2; 588 -3.7; 647 -3.2; 712 -2.7; 783 -2.3; 861 -2.2; 947 -2.3; 1042 -2.7; 1146 -3.0; 1261 -3.2; 1387 -3.2; 1526 -3.2; 1678 -3.1; 1846 -3.1; 2031 -2.9; 2234 -2.6; 2457 -2.5; 2703 -2.5; 2973 -2.9; 3270 -3.5; 3597 -3.8; 3957 -3.7; 4353 -3.3; 4788 -4.0; 5267 -5.0; 5793 -3.2; 6373 -0.5; 7010 -2.7; 7711 -5.2; 8482 -8.1; 9330 -10.1; 10263 -11.6; 11289 -10.4; 12418 -11.4; 13660 -21.1; 15026 -32.1; 16529 -34.5; 18182 -28.2; 20000 -15.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung EO-IG955 (AKG) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung EO-IG955 (AKG) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 102 Hz   | 0.4  | -5.4 dB  |
| Peaking | 253 Hz   | 0.97 | -2.2 dB  |
| Peaking | 2411 Hz  | 0.08 | 3.1 dB   |
| Peaking | 15593 Hz | 1.76 | -20.3 dB |
| Peaking | 17748 Hz | 0.79 | -20.5 dB |
| Peaking | 808 Hz   | 2.61 | 1.3 dB   |
| Peaking | 6588 Hz  | 5.13 | 5.4 dB   |
| Peaking | 9786 Hz  | 2.83 | -2.3 dB  |
| Peaking | 12120 Hz | 4.34 | 5.5 dB   |
| Peaking | 14619 Hz | 0.03 | -0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB  |
| Peaking | 62 Hz    | 1.41 | -3.3 dB  |
| Peaking | 125 Hz   | 1.41 | -4.6 dB  |
| Peaking | 250 Hz   | 1.41 | -3.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.9 dB   |
| Peaking | 16000 Hz | 1.41 | -38.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Samsung%20EO-IG955%20(AKG)/Samsung%20EO-IG955%20(AKG).png)