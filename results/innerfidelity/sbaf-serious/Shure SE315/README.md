# Shure SE315
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -3.6; 25 -3.7; 28 -3.8; 31 -3.9; 34 -4.0; 37 -4.1; 41 -4.3; 45 -4.4; 49 -4.6; 54 -4.8; 60 -5.1; 66 -5.4; 72 -5.7; 79 -6.1; 87 -6.5; 96 -7.0; 106 -7.3; 116 -7.5; 128 -7.8; 141 -8.0; 155 -8.2; 170 -8.3; 187 -8.4; 206 -8.5; 227 -8.4; 249 -8.4; 274 -8.3; 302 -8.2; 332 -8.1; 365 -7.9; 402 -7.8; 442 -7.6; 486 -7.7; 535 -7.6; 588 -7.2; 647 -7.3; 712 -7.5; 783 -7.6; 861 -8.2; 947 -8.8; 1042 -9.7; 1146 -10.4; 1261 -11.2; 1387 -12.3; 1526 -13.3; 1678 -13.9; 1846 -13.5; 2031 -12.1; 2234 -9.7; 2457 -6.5; 2703 -3.6; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -0.7; 4353 -3.6; 4788 -3.9; 5267 -1.0; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE315 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE315 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.35 | 3.0 dB  |
| Peaking | 177 Hz  | 0.64 | -2.3 dB |
| Peaking | 1767 Hz | 1.28 | -9.3 dB |
| Peaking | 3177 Hz | 1.67 | 9.0 dB  |
| Peaking | 5909 Hz | 3.7  | 5.8 dB  |
| Peaking | 731 Hz  | 1.55 | 1.5 dB  |
| Peaking | 813 Hz  | 0.82 | -1.2 dB |
| Peaking | 1759 Hz | 0.43 | 0.2 dB  |
| Peaking | 6649 Hz | 8.6  | 1.9 dB  |
| Peaking | 7697 Hz | 2.05 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | -6.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE315/Shure%20SE315.png)