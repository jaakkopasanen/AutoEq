# Grado RS1e Bowl Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.7; 66 -2.0; 72 -3.6; 79 -5.1; 87 -6.6; 96 -7.9; 106 -8.7; 116 -9.0; 128 -9.4; 141 -9.4; 155 -9.3; 170 -9.0; 187 -8.6; 206 -8.1; 227 -7.5; 249 -7.1; 274 -7.0; 302 -7.7; 332 -7.1; 365 -6.8; 402 -6.6; 442 -6.2; 486 -6.2; 535 -6.1; 588 -5.7; 647 -5.7; 712 -5.9; 783 -5.8; 861 -6.2; 947 -6.5; 1042 -6.8; 1146 -7.2; 1261 -7.8; 1387 -8.7; 1526 -9.5; 1678 -11.8; 1846 -17.3; 2031 -17.7; 2234 -15.1; 2457 -10.8; 2703 -7.4; 2973 -4.7; 3270 -3.6; 3597 -2.8; 3957 -0.8; 4353 -0.5; 4788 -3.5; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS1e Bowl Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1e Bowl Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 72 Hz   | 0.27 | 12.5 dB  |
| Peaking | 121 Hz  | 0.58 | -14.2 dB |
| Peaking | 2004 Hz | 2.98 | -13.4 dB |
| Peaking | 3930 Hz | 1.71 | 6.0 dB   |
| Peaking | 5971 Hz | 4.01 | 5.1 dB   |
| Peaking | 61 Hz   | 5.1  | 1.3 dB   |
| Peaking | 91 Hz   | 4.44 | -0.8 dB  |
| Peaking | 315 Hz  | 4.04 | -1.0 dB  |
| Peaking | 728 Hz  | 1.86 | 0.7 dB   |
| Peaking | 8270 Hz | 4.16 | -1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 4.5 dB   |
| Peaking | 125 Hz   | 1.41 | -4.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.5 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20RS1e%20Bowl%20Pads/Grado%20RS1e%20Bowl%20Pads.png)