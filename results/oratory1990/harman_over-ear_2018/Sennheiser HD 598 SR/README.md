# Sennheiser HD 598 SR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -1.0; 34 -1.5; 37 -2.1; 41 -2.8; 45 -3.3; 49 -3.8; 54 -4.4; 60 -5.1; 66 -5.6; 72 -6.0; 79 -6.3; 87 -6.4; 96 -6.6; 106 -7.5; 116 -8.5; 128 -9.0; 141 -9.5; 155 -9.8; 170 -9.8; 187 -9.8; 206 -9.8; 227 -9.7; 249 -9.5; 274 -9.2; 302 -8.8; 332 -8.4; 365 -8.1; 402 -7.8; 442 -7.7; 486 -7.6; 535 -7.1; 588 -6.8; 647 -6.5; 712 -5.1; 783 -5.7; 861 -6.1; 947 -5.9; 1042 -5.8; 1146 -5.6; 1261 -5.5; 1387 -4.9; 1526 -3.7; 1678 -3.1; 1846 -3.1; 2031 -3.9; 2234 -4.0; 2457 -4.1; 2703 -5.5; 2973 -7.1; 3270 -8.2; 3597 -6.8; 3957 -5.9; 4353 -7.2; 4788 -7.1; 5267 -8.0; 5793 -8.9; 6373 -4.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.9; 16529 -9.4; 18182 -10.7; 20000 -14.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 598 SR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 SR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.65 | 6.3 dB  |
| Peaking | 182 Hz  | 0.83 | -3.9 dB |
| Peaking | 1784 Hz | 1.75 | 3.6 dB  |
| Peaking | 6039 Hz | 2.5  | -4.5 dB |
| Peaking | 6596 Hz | 5.13 | 7.4 dB  |
| Peaking | 57 Hz   | 2.58 | -0.1 dB |
| Peaking | 726 Hz  | 7.01 | 1.6 dB  |
| Peaking | 2462 Hz | 6.45 | 1.5 dB  |
| Peaking | 3299 Hz | 3.5  | -2.6 dB |
| Peaking | 3795 Hz | 4.85 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.8 dB |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20598%20SR/Sennheiser%20HD%20598%20SR.png)