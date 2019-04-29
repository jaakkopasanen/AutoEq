# Kumitate KL-Corona sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.3; 25 -2.1; 28 -2.9; 31 -3.6; 34 -4.1; 37 -4.5; 41 -5.0; 45 -5.5; 49 -5.9; 54 -6.3; 60 -6.6; 66 -7.0; 72 -7.4; 79 -7.8; 87 -8.1; 96 -8.5; 106 -8.8; 116 -9.0; 128 -9.2; 141 -9.2; 155 -9.2; 170 -9.1; 187 -9.1; 206 -9.0; 227 -8.8; 249 -8.5; 274 -8.3; 302 -8.1; 332 -7.8; 365 -7.4; 402 -7.1; 442 -6.8; 486 -6.5; 535 -6.2; 588 -5.9; 647 -5.4; 712 -4.9; 783 -4.4; 861 -4.0; 947 -3.8; 1042 -4.0; 1146 -4.7; 1261 -5.4; 1387 -5.9; 1526 -6.0; 1678 -5.9; 1846 -5.9; 2031 -6.2; 2234 -6.6; 2457 -6.8; 2703 -6.4; 2973 -5.7; 3270 -4.9; 3597 -4.0; 3957 -3.1; 4353 -2.4; 4788 -2.2; 5267 -2.8; 5793 -4.6; 6373 -7.5; 7010 -8.5; 7711 -8.9; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Corona sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Corona sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.78 | 7.1 dB  |
| Peaking | 149 Hz  | 0.55 | -3.3 dB |
| Peaking | 888 Hz  | 1.91 | 2.7 dB  |
| Peaking | 4702 Hz | 2.25 | 4.7 dB  |
| Peaking | 7121 Hz | 3.5  | -3.8 dB |
| Peaking | 2484 Hz | 3.12 | -1.1 dB |
| Peaking | 3625 Hz | 4.74 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kumitate%20KL-Corona%20sample%202/Kumitate%20KL-Corona%20sample%202.png)