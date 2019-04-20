# Hifiman HE400i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.8; 45 -1.4; 49 -2.1; 54 -2.8; 60 -3.6; 66 -4.2; 72 -4.8; 79 -5.4; 87 -5.9; 96 -6.5; 106 -6.9; 116 -7.2; 128 -7.4; 141 -7.6; 155 -7.8; 170 -8.0; 187 -8.0; 206 -8.1; 227 -8.2; 249 -8.2; 274 -8.2; 302 -8.1; 332 -8.0; 365 -7.9; 402 -7.8; 442 -7.4; 486 -6.7; 535 -6.6; 588 -7.2; 647 -7.1; 712 -7.2; 783 -7.2; 861 -7.3; 947 -6.8; 1042 -6.0; 1146 -5.1; 1261 -4.6; 1387 -4.3; 1526 -4.1; 1678 -3.7; 1846 -3.9; 2031 -5.2; 2234 -7.1; 2457 -8.9; 2703 -9.2; 2973 -8.2; 3270 -6.6; 3597 -4.1; 3957 -2.7; 4353 -3.2; 4788 -1.7; 5267 -0.5; 5793 -2.3; 6373 -7.8; 7010 -12.5; 7711 -13.3; 8482 -8.0; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.4; 13660 -6.8; 15026 -6.5; 16529 -6.9; 18182 -10.0; 20000 -17.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hifiman HE400i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hifiman HE400i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 1.07 | 7.0 dB   |
| Peaking | 1688 Hz | 2.29 | 3.4 dB   |
| Peaking | 2646 Hz | 2.83 | -4.7 dB  |
| Peaking | 5360 Hz | 1.47 | 7.9 dB   |
| Peaking | 7202 Hz | 3.14 | -11.5 dB |
| Peaking | 55 Hz   | 1.9  | 1.5 dB   |
| Peaking | 208 Hz  | 0.61 | -1.9 dB  |
| Peaking | 854 Hz  | 3.35 | -0.9 dB  |
| Peaking | 1198 Hz | 4.16 | 1.2 dB   |
| Peaking | 6452 Hz | 4.38 | -0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Hifiman%20HE400i/Hifiman%20HE400i.png)