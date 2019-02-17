# Tekfusion Twinwoofers
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.7; 23 -16.8; 25 -16.8; 28 -17.0; 31 -17.1; 34 -17.1; 37 -17.1; 41 -17.1; 45 -17.2; 49 -17.3; 54 -17.3; 60 -17.5; 66 -17.6; 72 -17.7; 79 -17.9; 87 -18.0; 96 -18.1; 106 -18.0; 116 -17.9; 128 -17.8; 141 -17.6; 155 -17.3; 170 -16.9; 187 -16.5; 206 -15.9; 227 -15.3; 249 -14.7; 274 -13.8; 302 -13.1; 332 -12.2; 365 -11.3; 402 -10.3; 442 -9.3; 486 -8.5; 535 -7.6; 588 -6.7; 647 -6.5; 712 -6.8; 783 -6.9; 861 -5.4; 947 -6.2; 1042 -6.6; 1146 -6.7; 1261 -6.6; 1387 -6.5; 1526 -6.4; 1678 -5.9; 1846 -5.0; 2031 -4.0; 2234 -2.9; 2457 -1.4; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.7; 3957 -2.9; 4353 -6.3; 4788 -9.0; 5267 -10.7; 5793 -9.2; 6373 -5.1; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tekfusion Twinwoofers GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tekfusion Twinwoofers ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.25 | -9.9 dB |
| Peaking | 128 Hz  | 0.74 | -6.1 dB |
| Peaking | 253 Hz  | 1.31 | -3.7 dB |
| Peaking | 3162 Hz | 1.34 | 7.0 dB  |
| Peaking | 5061 Hz | 3.8  | -6.9 dB |
| Peaking | 611 Hz  | 3.39 | 1.7 dB  |
| Peaking | 878 Hz  | 4.69 | 1.9 dB  |
| Peaking | 2172 Hz | 0.39 | -1.8 dB |
| Peaking | 2593 Hz | 1.02 | 2.1 dB  |
| Peaking | 6751 Hz | 7.46 | 3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.5 dB |
| Peaking | 62 Hz    | 1.41 | -7.9 dB  |
| Peaking | 125 Hz   | 1.41 | -9.4 dB  |
| Peaking | 250 Hz   | 1.41 | -6.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 16000 Hz | 1.41 | 0.0 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Tekfusion%20Twinwoofers/Tekfusion%20Twinwoofers.png)