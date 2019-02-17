# Sennheiser HD 580 (HD600 headband)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.9; 41 -1.5; 45 -2.1; 49 -2.5; 54 -2.9; 60 -3.3; 66 -3.9; 72 -4.5; 79 -4.7; 87 -5.4; 96 -6.2; 106 -6.6; 116 -6.9; 128 -7.2; 141 -7.5; 155 -7.7; 170 -7.6; 187 -7.6; 206 -7.7; 227 -7.6; 249 -7.4; 274 -7.3; 302 -7.1; 332 -7.0; 365 -6.8; 402 -6.6; 442 -6.4; 486 -6.5; 535 -6.5; 588 -6.2; 647 -6.2; 712 -6.4; 783 -6.3; 861 -6.6; 947 -6.7; 1042 -6.7; 1146 -7.3; 1261 -7.4; 1387 -8.0; 1526 -8.4; 1678 -8.7; 1846 -8.7; 2031 -8.4; 2234 -8.1; 2457 -7.9; 2703 -7.9; 2973 -7.8; 3270 -8.2; 3597 -8.2; 3957 -7.2; 4353 -7.4; 4788 -7.4; 5267 -5.0; 5793 -2.4; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 580 (HD600 headband) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 580 (HD600 headband) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.48 | 6.3 dB  |
| Peaking | 148 Hz  | 0.91 | -2.0 dB |
| Peaking | 1717 Hz | 2.32 | -1.9 dB |
| Peaking | 4726 Hz | 0.7  | -2.0 dB |
| Peaking | 6185 Hz | 3.38 | 7.6 dB  |
| Peaking | 652 Hz  | 2.31 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20580%20(HD600%20headband)/Sennheiser%20HD%20580%20(HD600%20headband).png)