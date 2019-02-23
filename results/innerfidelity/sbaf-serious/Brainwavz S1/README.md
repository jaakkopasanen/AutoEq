# Brainwavz S1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.1; 23 -10.2; 25 -10.3; 28 -10.4; 31 -10.5; 34 -10.5; 37 -10.6; 41 -10.7; 45 -10.8; 49 -10.9; 54 -11.0; 60 -11.2; 66 -11.4; 72 -11.5; 79 -11.7; 87 -11.9; 96 -12.1; 106 -12.1; 116 -12.0; 128 -12.0; 141 -11.9; 155 -11.7; 170 -11.4; 187 -11.1; 206 -10.7; 227 -10.1; 249 -9.7; 274 -9.1; 302 -8.4; 332 -7.8; 365 -7.1; 402 -6.4; 442 -5.6; 486 -5.0; 535 -4.3; 588 -3.3; 647 -2.7; 712 -2.2; 783 -1.6; 861 -1.3; 947 -1.1; 1042 -1.0; 1146 -0.7; 1261 -0.5; 1387 -0.8; 1526 -2.1; 1678 -3.7; 1846 -4.0; 2031 -3.7; 2234 -3.5; 2457 -3.1; 2703 -3.1; 2973 -3.1; 3270 -3.4; 3597 -3.9; 3957 -5.4; 4353 -8.4; 4788 -10.1; 5267 -10.5; 5793 -6.4; 6373 -2.5; 7010 -2.9; 7711 -5.1; 8482 -5.4; 9330 -5.4; 10263 -6.3; 11289 -5.7; 12418 -5.4; 13660 -5.6; 15026 -7.4; 16529 -5.4; 18182 -5.4; 20000 -7.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Brainwavz S1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz S1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.59 | -3.2 dB |
| Peaking | 142 Hz  | 0.29 | -7.0 dB |
| Peaking | 853 Hz  | 0.47 | 5.9 dB  |
| Peaking | 4888 Hz | 4.98 | -6.5 dB |
| Peaking | 1379 Hz | 2.7  | 1.8 dB  |
| Peaking | 1713 Hz | 2.88 | -2.3 dB |
| Peaking | 3250 Hz | 1.52 | 3.1 dB  |
| Peaking | 4567 Hz | 0.62 | -2.4 dB |
| Peaking | 6653 Hz | 4.83 | 5.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Brainwavz%20S1/Brainwavz%20S1.png)