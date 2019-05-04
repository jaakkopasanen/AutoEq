# Stax SR-404 (with perfect seal)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -0.9; 37 -1.2; 41 -1.5; 45 -1.8; 49 -2.0; 54 -2.2; 60 -2.4; 66 -2.6; 72 -2.9; 79 -3.3; 87 -3.6; 96 -4.0; 106 -4.4; 116 -4.8; 128 -5.2; 141 -5.5; 155 -5.7; 170 -5.9; 187 -6.1; 206 -6.2; 227 -6.3; 249 -6.4; 274 -6.4; 302 -6.3; 332 -6.2; 365 -6.1; 402 -6.1; 442 -6.2; 486 -6.2; 535 -6.2; 588 -6.3; 647 -6.5; 712 -6.7; 783 -7.1; 861 -7.7; 947 -8.3; 1042 -9.0; 1146 -9.6; 1261 -10.5; 1387 -11.4; 1526 -11.6; 1678 -10.7; 1846 -10.6; 2031 -9.7; 2234 -8.2; 2457 -7.2; 2703 -6.6; 2973 -7.0; 3270 -7.4; 3597 -6.4; 3957 -5.1; 4353 -3.3; 4788 -3.2; 5267 -5.4; 5793 -8.9; 6373 -7.3; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -8.4; 11289 -10.5; 12418 -7.8; 13660 -7.1; 15026 -9.9; 16529 -13.4; 18182 -17.3; 20000 -22.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-404 (with perfect seal) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-404 (with perfect seal) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.46 | 6.0 dB   |
| Peaking | 74 Hz    | 1.24 | 1.3 dB   |
| Peaking | 1498 Hz  | 1.64 | -5.3 dB  |
| Peaking | 4530 Hz  | 4.66 | 4.4 dB   |
| Peaking | 19638 Hz | 0.69 | -15.5 dB |
| Peaking | 5979 Hz  | 5.55 | -5.4 dB  |
| Peaking | 6606 Hz  | 2.3  | 3.2 dB   |
| Peaking | 10966 Hz | 7.76 | -2.6 dB  |
| Peaking | 11534 Hz | 6.69 | -1.7 dB  |
| Peaking | 13440 Hz | 3.86 | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 3.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -8.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Stax%20SR-404%20(with%20perfect%20seal)/Stax%20SR-404%20(with%20perfect%20seal).png)