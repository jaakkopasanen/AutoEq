# Skullcandy Holua
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.8; 23 -13.8; 25 -13.7; 28 -13.5; 31 -13.4; 34 -13.3; 37 -13.1; 41 -13.0; 45 -12.9; 49 -12.7; 54 -12.6; 60 -12.5; 66 -12.4; 72 -12.3; 79 -12.2; 87 -12.1; 96 -12.0; 106 -11.8; 116 -11.5; 128 -11.3; 141 -11.0; 155 -10.7; 170 -10.2; 187 -9.8; 206 -9.3; 227 -8.8; 249 -8.3; 274 -7.7; 302 -7.2; 332 -6.6; 365 -6.1; 402 -5.6; 442 -4.9; 486 -4.6; 535 -4.2; 588 -3.5; 647 -3.2; 712 -3.2; 783 -2.9; 861 -3.1; 947 -3.5; 1042 -4.2; 1146 -4.6; 1261 -5.2; 1387 -6.2; 1526 -7.4; 1678 -8.4; 1846 -9.4; 2031 -10.5; 2234 -12.3; 2457 -12.3; 2703 -8.8; 2973 -5.0; 3270 -1.7; 3597 -0.5; 3957 -2.8; 4353 -7.2; 4788 -14.0; 5267 -9.3; 5793 -2.9; 6373 -0.6; 7010 -3.6; 7711 -5.8; 8482 -6.1; 9330 -6.1; 10263 -6.1; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Holua GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Holua ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 0.21 | -7.5 dB  |
| Peaking | 139 Hz  | 0.89 | -2.8 dB  |
| Peaking | 2164 Hz | 1.41 | -16.7 dB |
| Peaking | 2424 Hz | 0.43 | 10.2 dB  |
| Peaking | 4843 Hz | 7.05 | -13.4 dB |
| Peaking | 2520 Hz | 8.28 | -2.1 dB  |
| Peaking | 2804 Hz | 4.9  | -0.8 dB  |
| Peaking | 3485 Hz | 3.47 | 4.7 dB   |
| Peaking | 6300 Hz | 4.05 | 7.1 dB   |
| Peaking | 6643 Hz | 0.88 | -3.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.7 dB |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Holua/Skullcandy%20Holua.png)