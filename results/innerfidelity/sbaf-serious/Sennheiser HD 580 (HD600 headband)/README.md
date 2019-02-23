# Sennheiser HD 580 (HD600 headband)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.3; 45 -1.9; 49 -2.3; 54 -2.7; 60 -3.1; 66 -3.7; 72 -4.3; 79 -4.5; 87 -5.1; 96 -6.0; 106 -6.4; 116 -6.7; 128 -7.0; 141 -7.3; 155 -7.5; 170 -7.4; 187 -7.4; 206 -7.5; 227 -7.4; 249 -7.2; 274 -7.1; 302 -6.9; 332 -6.8; 365 -6.5; 402 -6.4; 442 -6.2; 486 -6.3; 535 -6.3; 588 -5.9; 647 -5.9; 712 -6.1; 783 -6.0; 861 -6.4; 947 -6.5; 1042 -6.5; 1146 -7.1; 1261 -7.2; 1387 -7.7; 1526 -8.2; 1678 -8.5; 1846 -8.5; 2031 -8.1; 2234 -7.9; 2457 -7.6; 2703 -7.7; 2973 -7.6; 3270 -8.0; 3597 -8.0; 3957 -7.0; 4353 -7.2; 4788 -7.2; 5267 -4.8; 5793 -2.2; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.3
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
| Peaking | 27 Hz   | 0.47 | 6.2 dB  |
| Peaking | 145 Hz  | 1.02 | -1.9 dB |
| Peaking | 1731 Hz | 2.59 | -1.8 dB |
| Peaking | 4872 Hz | 0.74 | -1.9 dB |
| Peaking | 6163 Hz | 3.35 | 7.6 dB  |
| Peaking | 653 Hz  | 1.97 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20580%20(HD600%20headband)/Sennheiser%20HD%20580%20(HD600%20headband).png)