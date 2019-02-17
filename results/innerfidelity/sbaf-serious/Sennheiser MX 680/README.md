# Sennheiser MX 680
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.6; 206 -1.2; 227 -1.6; 249 -2.1; 274 -2.4; 302 -2.8; 332 -3.1; 365 -3.2; 402 -3.0; 442 -3.3; 486 -3.4; 535 -3.7; 588 -3.8; 647 -4.5; 712 -4.9; 783 -5.1; 861 -5.6; 947 -6.2; 1042 -6.4; 1146 -7.1; 1261 -8.2; 1387 -9.7; 1526 -11.6; 1678 -13.6; 1846 -15.5; 2031 -17.0; 2234 -17.7; 2457 -17.3; 2703 -16.6; 2973 -13.6; 3270 -10.6; 3597 -8.6; 3957 -8.8; 4353 -10.7; 4788 -11.8; 5267 -12.9; 5793 -15.7; 6373 -16.6; 7010 -14.0; 7711 -12.1; 8482 -12.3; 9330 -12.0; 10263 -8.8; 11289 -6.5; 12418 -6.5; 13660 -6.9; 15026 -8.7; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MX 680 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MX 680 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.1  | 5.7 dB   |
| Peaking | 342 Hz   | 0.26 | 2.3 dB   |
| Peaking | 2168 Hz  | 1.6  | -12.3 dB |
| Peaking | 6491 Hz  | 1.76 | -9.1 dB  |
| Peaking | 14855 Hz | 6.39 | -2.2 dB  |
| Peaking | 2749 Hz  | 7.22 | -2.6 dB  |
| Peaking | 3672 Hz  | 3.89 | 3.2 dB   |
| Peaking | 7491 Hz  | 3.27 | 4.8 dB   |
| Peaking | 9040 Hz  | 1.24 | -6.0 dB  |
| Peaking | 11097 Hz | 1.88 | 4.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB   |
| Peaking | 62 Hz    | 1.41 | 4.2 dB   |
| Peaking | 125 Hz   | 1.41 | 5.1 dB   |
| Peaking | 250 Hz   | 1.41 | 3.4 dB   |
| Peaking | 500 Hz   | 1.41 | 2.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.3 dB |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.1 dB  |
| Peaking | 16000 Hz | 1.41 | 0.2 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20MX%20680/Sennheiser%20MX%20680.png)