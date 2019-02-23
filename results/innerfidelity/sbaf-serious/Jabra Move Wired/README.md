# Jabra Move Wired
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.4; 23 -11.5; 25 -11.6; 28 -11.6; 31 -11.6; 34 -11.4; 37 -11.3; 41 -10.9; 45 -10.1; 49 -9.3; 54 -9.6; 60 -10.5; 66 -10.3; 72 -9.8; 79 -9.1; 87 -9.3; 96 -10.7; 106 -11.6; 116 -11.7; 128 -11.4; 141 -11.6; 155 -11.0; 170 -10.6; 187 -10.1; 206 -9.1; 227 -7.9; 249 -7.8; 274 -8.8; 302 -9.4; 332 -9.4; 365 -9.3; 402 -9.1; 442 -9.3; 486 -9.5; 535 -9.6; 588 -9.5; 647 -9.4; 712 -8.9; 783 -8.2; 861 -9.0; 947 -8.2; 1042 -6.9; 1146 -7.5; 1261 -7.5; 1387 -7.4; 1526 -7.3; 1678 -7.1; 1846 -6.1; 2031 -5.1; 2234 -4.1; 2457 -3.0; 2703 -2.5; 2973 -3.0; 3270 -1.9; 3597 -0.6; 3957 -0.5; 4353 -1.9; 4788 -2.9; 5267 -0.5; 5793 -0.5; 6373 -1.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Move Wired GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Move Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.54 | -5.1 dB |
| Peaking | 128 Hz  | 1.39 | -4.4 dB |
| Peaking | 553 Hz  | 0.65 | -2.9 dB |
| Peaking | 3489 Hz | 1.36 | 5.5 dB  |
| Peaking | 5817 Hz | 3.55 | 5.0 dB  |
| Peaking | 237 Hz  | 9    | 1.4 dB  |
| Peaking | 1653 Hz | 3.23 | -1.3 dB |
| Peaking | 2739 Hz | 1.59 | 1.9 dB  |
| Peaking | 3030 Hz | 4.6  | -2.7 dB |
| Peaking | 8414 Hz | 3.3  | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Jabra%20Move%20Wired/Jabra%20Move%20Wired.png)