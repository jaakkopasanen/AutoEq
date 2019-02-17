# Sennheiser HD 800 S (Dekoni Fenestrated Sheepskin earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.6; 60 -1.1; 66 -1.6; 72 -2.0; 79 -2.6; 87 -3.1; 96 -3.6; 106 -4.1; 116 -4.6; 128 -5.1; 141 -5.6; 155 -5.9; 170 -6.3; 187 -6.5; 206 -6.8; 227 -6.9; 249 -7.0; 274 -6.9; 302 -6.8; 332 -6.7; 365 -6.6; 402 -6.6; 442 -6.6; 486 -6.6; 535 -6.6; 588 -6.6; 647 -6.6; 712 -6.6; 783 -6.7; 861 -6.7; 947 -6.6; 1042 -6.3; 1146 -6.1; 1261 -5.5; 1387 -4.5; 1526 -3.6; 1678 -2.7; 1846 -2.3; 2031 -2.4; 2234 -3.0; 2457 -4.4; 2703 -6.4; 2973 -7.0; 3270 -6.2; 3597 -4.8; 3957 -5.0; 4353 -7.4; 4788 -9.4; 5267 -7.8; 5793 -7.7; 6373 -9.7; 7010 -9.2; 7711 -9.1; 8482 -8.2; 9330 -6.5; 10263 -7.7; 11289 -13.2; 12418 -13.6; 13660 -11.1; 15026 -12.6; 16529 -16.7; 18182 -18.1; 20000 -17.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 S (Dekoni Fenestrated Sheepskin earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 S (Dekoni Fenestrated Sheepskin earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.57 | 6.8 dB  |
| Peaking | 1883 Hz  | 2.22 | 4.7 dB  |
| Peaking | 6559 Hz  | 4.54 | -2.6 dB |
| Peaking | 17734 Hz | 0.42 | -4.6 dB |
| Peaking | 19385 Hz | 0.42 | -7.9 dB |
| Peaking | 2936 Hz  | 6.55 | -1.7 dB |
| Peaking | 3802 Hz  | 4.67 | 2.3 dB  |
| Peaking | 4777 Hz  | 7.13 | -2.9 dB |
| Peaking | 9773 Hz  | 4.65 | 3.5 dB  |
| Peaking | 11707 Hz | 5.35 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB   |
| Peaking | 62 Hz    | 1.41 | 4.4 dB   |
| Peaking | 125 Hz   | 1.41 | 0.6 dB   |
| Peaking | 250 Hz   | 1.41 | -0.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB   |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -12.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20800%20S%20(Dekoni%20Fenestrated%20Sheepskin%20earpads)/Sennheiser%20HD%20800%20S%20(Dekoni%20Fenestrated%20Sheepskin%20earpads).png)