# Tekfusion Twinwoofers
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.0; 23 -15.0; 25 -15.1; 28 -15.2; 31 -15.3; 34 -15.3; 37 -15.3; 41 -15.4; 45 -15.5; 49 -15.5; 54 -15.6; 60 -15.7; 66 -15.8; 72 -16.0; 79 -16.1; 87 -16.2; 96 -16.3; 106 -16.3; 116 -16.1; 128 -16.0; 141 -15.8; 155 -15.6; 170 -15.1; 187 -14.7; 206 -14.2; 227 -13.5; 249 -12.9; 274 -12.1; 302 -11.3; 332 -10.4; 365 -9.6; 402 -8.6; 442 -7.5; 486 -6.7; 535 -5.8; 588 -5.0; 647 -4.8; 712 -5.0; 783 -5.1; 861 -3.7; 947 -4.4; 1042 -4.8; 1146 -4.9; 1261 -4.8; 1387 -4.8; 1526 -4.6; 1678 -4.2; 1846 -3.3; 2031 -2.2; 2234 -1.1; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.2; 4353 -4.6; 4788 -7.3; 5267 -8.9; 5793 -7.4; 6373 -3.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tekfusion Twinwoofers GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tekfusion Twinwoofers ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.34 | -8.5 dB |
| Peaking | 119 Hz   | 0.92 | -5.8 dB |
| Peaking | 227 Hz   | 1.62 | -3.9 dB |
| Peaking | 2654 Hz  | 1.08 | 6.4 dB  |
| Peaking | 22050 Hz | 2.34 | 0.6 dB  |
| Peaking | 347 Hz   | 2.65 | -1.3 dB |
| Peaking | 679 Hz   | 1.3  | 2.2 dB  |
| Peaking | 3895 Hz  | 2.66 | 6.1 dB  |
| Peaking | 5010 Hz  | 1.34 | -6.7 dB |
| Peaking | 6594 Hz  | 4.28 | 6.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.6 dB |
| Peaking | 62 Hz    | 1.41 | -6.7 dB |
| Peaking | 125 Hz   | 1.41 | -8.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Tekfusion%20Twinwoofers/Tekfusion%20Twinwoofers.png)