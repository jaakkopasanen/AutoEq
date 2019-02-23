# NVX XPT100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.2; 23 -1.6; 25 -2.0; 28 -2.5; 31 -3.0; 34 -3.3; 37 -3.6; 41 -3.9; 45 -4.1; 49 -4.3; 54 -4.6; 60 -4.9; 66 -5.2; 72 -5.4; 79 -5.7; 87 -6.0; 96 -6.3; 106 -6.4; 116 -6.5; 128 -7.3; 141 -8.0; 155 -8.5; 170 -7.6; 187 -8.3; 206 -8.2; 227 -7.3; 249 -5.8; 274 -3.2; 302 -1.8; 332 -2.6; 365 -3.8; 402 -4.7; 442 -5.2; 486 -6.1; 535 -6.5; 588 -6.4; 647 -6.6; 712 -6.8; 783 -6.4; 861 -6.6; 947 -7.1; 1042 -7.6; 1146 -8.0; 1261 -8.5; 1387 -9.3; 1526 -10.0; 1678 -10.2; 1846 -10.4; 2031 -10.3; 2234 -9.9; 2457 -9.0; 2703 -8.5; 2973 -6.3; 3270 -4.3; 3597 -6.9; 3957 -6.6; 4353 -5.6; 4788 -4.2; 5267 -1.5; 5793 -0.5; 6373 -4.1; 7010 -3.3; 7711 -5.5; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -8.1; 20000 -12.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NVX XPT100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NVX XPT100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.41 | 5.4 dB  |
| Peaking | 225 Hz  | 0.86 | -4.8 dB |
| Peaking | 302 Hz  | 2.05 | 7.8 dB  |
| Peaking | 1801 Hz | 1.3  | -4.9 dB |
| Peaking | 5635 Hz | 3.5  | 5.7 dB  |
| Peaking | 2822 Hz | 3.81 | -1.4 dB |
| Peaking | 3163 Hz | 5.88 | 4.8 dB  |
| Peaking | 3625 Hz | 3    | -1.7 dB |
| Peaking | 5189 Hz | 2.83 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | 1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NVX%20XPT100/NVX%20XPT100.png)