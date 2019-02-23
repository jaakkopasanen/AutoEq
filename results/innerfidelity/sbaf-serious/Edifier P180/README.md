# Edifier P180
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.2; 72 -2.7; 79 -4.4; 87 -5.9; 96 -7.2; 106 -8.0; 116 -8.2; 128 -8.0; 141 -7.8; 155 -7.4; 170 -6.8; 187 -6.3; 206 -5.9; 227 -5.2; 249 -5.0; 274 -4.6; 302 -4.2; 332 -4.0; 365 -4.0; 402 -3.1; 442 -2.8; 486 -2.1; 535 -1.8; 588 -1.2; 647 -1.1; 712 -1.0; 783 -0.8; 861 -0.9; 947 -1.0; 1042 -1.2; 1146 -2.0; 1261 -3.5; 1387 -6.1; 1526 -9.2; 1678 -12.3; 1846 -14.7; 2031 -16.2; 2234 -16.2; 2457 -14.2; 2703 -12.0; 2973 -8.5; 3270 -5.3; 3597 -3.6; 3957 -3.9; 4353 -6.0; 4788 -7.5; 5267 -8.6; 5793 -10.9; 6373 -11.8; 7010 -10.4; 7711 -10.3; 8482 -9.8; 9330 -7.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Edifier P180 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Edifier P180 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 35 Hz    | 0.98 | 7.2 dB   |
| Peaking | 988 Hz   | 0.67 | 9.4 dB   |
| Peaking | 2069 Hz  | 1.22 | -15.4 dB |
| Peaking | 3619 Hz  | 2.28 | 7.6 dB   |
| Peaking | 6517 Hz  | 1.9  | -4.9 dB  |
| Peaking | 38 Hz    | 3.27 | -1.7 dB  |
| Peaking | 64 Hz    | 1.64 | 4.2 dB   |
| Peaking | 107 Hz   | 1.04 | -3.9 dB  |
| Peaking | 306 Hz   | 0.96 | 0.9 dB   |
| Peaking | 10491 Hz | 4.93 | 1.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 4.6 dB   |
| Peaking | 125 Hz   | 1.41 | -3.6 dB  |
| Peaking | 250 Hz   | 1.41 | 1.3 dB   |
| Peaking | 500 Hz   | 1.41 | 3.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 8.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.8 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB  |
| Peaking | 16000 Hz | 1.41 | 0.8 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Edifier%20P180/Edifier%20P180.png)