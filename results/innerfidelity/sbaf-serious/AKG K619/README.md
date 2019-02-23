# AKG K619
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.2; 23 -15.3; 25 -15.4; 28 -15.5; 31 -15.6; 34 -15.6; 37 -15.6; 41 -15.6; 45 -15.5; 49 -15.3; 54 -15.1; 60 -14.8; 66 -14.3; 72 -13.6; 79 -12.6; 87 -11.5; 96 -11.4; 106 -11.4; 116 -10.3; 128 -9.1; 141 -8.8; 155 -7.8; 170 -7.1; 187 -7.0; 206 -6.8; 227 -6.9; 249 -7.0; 274 -7.0; 302 -7.4; 332 -7.9; 365 -8.4; 402 -8.9; 442 -9.1; 486 -9.5; 535 -9.7; 588 -9.6; 647 -9.8; 712 -10.1; 783 -10.0; 861 -10.4; 947 -10.6; 1042 -10.6; 1146 -10.6; 1261 -10.1; 1387 -10.3; 1526 -10.2; 1678 -9.9; 1846 -8.9; 2031 -7.9; 2234 -6.2; 2457 -3.6; 2703 -3.1; 2973 -1.6; 3270 -0.6; 3597 -0.5; 3957 -0.8; 4353 -1.5; 4788 -1.3; 5267 -2.9; 5793 -3.3; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K619 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K619 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 36 Hz   | 0.52 | -10.0 dB |
| Peaking | 1579 Hz | 0.49 | -7.1 dB  |
| Peaking | 3370 Hz | 0.81 | 10.5 dB  |
| Peaking | 6456 Hz | 5.4  | 4.7 dB   |
| Peaking | 7387 Hz | 1.26 | -2.3 dB  |
| Peaking | 22 Hz   | 0.18 | -2.6 dB  |
| Peaking | 36 Hz   | 1.11 | 3.3 dB   |
| Peaking | 195 Hz  | 1.06 | 2.1 dB   |
| Peaking | 459 Hz  | 1.89 | -1.1 dB  |
| Peaking | 1269 Hz | 7.77 | 0.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.6 dB |
| Peaking | 62 Hz    | 1.41 | -6.5 dB |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | -4.3 dB |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K619/AKG%20K619.png)