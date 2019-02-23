# Sennheiser MX 680
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.8; 249 -1.4; 274 -1.6; 302 -2.0; 332 -2.3; 365 -2.4; 402 -2.2; 442 -2.5; 486 -2.6; 535 -2.9; 588 -3.0; 647 -3.7; 712 -4.1; 783 -4.3; 861 -4.8; 947 -5.4; 1042 -5.6; 1146 -6.3; 1261 -7.4; 1387 -8.9; 1526 -10.8; 1678 -12.8; 1846 -14.8; 2031 -16.2; 2234 -16.9; 2457 -16.5; 2703 -15.8; 2973 -12.8; 3270 -9.8; 3597 -7.8; 3957 -8.0; 4353 -9.9; 4788 -11.0; 5267 -12.1; 5793 -14.9; 6373 -15.9; 7010 -13.2; 7711 -11.3; 8482 -11.5; 9330 -11.2; 10263 -8.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.9; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MX 680 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MX 680 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 0.12 | 5.7 dB   |
| Peaking | 349 Hz   | 0.31 | 3.5 dB   |
| Peaking | 2166 Hz  | 1.67 | -11.7 dB |
| Peaking | 6443 Hz  | 1.95 | -8.6 dB  |
| Peaking | 22049 Hz | 1.95 | 0.1 dB   |
| Peaking | 2746 Hz  | 6.94 | -2.7 dB  |
| Peaking | 3651 Hz  | 4.79 | 2.8 dB   |
| Peaking | 5874 Hz  | 3.19 | -1.9 dB  |
| Peaking | 8505 Hz  | 1.25 | 3.5 dB   |
| Peaking | 8993 Hz  | 3.33 | -6.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB   |
| Peaking | 62 Hz    | 1.41 | 4.3 dB   |
| Peaking | 125 Hz   | 1.41 | 4.8 dB   |
| Peaking | 250 Hz   | 1.41 | 4.2 dB   |
| Peaking | 500 Hz   | 1.41 | 2.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -10.6 dB |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.4 dB  |
| Peaking | 16000 Hz | 1.41 | 0.5 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20MX%20680/Sennheiser%20MX%20680.png)