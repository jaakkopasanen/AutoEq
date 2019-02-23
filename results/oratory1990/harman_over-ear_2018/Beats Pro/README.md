# Beats Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -3.2; 25 -4.0; 28 -5.1; 31 -6.0; 34 -6.6; 37 -7.1; 41 -7.6; 45 -7.9; 49 -8.1; 54 -8.2; 60 -8.2; 66 -8.1; 72 -8.0; 79 -8.2; 87 -8.5; 96 -8.9; 106 -9.3; 116 -9.3; 128 -9.5; 141 -9.8; 155 -9.9; 170 -9.8; 187 -9.7; 206 -9.4; 227 -8.9; 249 -8.2; 274 -7.4; 302 -6.0; 332 -5.3; 365 -4.4; 402 -3.5; 442 -3.2; 486 -3.3; 535 -3.4; 588 -3.4; 647 -3.2; 712 -2.8; 783 -2.8; 861 -2.4; 947 -1.4; 1042 -1.6; 1146 -1.2; 1261 -0.8; 1387 -0.5; 1526 -0.9; 1678 -1.8; 1846 -3.1; 2031 -4.8; 2234 -6.8; 2457 -8.9; 2703 -10.8; 2973 -11.2; 3270 -9.1; 3597 -5.5; 3957 -1.7; 4353 -2.7; 4788 -5.0; 5267 -2.6; 5793 -1.6; 6373 -5.5; 7010 -6.5; 7711 -6.9; 8482 -5.2; 9330 -5.2; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 18 Hz   | 1.43 | 4.8 dB   |
| Peaking | 53 Hz   | 0.39 | -3.1 dB  |
| Peaking | 180 Hz  | 1.15 | -4.1 dB  |
| Peaking | 1616 Hz | 0.36 | 5.0 dB   |
| Peaking | 2746 Hz | 2.39 | -10.9 dB |
| Peaking | 403 Hz  | 5.47 | 1.3 dB   |
| Peaking | 3248 Hz | 7.97 | -1.8 dB  |
| Peaking | 4022 Hz | 6.8  | 4.2 dB   |
| Peaking | 5757 Hz | 5.22 | 6.1 dB   |
| Peaking | 6357 Hz | 1.73 | -4.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beats%20Pro/Beats%20Pro.png)