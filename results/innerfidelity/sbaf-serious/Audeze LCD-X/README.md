# Audeze LCD-X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -2.6; 25 -2.7; 28 -3.0; 31 -3.5; 34 -4.2; 37 -4.9; 41 -5.4; 45 -5.5; 49 -5.6; 54 -5.6; 60 -5.7; 66 -5.7; 72 -5.9; 79 -6.1; 87 -6.4; 96 -6.8; 106 -6.9; 116 -7.1; 128 -7.5; 141 -7.7; 155 -7.9; 170 -8.0; 187 -8.2; 206 -8.3; 227 -8.3; 249 -8.3; 274 -8.2; 302 -8.1; 332 -7.9; 365 -7.7; 402 -7.6; 442 -7.3; 486 -7.7; 535 -7.7; 588 -7.2; 647 -7.2; 712 -7.3; 783 -6.9; 861 -6.8; 947 -6.5; 1042 -6.4; 1146 -6.4; 1261 -6.5; 1387 -7.1; 1526 -7.3; 1678 -7.4; 1846 -7.3; 2031 -7.5; 2234 -7.2; 2457 -5.9; 2703 -4.1; 2973 -2.4; 3270 -1.3; 3597 -1.2; 3957 -3.1; 4353 -3.3; 4788 -3.9; 5267 -0.5; 5793 -0.6; 6373 -3.0; 7010 -3.7; 7711 -5.5; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -6.3; 16529 -8.2; 18182 -9.8; 20000 -11.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.25 | 3.4 dB  |
| Peaking | 220 Hz   | 0.64 | -2.4 dB |
| Peaking | 3315 Hz  | 3.07 | 5.8 dB  |
| Peaking | 5710 Hz  | 1.94 | 6.2 dB  |
| Peaking | 18183 Hz | 0.03 | -1.7 dB |
| Peaking | 542 Hz   | 2.47 | -0.7 dB |
| Peaking | 1984 Hz  | 3.08 | -1.2 dB |
| Peaking | 6660 Hz  | 3.2  | -0.5 dB |
| Peaking | 11342 Hz | 2.18 | 1.3 dB  |
| Peaking | 14069 Hz | 4.23 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-X/Audeze%20LCD-X.png)