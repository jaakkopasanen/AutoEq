# Sennheiser HD 380 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.2; 23 -14.4; 25 -14.4; 28 -14.5; 31 -14.5; 34 -14.4; 37 -14.2; 41 -14.0; 45 -13.6; 49 -13.2; 54 -12.5; 60 -11.7; 66 -10.6; 72 -9.7; 79 -8.0; 87 -5.4; 96 -3.6; 106 -6.6; 116 -7.7; 128 -7.4; 141 -9.1; 155 -7.3; 170 -5.9; 187 -5.8; 206 -4.1; 227 -3.0; 249 -2.8; 274 -3.1; 302 -3.9; 332 -5.0; 365 -6.0; 402 -6.6; 442 -6.8; 486 -7.0; 535 -6.9; 588 -6.2; 647 -5.8; 712 -5.6; 783 -5.0; 861 -4.9; 947 -4.7; 1042 -4.5; 1146 -4.2; 1261 -4.2; 1387 -4.2; 1526 -4.5; 1678 -5.4; 1846 -7.5; 2031 -8.7; 2234 -8.8; 2457 -8.4; 2703 -6.4; 2973 -3.9; 3270 -2.6; 3597 -4.9; 3957 -6.5; 4353 -7.1; 4788 -3.9; 5267 -0.5; 5793 -0.6; 6373 -1.8; 7010 -3.9; 7711 -4.9; 8482 -5.2; 9330 -5.2; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 380 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 380 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 0.74 | -10.3 dB |
| Peaking | 143 Hz  | 7.32 | -3.4 dB  |
| Peaking | 243 Hz  | 3.59 | 3.3 dB   |
| Peaking | 2175 Hz | 4.38 | -4.4 dB  |
| Peaking | 5670 Hz | 4.23 | 5.6 dB   |
| Peaking | 82 Hz   | 0.93 | -3.2 dB  |
| Peaking | 92 Hz   | 4.19 | 6.3 dB   |
| Peaking | 320 Hz  | 0.08 | 0.9 dB   |
| Peaking | 479 Hz  | 1.79 | -2.7 dB  |
| Peaking | 4245 Hz | 7.91 | -3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB  |
| Peaking | 250 Hz   | 1.41 | 2.7 dB   |
| Peaking | 500 Hz   | 1.41 | -2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20380%20Pro/Sennheiser%20HD%20380%20Pro.png)