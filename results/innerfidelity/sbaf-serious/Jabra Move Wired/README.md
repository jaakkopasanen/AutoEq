# Jabra Move Wired
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.4; 23 -10.5; 25 -10.6; 28 -10.6; 31 -10.5; 34 -10.4; 37 -10.2; 41 -9.9; 45 -9.1; 49 -8.3; 54 -8.5; 60 -9.5; 66 -9.3; 72 -8.8; 79 -8.1; 87 -8.3; 96 -9.7; 106 -10.6; 116 -10.6; 128 -10.4; 141 -10.6; 155 -10.0; 170 -9.6; 187 -9.1; 206 -8.1; 227 -6.9; 249 -6.8; 274 -7.8; 302 -8.4; 332 -8.4; 365 -8.2; 402 -8.1; 442 -8.3; 486 -8.5; 535 -8.6; 588 -8.5; 647 -8.4; 712 -7.8; 783 -7.2; 861 -8.0; 947 -7.2; 1042 -5.9; 1146 -6.5; 1261 -6.5; 1387 -6.4; 1526 -6.3; 1678 -6.0; 1846 -5.1; 2031 -4.1; 2234 -3.0; 2457 -2.0; 2703 -1.5; 2973 -2.0; 3270 -0.9; 3597 -0.5; 3957 -0.5; 4353 -1.3; 4788 -1.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Move Wired GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Move Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.67 | -4.1 dB |
| Peaking | 128 Hz  | 1.51 | -3.9 dB |
| Peaking | 540 Hz  | 0.95 | -2.1 dB |
| Peaking | 3330 Hz | 1.2  | 5.9 dB  |
| Peaking | 5797 Hz | 3.38 | 4.8 dB  |
| Peaking | 1685 Hz | 2.18 | -1.8 dB |
| Peaking | 2318 Hz | 0.97 | 1.6 dB  |
| Peaking | 3031 Hz | 5.02 | -2.1 dB |
| Peaking | 8400 Hz | 2.98 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | 0.0 dB  |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Jabra%20Move%20Wired/Jabra%20Move%20Wired.png)