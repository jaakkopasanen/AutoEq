# Koss Porta Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.2; 34 -2.2; 37 -3.1; 41 -4.1; 45 -5.1; 49 -5.9; 54 -6.9; 60 -7.9; 66 -8.7; 72 -9.5; 79 -10.1; 87 -10.8; 96 -11.3; 106 -11.7; 116 -11.7; 128 -11.9; 141 -11.9; 155 -11.8; 170 -11.6; 187 -11.2; 206 -10.9; 227 -10.5; 249 -10.1; 274 -9.7; 302 -9.4; 332 -9.0; 365 -8.5; 402 -8.1; 442 -7.6; 486 -7.3; 535 -7.0; 588 -6.5; 647 -6.4; 712 -6.2; 783 -6.0; 861 -6.1; 947 -6.2; 1042 -6.2; 1146 -6.4; 1261 -6.8; 1387 -7.6; 1526 -8.6; 1678 -9.6; 1846 -10.1; 2031 -9.7; 2234 -8.3; 2457 -6.0; 2703 -3.6; 2973 -1.1; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -3.2; 4788 -4.6; 5267 -1.9; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Porta Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.88 | 7.1 dB  |
| Peaking | 124 Hz  | 0.58 | -6.0 dB |
| Peaking | 1940 Hz | 2.49 | -5.2 dB |
| Peaking | 3350 Hz | 1.88 | 7.0 dB  |
| Peaking | 5991 Hz | 4.15 | 5.7 dB  |
| Peaking | 295 Hz  | 1.96 | -0.5 dB |
| Peaking | 630 Hz  | 2.18 | 0.4 dB  |
| Peaking | 897 Hz  | 1.14 | 0.8 dB  |
| Peaking | 1552 Hz | 4.85 | -1.0 dB |
| Peaking | 8301 Hz | 4.16 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20Porta%20Pro/Koss%20Porta%20Pro.png)