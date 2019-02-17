# Klipsch Image One
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.8; 45 -1.4; 49 -2.0; 54 -2.7; 60 -3.3; 66 -3.8; 72 -4.4; 79 -5.2; 87 -6.0; 96 -6.8; 106 -7.3; 116 -7.7; 128 -8.2; 141 -8.5; 155 -8.7; 170 -8.7; 187 -8.9; 206 -8.8; 227 -8.5; 249 -8.2; 274 -8.1; 302 -8.0; 332 -7.8; 365 -7.5; 402 -7.4; 442 -7.1; 486 -6.9; 535 -6.4; 588 -5.4; 647 -4.7; 712 -5.1; 783 -5.0; 861 -5.8; 947 -6.4; 1042 -6.7; 1146 -7.3; 1261 -8.0; 1387 -8.5; 1526 -8.9; 1678 -9.5; 1846 -10.0; 2031 -10.3; 2234 -10.6; 2457 -10.8; 2703 -11.5; 2973 -11.5; 3270 -10.5; 3597 -8.2; 3957 -5.5; 4353 -3.9; 4788 -3.5; 5267 -2.9; 5793 -5.0; 6373 -7.5; 7010 -9.2; 7711 -6.9; 8482 -6.9; 9330 -8.0; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Image One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.53 | 6.5 dB  |
| Peaking | 153 Hz  | 0.88 | -3.2 dB |
| Peaking | 2821 Hz | 1.15 | -6.5 dB |
| Peaking | 4721 Hz | 1.69 | 6.3 dB  |
| Peaking | 6822 Hz | 4.4  | -4.0 dB |
| Peaking | 453 Hz  | 1.04 | -1.0 dB |
| Peaking | 681 Hz  | 1.62 | 2.8 dB  |
| Peaking | 1508 Hz | 2.48 | -1.0 dB |
| Peaking | 8221 Hz | 3.57 | 0.8 dB  |
| Peaking | 9160 Hz | 5.52 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20Image%20One/Klipsch%20Image%20One.png)