# Focal Utopia
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.0; 37 -1.2; 41 -1.4; 45 -1.6; 49 -1.7; 54 -2.0; 60 -2.3; 66 -2.6; 72 -3.0; 79 -3.3; 87 -3.8; 96 -4.2; 106 -4.7; 116 -5.0; 128 -5.4; 141 -5.6; 155 -5.8; 170 -6.0; 187 -6.0; 206 -6.1; 227 -6.1; 249 -6.0; 274 -5.7; 302 -5.5; 332 -5.3; 365 -5.1; 402 -5.0; 442 -4.9; 486 -4.8; 535 -4.7; 588 -4.7; 647 -4.8; 712 -5.0; 783 -5.4; 861 -5.9; 947 -6.2; 1042 -6.7; 1146 -6.9; 1261 -6.9; 1387 -5.7; 1526 -4.2; 1678 -2.0; 1846 -0.6; 2031 -0.5; 2234 -0.9; 2457 -2.9; 2703 -4.1; 2973 -3.6; 3270 -3.2; 3597 -2.6; 3957 -4.5; 4353 -5.2; 4788 -5.2; 5267 -6.6; 5793 -9.5; 6373 -4.9; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.0; 18182 -11.7; 20000 -22.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Utopia GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Utopia ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.6  | 5.8 dB  |
| Peaking | 63 Hz   | 1.07 | 2.1 dB  |
| Peaking | 499 Hz  | 1.53 | 1.9 dB  |
| Peaking | 2001 Hz | 2.76 | 6.5 dB  |
| Peaking | 3480 Hz | 3.41 | 3.3 dB  |
| Peaking | 708 Hz  | 4.16 | 0.7 dB  |
| Peaking | 1204 Hz | 2.86 | -1.6 dB |
| Peaking | 1677 Hz | 6.12 | 1.3 dB  |
| Peaking | 5742 Hz | 9.33 | -4.3 dB |
| Peaking | 6710 Hz | 6.61 | 3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focal%20Utopia/Focal%20Utopia.png)