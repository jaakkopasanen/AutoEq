# Etymotic Research ER-4XR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.7; 25 -3.7; 28 -3.8; 31 -3.9; 34 -3.9; 37 -4.0; 41 -4.1; 45 -4.3; 49 -4.4; 54 -4.6; 60 -4.8; 66 -5.0; 72 -5.2; 79 -5.5; 87 -5.8; 96 -6.1; 106 -6.4; 116 -6.7; 128 -7.0; 141 -7.2; 155 -7.3; 170 -7.4; 187 -7.5; 206 -7.5; 227 -7.5; 249 -7.4; 274 -7.4; 302 -7.2; 332 -7.0; 365 -6.9; 402 -6.8; 442 -6.7; 486 -6.6; 535 -6.5; 588 -6.4; 647 -6.3; 712 -6.2; 783 -6.2; 861 -6.4; 947 -6.9; 1042 -7.6; 1146 -8.3; 1261 -8.7; 1387 -8.9; 1526 -8.8; 1678 -8.6; 1846 -8.4; 2031 -7.9; 2234 -7.4; 2457 -6.9; 2703 -6.3; 2973 -5.5; 3270 -4.8; 3597 -4.4; 3957 -4.3; 4353 -4.2; 4788 -3.8; 5267 -2.6; 5793 -0.7; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -7.3; 10263 -11.1; 11289 -11.6; 12418 -14.1; 13660 -21.3; 15026 -26.7; 16529 -23.3; 18182 -15.3; 20000 -10.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic Research ER-4XR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic Research ER-4XR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.35 | 2.3 dB   |
| Peaking | 181 Hz   | 0.74 | -1.9 dB  |
| Peaking | 1555 Hz  | 1.33 | -3.2 dB  |
| Peaking | 6356 Hz  | 1.07 | 7.1 dB   |
| Peaking | 15432 Hz | 1.03 | -22.3 dB |
| Peaking | 773 Hz   | 4.56 | 0.6 dB   |
| Peaking | 5002 Hz  | 3.37 | -2.2 dB  |
| Peaking | 6239 Hz  | 1.69 | 2.5 dB   |
| Peaking | 7353 Hz  | 5.09 | -3.4 dB  |
| Peaking | 11936 Hz | 8.39 | 2.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB   |
| Peaking | 62 Hz    | 1.41 | 1.0 dB   |
| Peaking | 125 Hz   | 1.41 | -1.0 dB  |
| Peaking | 250 Hz   | 1.41 | -1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 16000 Hz | 1.41 | -25.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Etymotic%20Research%20ER-4XR/Etymotic%20Research%20ER-4XR.png)