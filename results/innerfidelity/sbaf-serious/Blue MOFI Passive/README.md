# Blue MOFI Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.1; 25 -5.1; 28 -5.3; 31 -5.4; 34 -5.4; 37 -5.5; 41 -5.6; 45 -5.6; 49 -5.7; 54 -5.8; 60 -5.9; 66 -6.1; 72 -6.3; 79 -6.6; 87 -6.8; 96 -7.3; 106 -7.4; 116 -7.3; 128 -7.4; 141 -8.1; 155 -8.4; 170 -7.6; 187 -8.1; 206 -8.2; 227 -7.6; 249 -7.0; 274 -5.9; 302 -5.0; 332 -4.7; 365 -5.0; 402 -5.0; 442 -3.5; 486 -3.2; 535 -3.8; 588 -3.9; 647 -4.0; 712 -4.8; 783 -5.1; 861 -5.5; 947 -6.3; 1042 -6.6; 1146 -6.6; 1261 -6.6; 1387 -6.7; 1526 -7.1; 1678 -7.1; 1846 -6.5; 2031 -5.2; 2234 -4.4; 2457 -4.0; 2703 -2.7; 2973 -2.1; 3270 -1.8; 3597 -0.6; 3957 -2.2; 4353 -5.3; 4788 -0.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Blue MOFI Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Blue MOFI Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 188 Hz  | 1.17 | -2.0 dB |
| Peaking | 308 Hz  | 3.54 | 1.8 dB  |
| Peaking | 515 Hz  | 1.83 | 3.4 dB  |
| Peaking | 3266 Hz | 2.28 | 5.0 dB  |
| Peaking | 5673 Hz | 2.89 | 6.3 dB  |
| Peaking | 23 Hz   | 1.11 | 1.5 dB  |
| Peaking | 50 Hz   | 2.16 | 0.7 dB  |
| Peaking | 1709 Hz | 2.03 | -1.8 dB |
| Peaking | 2189 Hz | 2.63 | 1.5 dB  |
| Peaking | 8218 Hz | 4.63 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 3.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Blue%20MOFI%20Passive/Blue%20MOFI%20Passive.png)