# Sennheiser HD 212Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.2; 45 -2.3; 49 -3.2; 54 -4.3; 60 -5.4; 66 -5.7; 72 -6.2; 79 -7.1; 87 -7.8; 96 -8.3; 106 -8.7; 116 -8.7; 128 -7.7; 141 -6.1; 155 -6.5; 170 -6.5; 187 -6.3; 206 -6.0; 227 -5.6; 249 -5.4; 274 -5.3; 302 -6.5; 332 -6.9; 365 -7.0; 402 -6.6; 442 -6.5; 486 -6.8; 535 -7.2; 588 -7.5; 647 -8.0; 712 -8.6; 783 -8.9; 861 -8.8; 947 -9.1; 1042 -9.6; 1146 -9.6; 1261 -9.4; 1387 -9.5; 1526 -9.8; 1678 -9.6; 1846 -8.8; 2031 -8.2; 2234 -7.5; 2457 -6.1; 2703 -5.4; 2973 -3.4; 3270 -0.5; 3597 -2.0; 3957 -8.5; 4353 -10.0; 4788 -7.4; 5267 -4.5; 5793 -1.1; 6373 -5.0; 7010 -8.1; 7711 -6.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -11.6; 15026 -11.7; 16529 -10.7; 18182 -10.2; 20000 -7.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 212Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 212Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 1.34 | 7.1 dB  |
| Peaking | 1259 Hz  | 0.89 | -3.4 dB |
| Peaking | 3253 Hz  | 5.69 | 7.5 dB  |
| Peaking | 11952 Hz | 0.71 | 6.0 dB  |
| Peaking | 14645 Hz | 0.69 | -9.4 dB |
| Peaking | 83 Hz    | 0.5  | 1.8 dB  |
| Peaking | 99 Hz    | 1.5  | -4.3 dB |
| Peaking | 255 Hz   | 4.76 | 1.2 dB  |
| Peaking | 4274 Hz  | 6.86 | -4.9 dB |
| Peaking | 5707 Hz  | 8.37 | 6.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | 1.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -3.4 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -6.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20212Pro/Sennheiser%20HD%20212Pro.png)