# Blue MOFI Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.5; 25 -7.5; 28 -7.7; 31 -7.8; 34 -7.8; 37 -7.9; 41 -8.0; 45 -8.0; 49 -8.1; 54 -8.2; 60 -8.3; 66 -8.5; 72 -8.7; 79 -9.0; 87 -9.2; 96 -9.6; 106 -9.8; 116 -9.7; 128 -9.8; 141 -10.5; 155 -10.8; 170 -10.0; 187 -10.5; 206 -10.6; 227 -10.0; 249 -9.4; 274 -8.3; 302 -7.4; 332 -7.1; 365 -7.4; 402 -7.4; 442 -5.9; 486 -5.6; 535 -6.2; 588 -6.3; 647 -6.4; 712 -7.2; 783 -7.5; 861 -7.9; 947 -8.7; 1042 -9.0; 1146 -9.0; 1261 -8.9; 1387 -9.1; 1526 -9.5; 1678 -9.5; 1846 -8.9; 2031 -7.6; 2234 -6.8; 2457 -6.4; 2703 -5.1; 2973 -4.5; 3270 -4.2; 3597 -2.6; 3957 -4.1; 4353 -7.7; 4788 -2.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Blue MOFI Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Blue MOFI Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 96 Hz   | 0.7  | -2.7 dB |
| Peaking | 191 Hz  | 1.79 | -3.0 dB |
| Peaking | 1421 Hz | 1.41 | -3.2 dB |
| Peaking | 3394 Hz | 3.35 | 3.4 dB  |
| Peaking | 5765 Hz | 3.34 | 6.9 dB  |
| Peaking | 26 Hz   | 1.53 | -0.9 dB |
| Peaking | 498 Hz  | 3.36 | 1.5 dB  |
| Peaking | 963 Hz  | 5.86 | -1.0 dB |
| Peaking | 6613 Hz | 6.8  | 2.1 dB  |
| Peaking | 8116 Hz | 1.63 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Blue%20MOFI%20Passive/Blue%20MOFI%20Passive.png)