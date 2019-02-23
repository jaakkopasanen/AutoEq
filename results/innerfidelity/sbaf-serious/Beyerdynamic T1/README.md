# Beyerdynamic T1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.0; 28 -1.5; 31 -2.0; 34 -2.3; 37 -2.6; 41 -2.9; 45 -3.2; 49 -3.5; 54 -3.5; 60 -3.1; 66 -3.7; 72 -4.6; 79 -5.2; 87 -5.7; 96 -6.1; 106 -6.5; 116 -6.7; 128 -7.0; 141 -7.3; 155 -7.4; 170 -7.6; 187 -7.6; 206 -7.7; 227 -7.6; 249 -7.6; 274 -7.5; 302 -7.4; 332 -7.2; 365 -7.0; 402 -6.8; 442 -6.6; 486 -6.4; 535 -6.3; 588 -5.9; 647 -5.6; 712 -5.4; 783 -5.1; 861 -5.4; 947 -5.3; 1042 -4.9; 1146 -4.4; 1261 -4.7; 1387 -4.8; 1526 -5.2; 1678 -6.1; 1846 -6.6; 2031 -5.6; 2234 -5.1; 2457 -6.1; 2703 -5.8; 2973 -5.1; 3270 -4.0; 3597 -4.5; 3957 -5.2; 4353 -6.1; 4788 -3.4; 5267 -0.5; 5793 -7.2; 6373 -10.0; 7010 -5.7; 7711 -11.3; 8482 -15.4; 9330 -13.4; 10263 -7.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 24 Hz    |  1.09 | 5.9 dB   |
| Peaking | 59 Hz    |  3.11 | 2.5 dB   |
| Peaking | 1860 Hz  |  0.48 | 1.3 dB   |
| Peaking | 5157 Hz  |  9.22 | 6.9 dB   |
| Peaking | 8635 Hz  |  3.96 | -10.1 dB |
| Peaking | 227 Hz   |  0.46 | -3.0 dB  |
| Peaking | 435 Hz   |  0.11 | 1.7 dB   |
| Peaking | 1879 Hz  |  1.85 | -2.2 dB  |
| Peaking | 6158 Hz  | 13    | -5.0 dB  |
| Peaking | 10786 Hz |  7.46 | 1.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.2 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T1/Beyerdynamic%20T1.png)