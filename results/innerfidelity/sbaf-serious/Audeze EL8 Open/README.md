# Audeze EL8 Open
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -2.8; 25 -2.9; 28 -3.0; 31 -3.1; 34 -3.1; 37 -3.2; 41 -3.3; 45 -3.6; 49 -3.7; 54 -3.6; 60 -4.1; 66 -4.8; 72 -5.1; 79 -5.2; 87 -5.5; 96 -5.9; 106 -6.2; 116 -6.2; 128 -6.6; 141 -6.8; 155 -7.0; 170 -7.2; 187 -7.3; 206 -7.5; 227 -7.5; 249 -7.7; 274 -7.7; 302 -7.8; 332 -7.7; 365 -7.4; 402 -7.4; 442 -7.5; 486 -7.6; 535 -7.6; 588 -7.4; 647 -7.6; 712 -8.0; 783 -8.1; 861 -8.4; 947 -8.7; 1042 -8.5; 1146 -9.1; 1261 -9.0; 1387 -8.9; 1526 -8.5; 1678 -8.3; 1846 -8.9; 2031 -9.7; 2234 -9.9; 2457 -9.1; 2703 -6.8; 2973 -6.3; 3270 -6.1; 3597 -4.7; 3957 -3.6; 4353 -5.1; 4788 -6.8; 5267 -5.7; 5793 -0.5; 6373 -0.7; 7010 -3.7; 7711 -5.9; 8482 -6.2; 9330 -6.5; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.6; 16529 -6.2; 18182 -6.2; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze EL8 Open GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze EL8 Open ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 30 Hz    |  0.44 | 3.7 dB  |
| Peaking | 471 Hz   |  0.11 | -1.5 dB |
| Peaking | 3224 Hz  |  0.58 | -3.5 dB |
| Peaking | 3585 Hz  |  1.95 | 5.9 dB  |
| Peaking | 6205 Hz  |  3.92 | 8.1 dB  |
| Peaking | 1706 Hz  |  6.83 | 0.9 dB  |
| Peaking | 2172 Hz  |  6.63 | -1.2 dB |
| Peaking | 5027 Hz  | 10.19 | -5.7 dB |
| Peaking | 5063 Hz  |  3.37 | 2.5 dB  |
| Peaking | 11255 Hz |  3.18 | 0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -1.9 dB |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20EL8%20Open/Audeze%20EL8%20Open.png)