# Sennheiser HD 800 S (Dekoni Fenestrated Sheepskin Earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.9; 60 -1.4; 66 -1.9; 72 -2.4; 79 -2.9; 87 -3.4; 96 -4.0; 106 -4.5; 116 -5.0; 128 -5.4; 141 -5.9; 155 -6.3; 170 -6.6; 187 -6.9; 206 -7.1; 227 -7.3; 249 -7.3; 274 -7.3; 302 -7.2; 332 -7.1; 365 -7.0; 402 -6.9; 442 -6.9; 486 -7.0; 535 -6.9; 588 -6.9; 647 -6.9; 712 -6.9; 783 -7.0; 861 -7.0; 947 -6.9; 1042 -6.7; 1146 -6.4; 1261 -5.8; 1387 -4.9; 1526 -3.9; 1678 -3.2; 1846 -2.8; 2031 -2.8; 2234 -3.5; 2457 -4.9; 2703 -6.5; 2973 -7.1; 3270 -6.4; 3597 -5.4; 3957 -5.7; 4353 -7.7; 4788 -9.1; 5267 -8.5; 5793 -8.5; 6373 -9.7; 7010 -9.3; 7711 -9.3; 8482 -8.0; 9330 -6.5; 10263 -8.5; 11289 -12.5; 12418 -13.4; 13660 -12.3; 15026 -13.4; 16529 -15.9; 18182 -18.0; 20000 -21.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 S (Dekoni Fenestrated Sheepskin Earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 S (Dekoni Fenestrated Sheepskin Earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 35 Hz    | 0.63 | 6.8 dB   |
| Peaking | 1942 Hz  | 2.1  | 4.3 dB   |
| Peaking | 2811 Hz  | 5.87 | -1.3 dB  |
| Peaking | 6049 Hz  | 2.55 | -2.0 dB  |
| Peaking | 19771 Hz | 0.3  | -13.8 dB |
| Peaking | 314 Hz   | 0.65 | -1.0 dB  |
| Peaking | 3801 Hz  | 5.62 | 1.8 dB   |
| Peaking | 4676 Hz  | 6.47 | -1.7 dB  |
| Peaking | 9546 Hz  | 4.9  | 3.6 dB   |
| Peaking | 11772 Hz | 4.43 | -3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 4.1 dB   |
| Peaking | 125 Hz   | 1.41 | 0.4 dB   |
| Peaking | 250 Hz   | 1.41 | -1.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -13.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20800%20S%20(Dekoni%20Fenestrated%20Sheepskin%20Earpads)/Sennheiser%20HD%20800%20S%20(Dekoni%20Fenestrated%20Sheepskin%20Earpads).png)