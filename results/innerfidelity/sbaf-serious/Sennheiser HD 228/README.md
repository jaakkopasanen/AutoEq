# Sennheiser HD 228
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.6; 25 -3.2; 28 -4.1; 31 -5.0; 34 -5.6; 37 -6.1; 41 -6.7; 45 -7.3; 49 -7.8; 54 -8.4; 60 -9.1; 66 -9.7; 72 -10.2; 79 -10.8; 87 -11.2; 96 -11.8; 106 -11.8; 116 -11.4; 128 -11.5; 141 -12.7; 155 -13.5; 170 -13.3; 187 -13.6; 206 -13.2; 227 -12.7; 249 -12.9; 274 -11.3; 302 -10.0; 332 -10.2; 365 -9.5; 402 -8.5; 442 -7.9; 486 -7.4; 535 -6.7; 588 -6.1; 647 -5.9; 712 -6.0; 783 -6.0; 861 -6.4; 947 -6.6; 1042 -6.6; 1146 -6.3; 1261 -5.8; 1387 -5.3; 1526 -5.4; 1678 -6.6; 1846 -5.7; 2031 -5.2; 2234 -4.5; 2457 -3.4; 2703 -3.1; 2973 -1.3; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.0; 4788 -7.7; 5267 -9.1; 5793 -5.4; 6373 -4.5; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.9; 18182 -11.0; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 228 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 228 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 1.06 | 5.4 dB  |
| Peaking | 90 Hz    | 0.82 | -3.9 dB |
| Peaking | 203 Hz   | 1.16 | -6.1 dB |
| Peaking | 3380 Hz  | 1.97 | 6.7 dB  |
| Peaking | 18741 Hz | 1.7  | -5.1 dB |
| Peaking | 646 Hz   | 3    | 1.3 dB  |
| Peaking | 4283 Hz  | 6.9  | 4.1 dB  |
| Peaking | 5036 Hz  | 4.92 | -6.2 dB |
| Peaking | 6733 Hz  | 3.17 | 3.5 dB  |
| Peaking | 7660 Hz  | 3.38 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.1 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -5.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20228/Sennheiser%20HD%20228.png)