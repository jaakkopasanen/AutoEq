# Aedle VK1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.2; 45 -2.5; 49 -3.7; 54 -5.2; 60 -6.7; 66 -8.1; 72 -9.2; 79 -10.3; 87 -11.1; 96 -11.6; 106 -11.6; 116 -11.4; 128 -11.2; 141 -10.9; 155 -10.6; 170 -10.2; 187 -9.9; 206 -9.6; 227 -9.2; 249 -8.9; 274 -8.5; 302 -7.9; 332 -7.4; 365 -7.6; 402 -7.2; 442 -6.7; 486 -6.3; 535 -5.7; 588 -6.6; 647 -6.6; 712 -5.0; 783 -4.3; 861 -4.8; 947 -5.8; 1042 -7.0; 1146 -8.2; 1261 -9.5; 1387 -10.9; 1526 -12.1; 1678 -12.3; 1846 -10.7; 2031 -10.4; 2234 -9.3; 2457 -7.7; 2703 -6.0; 2973 -3.8; 3270 -2.4; 3597 -1.2; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.0; 6373 -2.3; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Aedle VK1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Aedle VK1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.52 | 9.8 dB  |
| Peaking | 87 Hz   | 0.6  | -9.2 dB |
| Peaking | 847 Hz  | 1.56 | 3.6 dB  |
| Peaking | 1646 Hz | 1.21 | -7.1 dB |
| Peaking | 4271 Hz | 1.19 | 7.6 dB  |
| Peaking | 565 Hz  | 3.66 | 1.5 dB  |
| Peaking | 616 Hz  | 8.08 | -2.8 dB |
| Peaking | 4530 Hz | 4.26 | -1.7 dB |
| Peaking | 6249 Hz | 1.5  | 3.5 dB  |
| Peaking | 7666 Hz | 1.54 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.9 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Aedle%20VK1/Aedle%20VK1.png)