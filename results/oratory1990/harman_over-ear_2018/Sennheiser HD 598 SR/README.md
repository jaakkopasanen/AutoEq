# Sennheiser HD 598 SR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.0; 31 -1.7; 34 -2.3; 37 -2.9; 41 -3.5; 45 -4.1; 49 -4.6; 54 -5.2; 60 -5.8; 66 -6.3; 72 -6.8; 79 -7.0; 87 -7.2; 96 -7.3; 106 -8.3; 116 -9.3; 128 -9.8; 141 -10.2; 155 -10.5; 170 -10.6; 187 -10.6; 206 -10.6; 227 -10.4; 249 -10.2; 274 -9.9; 302 -9.6; 332 -9.2; 365 -8.8; 402 -8.5; 442 -8.4; 486 -8.3; 535 -7.9; 588 -7.5; 647 -7.3; 712 -5.8; 783 -6.4; 861 -6.9; 947 -6.6; 1042 -6.5; 1146 -6.3; 1261 -6.3; 1387 -5.7; 1526 -4.5; 1678 -3.9; 1846 -3.9; 2031 -4.6; 2234 -4.8; 2457 -4.8; 2703 -6.3; 2973 -7.9; 3270 -8.9; 3597 -7.6; 3957 -6.6; 4353 -8.0; 4788 -7.9; 5267 -8.7; 5793 -9.6; 6373 -4.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.6; 16529 -10.1; 18182 -11.5; 20000 -15.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 598 SR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 SR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.66 | 6.3 dB  |
| Peaking | 189 Hz  | 0.65 | -4.5 dB |
| Peaking | 1878 Hz | 1.66 | 2.9 dB  |
| Peaking | 3217 Hz | 4.36 | -3.0 dB |
| Peaking | 5517 Hz | 7.33 | -3.5 dB |
| Peaking | 96 Hz   | 7.35 | 0.8 dB  |
| Peaking | 707 Hz  | 1.47 | -0.7 dB |
| Peaking | 725 Hz  | 5.49 | 1.9 dB  |
| Peaking | 6204 Hz | 2.26 | -1.8 dB |
| Peaking | 6672 Hz | 6.12 | 5.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -3.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20598%20SR/Sennheiser%20HD%20598%20SR.png)