# Philips Cityscape Downtown
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -1.5; 25 -1.5; 28 -1.6; 31 -1.6; 34 -1.6; 37 -1.5; 41 -1.5; 45 -1.5; 49 -1.4; 54 -1.4; 60 -1.3; 66 -1.3; 72 -1.3; 79 -1.3; 87 -1.4; 96 -1.6; 106 -1.6; 116 -1.5; 128 -1.4; 141 -1.6; 155 -2.0; 170 -1.7; 187 -2.4; 206 -2.6; 227 -2.6; 249 -2.8; 274 -2.8; 302 -2.9; 332 -2.9; 365 -2.9; 402 -3.2; 442 -3.6; 486 -4.2; 535 -4.7; 588 -4.8; 647 -5.2; 712 -5.7; 783 -5.9; 861 -6.3; 947 -6.5; 1042 -6.5; 1146 -6.2; 1261 -5.8; 1387 -5.7; 1526 -5.2; 1678 -4.3; 1846 -3.2; 2031 -1.4; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.8; 4353 -2.1; 4788 -1.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Cityscape Downtown GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Cityscape Downtown ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.25 | 4.9 dB  |
| Peaking | 158 Hz  | 0.75 | 2.3 dB  |
| Peaking | 370 Hz  | 1.73 | 2.3 dB  |
| Peaking | 2843 Hz | 1.22 | 6.4 dB  |
| Peaking | 5604 Hz | 2.62 | 5.2 dB  |
| Peaking | 1138 Hz | 1.79 | -1.0 dB |
| Peaking | 2130 Hz | 5.19 | 1.8 dB  |
| Peaking | 2862 Hz | 3.63 | -1.0 dB |
| Peaking | 3825 Hz | 5.32 | 1.3 dB  |
| Peaking | 8352 Hz | 3.68 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 3.9 dB  |
| Peaking | 125 Hz   | 1.41 | 3.9 dB  |
| Peaking | 250 Hz   | 1.41 | 3.0 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Cityscape%20Downtown/Philips%20Cityscape%20Downtown.png)