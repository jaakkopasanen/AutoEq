# T-Peos Tank
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.7; 23 -13.6; 25 -13.5; 28 -13.5; 31 -13.4; 34 -13.3; 37 -13.2; 41 -13.0; 45 -12.9; 49 -12.8; 54 -12.7; 60 -12.6; 66 -12.5; 72 -12.5; 79 -12.4; 87 -12.4; 96 -12.3; 106 -12.0; 116 -11.7; 128 -11.5; 141 -11.2; 155 -10.9; 170 -10.4; 187 -10.0; 206 -9.5; 227 -8.9; 249 -8.4; 274 -7.8; 302 -7.3; 332 -6.7; 365 -6.0; 402 -5.6; 442 -4.9; 486 -4.5; 535 -4.0; 588 -3.4; 647 -3.1; 712 -3.0; 783 -2.8; 861 -3.0; 947 -3.4; 1042 -4.0; 1146 -4.4; 1261 -5.2; 1387 -6.4; 1526 -8.0; 1678 -9.2; 1846 -9.8; 2031 -10.0; 2234 -9.5; 2457 -7.2; 2703 -4.5; 2973 -1.3; 3270 -0.5; 3597 -0.5; 3957 -0.7; 4353 -4.4; 4788 -8.9; 5267 -13.0; 5793 -8.2; 6373 -4.0; 7010 -4.0; 7711 -6.2; 8482 -8.5; 9330 -8.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`T-Peos Tank GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Tank ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.22 | -6.9 dB |
| Peaking | 129 Hz  | 0.81 | -2.8 dB |
| Peaking | 679 Hz  | 1.46 | 4.3 dB  |
| Peaking | 3575 Hz | 3.33 | 7.4 dB  |
| Peaking | 5238 Hz | 7.59 | -8.2 dB |
| Peaking | 1142 Hz | 1.81 | 2.3 dB  |
| Peaking | 1974 Hz | 1.43 | -5.0 dB |
| Peaking | 2925 Hz | 4.3  | 4.3 dB  |
| Peaking | 6680 Hz | 6.03 | 4.1 dB  |
| Peaking | 8870 Hz | 5.37 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Tank/T-Peos%20Tank.png)