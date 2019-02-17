# Audeze EL8 Open
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.7; 28 -0.8; 31 -0.9; 34 -0.9; 37 -1.0; 41 -1.1; 45 -1.4; 49 -1.5; 54 -1.4; 60 -1.9; 66 -2.6; 72 -2.9; 79 -3.0; 87 -3.3; 96 -3.7; 106 -4.0; 116 -4.1; 128 -4.4; 141 -4.6; 155 -4.8; 170 -5.0; 187 -5.1; 206 -5.3; 227 -5.3; 249 -5.5; 274 -5.6; 302 -5.6; 332 -5.5; 365 -5.2; 402 -5.2; 442 -5.3; 486 -5.4; 535 -5.5; 588 -5.3; 647 -5.4; 712 -5.8; 783 -5.9; 861 -6.2; 947 -6.5; 1042 -6.3; 1146 -6.9; 1261 -6.8; 1387 -6.7; 1526 -6.3; 1678 -6.1; 1846 -6.7; 2031 -7.5; 2234 -7.7; 2457 -6.9; 2703 -4.6; 2973 -4.1; 3270 -3.9; 3597 -2.5; 3957 -1.5; 4353 -2.9; 4788 -4.6; 5267 -3.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze EL8 Open GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze EL8 Open ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 28 Hz   |  0.41 | 4.9 dB  |
| Peaking | 32 Hz   |  0.05 | 1.0 dB  |
| Peaking | 3854 Hz |  3.23 | 4.7 dB  |
| Peaking | 6033 Hz |  3.65 | 6.6 dB  |
| Peaking | 7751 Hz |  1.67 | -1.0 dB |
| Peaking | 568 Hz  |  2.34 | 0.6 dB  |
| Peaking | 1190 Hz |  4.43 | -0.8 dB |
| Peaking | 2249 Hz |  4.01 | -2.2 dB |
| Peaking | 2800 Hz |  5.42 | 2.0 dB  |
| Peaking | 4991 Hz | 17.25 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | 1.4 dB  |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20EL8%20Open/Audeze%20EL8%20Open.png)